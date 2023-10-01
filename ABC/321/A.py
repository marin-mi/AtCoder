N = input()

flag = True
for i in range(len(N) - 1):
    if int(N[i]) <= int(N[i + 1]):
        flag = False
        break

if flag:
    print('Yes')
else:
    print('No')

# int型で受け取ると各桁に分解する必要がある
# N[i]は文字列なためint型にする
