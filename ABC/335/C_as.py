n, q = map(int, input().split())

head = (1, 0)
move_count = 0

for _ in range(q):
    query = input().split()
    query_type = int(query[0])

    if query_type == 1:
        direction = query[1]
        dx, dy = 0, 0
        if direction == 'R':
            dx = 1
        elif direction == 'L':
            dx = -1
        elif direction == 'U':
            dy = 1
        elif direction == 'D':
            dy = -1

        head_x, head_y = head
        head = (head_x + dx, head_y + dy)
        move_count += 1

    elif query_type == 2:
        part = int(query[1])
        if part <= move_count:
            part_x, part_y = head
            for _ in range(min(move_count, part - 1)):
                part_x -= dx
                part_y -= dy
            print(part_x, part_y)
        else:
            print(part - move_count, 0)
