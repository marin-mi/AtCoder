a, b = map(int, input().split())

z = (a ** 2 + b ** 2) ** 0.5

x = a / z
y = b / z

print(x, y)

# 三平方の定理からzを求める
# 累乗根より、ルートは1/2乗
# 比からx,yを求める
