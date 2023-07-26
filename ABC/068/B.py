N = int(input())

cnt = 0
ans = 0

nums = list(range(1, N + 1))

for num in nums:
    tmp_cnt = 0
    tmp_num = num
    while True:
        if num % 2 == 0:
            num = num // 2
            tmp_cnt += 1
        else:
            break 
        
    if cnt < tmp_cnt:
        cnt = tmp_cnt 
        ans = tmp_num 

print(ans)        