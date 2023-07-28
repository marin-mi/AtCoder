K = int(input())

if K >= 60:
    HH = '22'
    MM = str(K - 60)
else:
    HH = '21'  
    MM = str(K)
    
if len(MM) == 1:
    MM = '0' + MM

print(f'{HH}:{MM}')