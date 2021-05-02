# 不觉得代码顶头没有几句`import`很难受吗？
# 有条件者可使用PyPy运行。


result = set()
with open('words_alpha.txt', encoding='utf-8') as f:
    for word in f.read().splitlines():
        result.add(word)

with open('out.txt', 'wb') as f:
    for word in sorted(result):
        if len(word) >= 5:  # 过滤单词！
            try:
                f.write(word.encode('ascii'))
                f.write(b'\n')
            except Exception as e:
                print(e, word)
                exit()