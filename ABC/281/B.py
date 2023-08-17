S = input()

flag = True
if len(S) != 8:
    flag = False
elif S[0].isnumeric():
    flag = False
elif S[7].isnumeric():
    flag = False
elif not S[1:7].isnumeric():
    flag = False
elif not 100000 <= int(S[1:7]) <= 999999:
    flag = False

if flag:
    print('Yes')
else:
    print('No')

# リストの2~7が数値であることが確認された後にのみ、数値範囲のチェックが行われなければならない
# そうでないとRE、エラーになる
# isnumericは文字列が数字を表すか判定する
# isupperは数字が含まれていたら無視されるため、NG