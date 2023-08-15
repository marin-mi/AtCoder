A, B = map(int, input().split())

S = B / A

print(f'{S:.3f}')

# fstringによって出力する桁数指定ができる
# 小数点以下3桁にできる
# 四捨五入する問題が出ない理由