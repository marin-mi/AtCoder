N = int(input())
S = [input() for _ in range(N)]

win = []
for i in range(N):
    cnt = S[i].count('o')
    win.append((cnt, -i))

win.sort(reverse=True)

ans = []
for pair in win:
    ans.append(-pair[1] + 1)

print(*ans)

# hyouriと公式解説2番目の方針を参考
# タプルにしてリストに追加していく
# 7行目の2つ目の要素がマイナスな理由は、買った試合数が同じ時プレイヤーの番号が小さい方が順位が上とするため
# 0indexなので13行目で+1する
