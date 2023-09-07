N = int(input())
S = [input() for _ in range(N)]

iti = ['H', 'D', 'C', 'S']
ni = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
for i in range(N):
    if not S[i][0] in iti:
        print('No')
        exit()
    elif not S[i][1] in ni:
        print('No')
        exit()
    elif len(set(S)) != N:
        print('No')
        exit()
print('Yes')
