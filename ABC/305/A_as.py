#計算がメインの解法

N = int(input())

#5で割った値の小数第一位を四捨五入し、5倍している
#5で割った値に最も近い整数を求めている
ans = round(N / 5) * 5

print(ans)