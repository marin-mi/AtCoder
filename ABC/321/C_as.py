def generate_321_like_numbers():
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while True:
        if not numbers:
            break
        num = numbers.pop(0)
        yield int(num)
        last_digit = int(num[-1])
        for i in range(last_digit):
            numbers.append(num + str(i))


def find_kth_321_like_number(K):
    gen = generate_321_like_numbers()
    for _ in range(K - 1):
        next(gen)
    return next(gen)


K = int(input())

print(find_kth_321_like_number(K))
