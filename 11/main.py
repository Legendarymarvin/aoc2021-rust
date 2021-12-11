def day11():
    moves = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if not (i == 0 and j == 0):
                moves.append((i, j))

    with open('input', 'r') as f:
        matrix = [[int(y) for y in list(x.strip())] for x in f.readlines()]

    steps_to_do = 100
    flashed = 0
    for _ in range(1, steps_to_do + 1):
        increase_octopi(matrix)
        flashed += flash_it(matrix, moves)
    print(flashed)

    all_flashed = False
    steps = 0
    # assuming we didn't do a full flash before
    while not all_flashed:
        steps += 1
        increase_octopi(matrix)
        flashed += flash_it(matrix, moves)
        all_flashed = check_all_flashed(matrix)
    print(steps + steps_to_do)


def flash_it(matrix, moves):
    flashed = []
    new_flashes = True
    f = 0
    while new_flashes:
        f += 1
        initial = len(flashed)
        for i, _ in enumerate(matrix):
            for j, _ in enumerate(matrix[i]):
                value = matrix[i][j]
                if value > 9:
                    matrix[i][j] = 0
                    flashed.append((i, j))
                    for move in moves:
                        x = i + move[0]
                        y = j + move[1]
                        if 0 <= x < len(matrix) and 0 <= y < len(matrix[i]):
                            if (x, y) not in flashed:
                                matrix[x][y] = matrix[x][y] + 1
        new_flashes = initial != len(flashed)

    return len(flashed)


def check_all_flashed(matrix):
    for line in matrix:
        for value in line:
            if value != 0:
                return False
    return True


def increase_octopi(matrix):
    for i, _ in enumerate(matrix):
        for j, _ in enumerate(matrix[i]):
            matrix[i][j] = matrix[i][j] + 1


def enter_the_matrix(matrix):
    for line in matrix:
        print(' '.join([str(x) for x in line]))


if __name__ == '__main__':
    day11()
