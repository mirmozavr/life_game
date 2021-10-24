from random import randint
from copy import deepcopy

size_h = 10
size_w = 10
field = [[0] * size_w for _ in range(size_h)]


def field_print(field):
    print()
    [print(*row) for row in field]
    print()
    print("* " * (size_h * 2))
    print()


def populate(field: list, count: int):
    cells = set()
    while len(cells) < count:
        x, y = randint(0, size_h - 1), randint(0, size_w - 1)
        if (x, y) not in cells:
            cells.add((x, y))
            field[x][y] = 1


def next_generation(field: list, unlimited_field: bool = False):
    replica = deepcopy(field)
    count_neighbours = count_unlimited_field_neighbour if unlimited_field else count_limited_field_neighbour
    for i in range(size_h):
        for j in range(size_w):
            neighbours = count_neighbours(replica, i, j, size_h, size_w)
            if field[i][j] and (neighbours > 3 or neighbours < 2):
                field[i][j] = 0
                print(i, j, "Died")
            elif not field[i][j] and neighbours == 3:
                field[i][j] = 1
                print(i, j, "Born")
    if replica == field:
        print("CYCLE")
        quit()


def count_limited_field_neighbour(field: list, i: int, j: int, size_h: int, size_w: int) -> int:
    return sum([field[i + x][j + y] for x in range(-1, 2) for y in range(-1, 2) if
                (x != 0 or y != 0) and 0 <= i + x < size_h and 0 <= j + y < size_w])


def count_unlimited_field_neighbour(field: list, i: int, j: int, size_h: int, size_w: int) -> int:
    return sum([field[(i + x) % size_h][(j + y) % size_w] for x in range(-1, 2) for y in range(-1, 2) if (x != 0 or y != 0)])


def check_life(field: list):
    return any([any(row) for row in field])


populate(field, 20)
field_print(field)
while check_life(field):
    next_generation(field, unlimited_field=True)
    field_print(field)
print("All cells died ;(")
