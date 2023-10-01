S = input()

if S.isupper() or S.islower() or len(set(S)) != len(list(S)):
    print('No')
else:
    print('Yes')

# hirai33のコードを参考にした
# isupperは全部大文字だったらTrueを返す
# islowerは全部小文字だったらTrueを返す
# 3つ目の条件はsetにした時とlistにしたときの長さを比較している
