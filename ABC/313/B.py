N, M = map(int, input().split())
S = set(range(1, N + 1))

for i in range(M):
    win, lose = map(int, input().split())
    S.discard(lose)

if len(S) != 1:
    print(-1)
else:
    print(*S)

# 競プロフレンズの解説参考にした
# loseに立てきていない人が最強と考える
# 人数分のsetを作る
# loserはsetから削除する、removeでも可
# 11行目でprint(S)すると{1}となってしまうためprint(S.pop())とする
# 11行目はprint(*S)でも可
# popはsetだと順序がないためランダムに削除される
# popはリストと辞書だと最後の要素が削除される
