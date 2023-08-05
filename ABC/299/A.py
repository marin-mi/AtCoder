n = int(input())
s = input()

a = s.index('|')
b = s.index('*')
c = s.rindex('|')

if a < b < c:
    print('in')
else:
    print('out')
    
# indexの使い方
# rindexは一番最後を返す