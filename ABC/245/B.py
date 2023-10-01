N = int(input())
A = list(map(int, input().split()))

for i in range(2001):
    if i not in A:
        print(i)
        exit()

# 5行目の書き方注意
# Aiの範囲は2000まで
