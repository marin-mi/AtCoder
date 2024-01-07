S = input()
T = input()

flag = True
tmp = (ord(T[0]) - ord(S[0])) % 26
for i in range(len(S)):
    diff = (ord(T[i]) - ord(S[i])) % 26
    if diff != tmp:
        flag = False

if flag:
    print('Yes')
else:
    print('No')

# B_asをflagを使って書いてみた
