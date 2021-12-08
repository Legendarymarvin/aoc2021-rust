def get_result(param, marks, lot):
    sum1 = 0
    for i, line in enumerate(param):
        for j, column in enumerate(line):
            if (i, j) not in marks:
                sum1 = sum1 + int(param[i][j])
    return sum1 * int(lot)


def day04():
    with open('input', 'r') as f:
        lines = f.readlines()
    input = lines[0]
    lines = lines[1:]

    boards = []
    for t in ''.join(lines).split('\n\n'):
        boardlines = t.split('\n')
        current_board = []
        for line in boardlines:
            b = line.split()
            if b:
                current_board.append(b)
        boards.append(current_board)

    marked = {}
    for i, _ in enumerate(boards):
        marked[i] = []

    done = False
    won = []
    for lot in input.split(','):
        for i, board in enumerate(boards):
            if i in won:
                continue
            for j, line in enumerate(board):
                for k, column in enumerate(line):
                    if boards[i][j][k] == lot:
                        marked[i].append((j, k))

            marks = marked[i]
            for r in range(5):
                c1 = sum(map(lambda x: x[0] == r, marks))
                c2 = sum(map(lambda x: x[1] == r, marks))
                if c1 == 5 or c2 == 5:
                    print(i, get_result(boards[i], marks, lot))
                    done = True
                    won.append(i)
                    break


if __name__ == '__main__':
    day04()
