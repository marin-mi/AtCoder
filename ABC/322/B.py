N, M = map(int, input().split())
S = input()
T = input()

atama = T.startswith(S)
osiri = T.endswith(S)

if atama and osiri:
    print(0)
elif atama:
    print(1)
elif osiri:
    print(2)
else:
    print(3)
