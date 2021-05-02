# 有条件者可使用PyPy运行。
from itertools import product


ABC = lambda x: map(lambda y: ''.join(y), product('abcdefghijklmnopqrstuvwxyz', repeat=x))
GET = lambda x, d: b'' if len(d) < 1 << x else ''.join(map(lambda y: y[0], sorted(d.items(), key=lambda z: z[1], reverse=True)[:1<<x])).encode('ascii')
def GET_(d):
    x = len(d)
    if x >= 16:     x = 16
    elif x >= 8:    x = 8
    elif x >= 4:    x = 4
    elif x >= 2:    x = 2
    elif x >= 1:    x = 1
    else: return    b''
    return          ''.join(map(lambda y: y[0], sorted(d.items(), key=lambda z: z[1], reverse=True)[:x])).encode('ascii')

langs = {}
for lang, weight in (('de', 1), ('en', 30), ('es', 2), ('fr', 4)):
    with open(f'out_{lang}.txt') as f:
        langs[lang] = (f.read().splitlines(), weight)

def generate(plan, allow_hyphen=False):
    dyn = isinstance(plan, int)
    max_trace = plan if dyn else len(plan)
    transfer = {}

    for words, weight in langs.values():
        for word in words:
            for i, c in enumerate(f'{word}-' if allow_hyphen else word):
                for j in range(1, (max_trace if i >= max_trace else i if i > 0 else 1) + 1):
                    try:
                        transfer[word[i-j:i]][c] += weight
                    except KeyError:
                        try:
                            transfer[word[i-j:i]][c] = weight
                        except KeyError:
                            transfer[word[i-j:i]] = {c: weight}

    if dyn:
        filename = f'0x{plan}'
    else:
        filename = '-'.join(map(str, plan))

    with open(f'{filename}{"+H" if allow_hyphen else ""}.txt', 'wb') as f:
        if dyn:
            for i in range(0, max_trace):
                for k in ABC(i):
                    if k in transfer:
                        f.write(GET_(transfer[k]))
                    f.write(b'\n')
        else:
            for i, n in zip(range(0, max_trace), plan):
                for k in ABC(i):
                    if k in transfer:
                        f.write(GET(n, transfer[k]))
                    f.write(b'\n')

generate((4, 4, 4))
generate((4, 4, 4, 4))
generate((4, 4, 4, 3, 2))
generate(3)
generate(4)
generate(5)
generate((4, 4, 4), True)
generate((4, 4, 4, 4), True)
generate((4, 4, 4, 3, 2), True)
generate(3, True)
generate(4, True)
generate(5, True)