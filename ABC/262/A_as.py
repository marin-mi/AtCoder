Y = int(input())

for i in range(4):
    if (Y + i) % 4 == 2:
        print(Y + i)
        break

# 4年周期で4で割った余りが2になるため、rangeの中は4になる
# Nakubaruさんのを参考にした