n = int(input())
w = list(input().split())

common = set(w) & set(['and', 'not', 'that', 'the', 'you'])
if len(common) > 0:
    print('Yes')
else:
    print('No')
    
# 複数の要素をリストで書いてもうまくいかない
# 入力文字列のリストと問題文の5単語に共通して存在する単語の集合を、set 型での集合演算を用いて求める

# andは論理AND演算子、if文で二つの条件式がTrueの時Trueを返す
# &はビット演算子、二つのバイナリ(2進数)で同じ位置のbitが1であるものだけ1で計算する