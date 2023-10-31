n = int(input())

while True:
    moji = str(n)
    seki = int(str(moji[0])) * int(str(moji[1]))
    if seki == int(str(moji[2])):
        print(n)
        exit()
    n += 1
