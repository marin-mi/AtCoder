N = int(input())
X = list(map(int, input().split()))

X.sort()
X = X[N:-N]

ans = sum(X) / len(X)
print(ans)

# 5つ要素があって、N = 1だった場合、取り除かない要素は1~4
# 5つ要素があって、N = 2だった場合、取り除かない要素は2~3
# つまり、X[N:-N]
# removeを使う場合、for文を用いてrange(N)でそれぞれ最小と最大を取り除く
# removeではスライスは使えない