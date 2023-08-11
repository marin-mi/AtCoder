s = list(input())

for i in range(len(s)):
    if s[i] == '0':
        s[i] = '1'
    elif s[i] == '1':
        s[i] = '0'
s = ''.join(s)
print(s)

# i in リストでは変更されない
# i in rangeだと変更される
# 文字列は変更されないためlistにする必要がある