N = int(input())
S = [input() for i in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        T = S[i] + S[j]
        if T == T[::-1]:
            print('Yes')
            exit()          
print('No')
              
# hyouchunのqiitaを参考にした      
# i == jの時は必ず回文になるためskipしたい
# continueでi == jの時skipできる
# 文字列の反転はT[::-1]とかける
# 9行目で回文かcheckしている(覚える)
# 早くACしてる人の回答はこれが多いからこれ覚えたほうがいいかも