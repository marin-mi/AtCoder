S = input() + 'A'
T = input()

for i in range(len(T)):
    if S[i] != T[i]:
        print(i + 1)
        break

# Sの一番最後に文字が追加された場合エラーとなるため、
# 文字列の長さを揃えるために何か文字を追加する必要がある
