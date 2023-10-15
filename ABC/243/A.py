v, a, b, c = map(int, input().split())

while True:
    v -= a
    if v < 0:
        print('F')
        exit()
    v -= b
    if v < 0:
        print('M')
        exit()
    v -= c
    if v < 0:
        print('T')
        exit()

# 公式の解説
# while Trueとはexit()が現れるまで無限ループを行う
