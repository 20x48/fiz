# FIZ

用于将`HEX`转换为`Human.Spellable.Words.`（人类可拼读）的工具 . . 我尽力了。

## 特性

1. 编码大小甚至比八进制还要糟糕。
2. 动态输出长度。
3. 但最重要的是，**人类可拼读**！

忽略前两项吧～别在你的用户界面上节省太多～

**注意：**
尽管已经对广泛的输入（和正确的类型）进行了测试，但仍不能保证不会出任何问题。
在历经时间考验之前，我不能肯定任何东西（BETA版本不要立Flag啊!）。
另外，你可以通过`except fiz.FizError`来捕获它们。

## 安装

    pip install fiz

## 用法

``` jupyter
In [1]: from fiz import Fiz

In [2]: Fiz(b'some bytes...')
Out[2]: 'Dacyorrheumiesciendlichouquinzai.Rsmoochylith.D.'

In [3]: Fiz(b'custom joiner', '-')
Out[3]: 'Taideutidipladeepfold-Tsphycomb-Nuf-Re'
```

## 长长的示例

```
--- 1 ---
In:  C7D2D5DBC1F8A3ACB4FDCBFBC8D5A3ACD4D9CFE0B7EA
Out: Ndfallbendol.Skwogmirinicksongymnadequeet.Dde.Mser.Npassu.Rggily.Mnchoce
--- 2 ---
In:  CED2CEAAC4E320B3AAD2BBC7FA20C8E7D3CECBBFB5C4C6F8CFA2
Out: Nkwoodlitzes.Mmhorichloanemid.Elsacksummox.Usallys.Ufan.T.Iflask.Pos.Foxshipfe
--- 3 ---
In:  CCE1B1CAD7DFB5A4C7E020BAE1C6C3CBAEC4AB20B7D6B1F0D2D1B9FDC7A7C7EF20CAAEC0EFC7EFD2B6BAEC20D6B4B1CABBADCCC4CEAABEFDC1F420CAB1B9E2C8E7C1F7CBAE20B5E3B5E3B0A7B3EE20BDF1CFA6BFD5D2D0D0A1C2A520BEB2BFB4BAD3B1DFBFDDC1F820C8D4BFC9BCFBBEFDB7F1
Out: Nuptigroizedly.Tls.Dwyershortfirs.Net.Dr.Pyeticshipinofoilershopped.Ifehol.Pbonedly.Islesplin.Aeohippro.Ddlieshit.Hemphysnowts.Fuz.Tl.Dulan.Ilts.Osspromemoiredackeersty.Hfoe.Sknessly.Ann.Abag.Tredoximoblershedhandybonehowleecelicerioleums.Auked.Cquopersabdacistabdosimumly.Mstrail.Ormidomy.Ilotumta.Cnotiza.Tapmongcourebreadnut.Cogwooleye.Fedomizil.Dl.Fnullbit.Bi
--- 4 ---
In:  D2FBB9FDD2BBD5B5D3EABAF3CCECC7E0B4C920D2B2B2BBCBE3C0B4B3D9
Out: Icwiserraghs.Ognescati.Mfuseesawis.Mrena.Aggeis.Shynesicaliburoo.Hods.Nff.Ainworl.Aec
--- 5 ---
In:  B1CBCAB1C1B520D4B8BAA3CAC4C9BDC3CB
Out: Himsas.Cl.Amagilanco.Mlittifocklied.Uebrecco.Aia
```