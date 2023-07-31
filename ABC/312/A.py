S = input()

flag = False
if S == 'ACE':
    flag = True
elif S == 'BDF':
    flag = True
elif S == 'CEG':
    flag = True
elif S == 'DFA':
    flag = True
elif S == 'EGB':
    flag = True
elif S == 'FAC':
    flag = True
elif S == 'GBD':
    flag = True
else:
    pass

if flag:
    print('Yes')
else:
    print('No')