S = input()

flag = True

if not (S[0].isupper() and S[-1].isupper()):
    flag = False

if not (S[1:-1].isdigit() and 100000 <= int(S[1:-1]) <= 999999):
    flag = False
    
if flag:
    print("Yes")
else:
    print("No")