N = int(input())
A = int(input())

rest = N % 500
if rest <= A:
    print('Yes')
else:
    print('No')