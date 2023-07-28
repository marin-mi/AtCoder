s = list(input())
t = list(input())

s.sort()
t.sort(reverse = True)
S = ''.join(s)
T = ''.join(t)
if S < T:
    print('Yes')
else:
    print('No')
    
#join関数は書かなくてもいい