N = int(input())
Pi = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'

for i in range(N + 2):
    print(Pi[i], end = '')
    
# 3.を含むために+2している
# printのデフォルトはend = '\n'
# つまり、勝手に改行されて出力される
# それを防ぐためにend = ''とすると、連結されて出力される