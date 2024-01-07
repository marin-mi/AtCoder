S = input()
T = input()

tmp = (ord(T[0]) - ord(S[0])) % 26
for i in range(len(S)):
    diff = (ord(T[i]) - ord(S[i])) % 26
    if diff != tmp:
        print('No')
        exit()

print('Yes')

# 自分で考えた
# 別にi=0の時が重複してもいいから5行目のようにしている
