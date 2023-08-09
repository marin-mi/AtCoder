n = int(input())
w = set(input().split())

if 'and' in w or 'not' in w or 'that' in w or 'the' in w or 'you' in w:
    print('Yes')
else:
    print('No')
    
# if 特定の値 in リストなど
# wは文字列でもsetでもlistでもOK

# exitでもOK

# if 'and' in w or 'not' in w or 'that' in w or 'the' in w or 'you' in w:
    #print('Yes')
    #exit()
#print('No')