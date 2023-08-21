S = input()

A = ['a', 'e', 'i', 'o', 'u']
ans = ''

for s in S:
    if s not in A:
        ans += s
print(ans)

# メソッドを使わずに削除する方法
# sがリストAの要素でなかったらansに足していく