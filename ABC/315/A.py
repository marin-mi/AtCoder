S = input()

S = S.replace('a', '')
S = S.replace('e', '')
S = S.replace('i', '')
S = S.replace('o', '')
S = S.replace('u', '')

print(S)

# S = にしないと変更されない
# S.replace('文字', '')でその文字は削除される