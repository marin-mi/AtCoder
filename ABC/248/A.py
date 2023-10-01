S = input()

for i in range(0, 10):
    if str(i) not in list(S):
        print(i)
        exit()
