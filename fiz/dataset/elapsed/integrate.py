# 不觉得代码顶头没有几句`import`很难受吗？
# 有条件者可使用PyPy运行。


def normalize(word: str) -> str:
    return ''.join({
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ý': 'y',
        'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
        'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u',
        'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u', 'ÿ': 'y',
        'ç': 'c', 'ş': 's', 'å': 'a',   # 很他妈无奈，这些都是啥？
        'ã': 'a', 'õ': 'o', 'ñ': 'n',
        'ą': 'a', 'ę': 'e', 'į': 'i', 'ų': 'u',
        'æ': 'ae', 'œ': 'oe', 'ø': 'oe', 'ĳ': 'ij', 'ß': 'ss',
    }.get(c, c) for c in word)


for lang in ('de', 'en', 'es', 'fr'):
    result = set()
    with open(f'{lang}.txt', encoding='utf-8') as f:
        for word in f.read().splitlines():
            result.update(normalize(word.lower()).split('-'))   # 还有连字符？！

    with open(f'out_{lang}.txt', 'wb') as f:
        for word in sorted(result):
            if len(word) >= 5:  # 过滤单词！
                try:
                    f.write(word.encode('ascii'))
                    f.write(b'\n')
                except Exception as e:
                    print(e, word)
                    exit()