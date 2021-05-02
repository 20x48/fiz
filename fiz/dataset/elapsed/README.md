# FIZ

> ~~*起名字是他妈真的烦，我能他妈花好几个小时在这上面。*~~
> 
> ~~（是的，就是这个项目存在过的问题）~~
>
> 这个项目不仅可以用来生成好看的哈希，~~*我还希望这他妈能帮我解决起名问题。*~~
>
> ……
>
> *现在，我知道了，就从没有哪一代算法考虑过单词结尾来看，这玩意根本不可能帮我解决起名问题。*
>
> ---
>
> *你可以把这看成是个被遗忘的README。*

我花了两天时间来完成这个项目。

[✱](#大致思路) 原先有很多实现方法，但是它们都已被淘汰，于是现在就只剩一种了。

[✱](#数据集的选择) 我错了我再也不敢缝合多国语言了。

## 大致思路
这应该是在某种程度上的马尔可夫链；拥有一个转移表，形如：

``` python
{
    '': 'abcd',
    'a': 'bc',
    'ab': 'd',
    'bd': 'i',
    'bdi': ''
}
```

这儿有一个常量：`MAX_TRACE = 4`

- 输入是一串字节串（`bytes`），目前的输出缓冲是空的。
- 对于每个输出缓冲的状态，算法会试图从尾向头读取*最多*`MAX_TRACE`个字符，并在转移表当中查找；

    “*最多*”是因为我的算法实现了降级，这样便不可能出现被迫中断的情景了。
- 转移表的“值”（键值对的值）的长度必定是`pow(2, n)`或`0`，这样才可以准确的消耗输入。
- 转移表的“键”的长度越长，那么它的值的长度为`0`的可能性就越大。存储（特么的要我怎么描述啊？？？）：
    ```
        1 | (for empty key)
        2 | "a"
        3 | "b"
      ... | ...
       26 | "y"
       27 | "z"
       28 | "aa"
       29 | "ab"
    ```
    以此类推……看不懂就算了。
- ……键的长度称作它们的级别。
- `4x3`描述的是“级”和“值长度”的关系，即一个方案：最多有三级，每级都消耗`4bit`。
- `4x3-3-2`也是一个方案：在零至二级时消耗`4bit`，在三级时消耗`3bit`，在四级时消耗`2bit`。

    很明显这会产生不定长的输出，但是单词生成的效果应该也更好。
- 实际上还有另外的方案算法：级和值长度可以并不一定需要是固定的。举个例子，相比于`ti?`和`xx?`，肯定是前者的`?`的可能性更多……总之就是它们的最大值并不合理，不能完全发挥它们的潜力。

    这样单词生成的效果应该是最好的，但也是最慢的；称其方案为`0xN`；`N`是它的最大级数减一。
- 方案可能会带有`-H`后缀，这是启用了断词，原先的编码量不会变，但视觉效果可能会更好。

    （以下所有方案都支持启用断词）
- 为了调和XX和YY的关系，总之就是提供有不同的方案：
    |方案|编码量|转移表大小|性能|生成的单词的视觉效果|
    |:-:|:-:|:-:|:-:|:-:|
    |`4x3`|定长，十六进制|6KB|⭐⭐⭐⭐|⭐|
    |`4x4`|定长，十六进制|54KB|⭐⭐⭐|⭐⭐|
    |`4x3-3-2`|变长，未知|662KB|⭐⭐|⭐⭐⭐|
    |`0x3`|变长，未知|8KB|⭐⭐⭐|⭐⭐|
    |`0x4`|变长，未知|90KB|⭐⭐|⭐⭐⭐|
    |`0x5`|变长，未知|849KB|⭐|⭐⭐⭐⭐|

    （⭐请以实际为准，因为都是凭感觉得出的；最大为4）

> *妈的写这些东西真的好特么难受啊半天憋不出一个字来！！（前半部分）*

> ……所以，最后只有`0x5-H`留了下来。

## 数据集的选择

这是在“大清理”之后仅存的实现、使用德`[~1.6M*1]`、法`[~0.3M*4]`、英`[~0.25M*30]`、西班牙`[~0.6M×2]`（单词数乘权重）训练出的转移表的效果（已启用连字）：

    -- Rsgieiars.Mlbwieuvgeaabbnsiyy.Siunoiosactbuzruaayaeooaeeerucybhruu.Sneoaeeiieeuvnruhoaeueumo.
    -- Ioeuoiierutuooymierueeukanoeeaaesyiumos.Turu.Mbvditkaafmuaedoeseaeycoowaiesulaeeylnagrui.Cgla
    -- Aeruyyioluaeeleisafuugoeaeopruiweoaeyoeyweaeouoesuiiouueisadttoozcoiulnabttooumiumiuoaaeeruceue
    -- B.Lho.Asmseiogeisacseiuoesooou.Tkuyyxoseuhegeplt.Cgeu.Poy.Uzauifaysafuukaerutsoe.Lhoga.C

*数据来自<https://github.com/lorenbrichter/Words>，没有加入这个repo，感兴趣的可以自己下来尝试；过滤长度小于5的单词。*

*“也许这个目录下的一些被遗忘的脚本可以帮助你。”*

---

然后，这是仅使用英语`[~0.36M]`训练出的转移表的效果（已启用连字）：

    -- Ntpuoiwe.Dlha.If.Nmiaa.Uweieaai.Rltpprus.Ro.Cofculsuerrvmpti.Ucaoaewoaimdmoooefsolnahiaa.Mndauhu.S
    -- Duweiyyvdoeuheotcoosopsaegfcueaeuoiyhuh.Ptteo.Ctpcso.Pneiuyteuserr.Adqiaa.Pduioaiebruoehrthe.F.
    -- Ocadoebrudoalyioythi.Uyiiyalwe.Ieiucruytciu.Ewaaenrudoiuerudhyw.Dibtmibrudhe.B.Dclhdlbm.Uh
    -- Auuserr.Nfdaooieue.Hohrthe.Aibsllatuha.Rpnue.Abiyleiiawu.Anoglir.Nydey.Cjgoewaanaieotweaeururui

*数据来自<https://github.com/dwyl/english-words>；过滤长度小于5的单词。*

虽然仍存在此类现象，但就是感觉比多国语言要好了。大概这就是“异域风情”的影响吧……还是只有英语比较舒服。