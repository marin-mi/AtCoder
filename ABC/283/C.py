S = input()

cnt = 0
i = 0
while i < len(S):
    if S[i:i+2] == '00':
        cnt += 1
        i += 1
    i += 1

print(len(S) - cnt)

# 公式の解説
# countとreplaceを使わない方法
