S = input()

for s in S[1:16:2]:
    if s == '0':
        pass
    else:
        print('No')
        exit()
print('Yes')
