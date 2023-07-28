N = int(input())
S = input()

flag_A = False
flag_B = False
flag_C = False

for i in range(len(S)):
    if S[i] == 'A':
        flag_A = True
    elif S[i] == 'B':
        flag_B = True
    elif S[i] == 'C':
        flag_C = True
    if flag_A and flag_B and flag_C:
        print(i + 1)
        break