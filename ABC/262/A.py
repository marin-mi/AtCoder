Y = int(input())

for i in range(1000):
    if Y % 4 == 2:
        print(Y)
        exit()
    else:
        Y += 1