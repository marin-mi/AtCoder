S = input()
N = len(S)

for i in range(N, 0, -1):
    if S[i - 1] == 'a':
        print(i)
        exit()
print(-1)

# rangeを使って後ろから順番に
# 文字列が3つならリストの最後の添字は2になるためi - 1とする
# 長さをNとする
# range(start, stop, step)