A, B = map(int, input().split())

cal = str(B / A)

if int(cal[6]) < 5:
    print(cal[:5])
else:
    cal[5] + 1
    print(cal[:5])