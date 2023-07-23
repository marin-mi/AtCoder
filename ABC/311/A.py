N = int(input())
S = input()

count = {'A': 0, 'B': 0, 'C': 0}

for i in range(N):
    count[S[i]] += 1
    if all(c > 0 for c in count.values()):
        print(i + 1)
        break