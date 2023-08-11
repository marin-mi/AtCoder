s = input()

s = s.replace('0', 'x')
s = s.replace('1', '0')
s = s.replace('x', '1')

print(s)

# replaceを使った方法
# すべて0に変わってしまうため途中でxという仮の値に変換する