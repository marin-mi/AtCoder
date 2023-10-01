A, B, C, D, E, F, X = map(int, input().split())

takahashi = 0
aoki = 0
time = 0

while time < X:
    if time % (C + A) < A:
        takahashi += B
    if time % (F + D) < D:
        aoki += E
    time += 1

if takahashi > aoki:
    print('Takahashi')
elif takahashi < aoki:
    print('Aoki')
else:
    print('Draw')

# 変数を左にする
# kskkkkを参考にした
# よくわからんので飛ばす
