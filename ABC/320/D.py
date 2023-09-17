N, M = map(int, input().split())

coordinates = [(None, None) for _ in range(N)]
coordinates[0] = (0, 0)

for _ in range(M):
    A, B, X, Y = map(int, input().split())
    A -= 1
    B -= 1
    if coordinates[A] != (None, None):
        x, y = coordinates[A]
        coordinates[B] = (x + X, y + Y)
    elif coordinates[B] != (None, None):
        x, y = coordinates[B]
        coordinates[A] = (x - X, y - Y)

for x, y in coordinates:
    if x is None or y is None:
        print("undecidable")
    else:
        print(x, y)
