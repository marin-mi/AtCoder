K = int(input())

cnt = 0
num = '1'
while cnt < K:
    for i in range(len(num) - 1):
        if not int(num[i]) <= int(num[i + 1]):
            num += 1
            break
    cnt += 1
    num += 1

print(num)
