from functools import reduce
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def day08():
    matrix = enter_the_matrix()
    lows = []
    find_lows(lows, matrix)
    find_basins(lows, matrix)


def enter_the_matrix():
    with open('input', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    matrix = []
    for i, line in enumerate(lines):
        coord_line = []
        for j, char in enumerate(line):
            coord_line.append(char)
        matrix.append(coord_line)
    return matrix


# Part 1
def find_lows(lows, matrix):
    for i, line in enumerate(matrix):
        for j, char in enumerate(line):
            if is_low_point(matrix, i, j):
                lows.append((i, j))

    result = 0
    for low in lows:
        result = result + (int(matrix[low[0]][low[1]]) + 1)
    print(result)


def is_low_point(matrix, i, j):
    max_x = len(matrix) - 1
    max_y = len(matrix[0]) - 1
    value = matrix[i][j]

    for move in moves:
        hm, vm = move
        x = i + hm
        y = j + vm
        if 0 <= x <= max_x and 0 <= y <= max_y:
            comp = matrix[x][y]
            if comp <= value:
                return False

    return True


# Part 2
def find_basins(lows, matrix):
    basins_by_index = {}

    for i, coord in enumerate(lows):
        basin = measure_basin(coord, matrix)
        basins_by_index[i] = len(basin)

    sorted_sizes = sorted([x for x in basins_by_index.values()])
    biggest_basins = [int(x) for x in sorted_sizes[-3:]]
    print(reduce((lambda x, y: x*y), biggest_basins))


def measure_basin(coord, matrix):
    basin = [coord]
    while True:
        initial = len(basin)
        check_surroundings_of_basin(basin, matrix)
        if initial == len(basin):
            break
    return basin


def check_surroundings_of_basin(basin, matrix):
    max_x = len(matrix) - 1
    max_y = len(matrix[0]) - 1
    for pos in basin:
        for move in moves:
            hm, vm = move
            x = pos[0] + hm
            y = pos[1] + vm
            if 0 <= x <= max_x and 0 <= y <= max_y:
                current_pos = (x, y)
                if current_pos not in basin and matrix[x][y] != '9':
                    basin.append(current_pos)


if __name__ == '__main__':
    day08()
