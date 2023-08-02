N = int(input())

up = N
down = N
if N % 5 == 0:
    print(N)
else:
    for i in range(4):
        up += 1
        down -= 1
        if up % 5 == 0:
            print(up)
            break
        elif down % 5 == 0:
            print(down)
            break