n = int(input())
s = input()

for i in range(n - 1):
    if s[i] == s[i + 1]:
        print('No')
        exit()
print('Yes')

# exitはプログラム自体が終わる
# yesがprintされない
# breakはfor文抜け出す