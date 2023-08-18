p, q = input().split()

mydict = {'A':0, 'B':3, 'C':4, 'D':8, 'E':9, 'F':14, 'G':23}

ans = abs(mydict[p] - mydict[q])

print(ans)

# 原点をAとする
# Aとの差をそれぞれ辞書に並べる
# drop310さんを参考にした