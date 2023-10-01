N = input()

for i in range(len(N) - 1):
    if int(N[i]) <= int(N[i + 1]):
        print('No')
        exit()
print('Yes')

# exit()を使ってコードを短くした
# exit()はプログラムを終了、breakはfor文を抜ける
