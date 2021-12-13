import copy


def day13():
    with open('input', 'r') as f:
        lines = [x.strip() for x in f.readlines()]
    dots, instructions = get_dots_and_instructions(lines)

    width = 0
    height = 0

    for idx, inst in enumerate(instructions):
        dots = fold(dots, inst)
        if idx == 0:
            print("Part 1: " + str(len(dots.keys())))

        axis = int(inst.split(' ')[-1].split('=')[-1])
        # last folds for x/y give the max width/height respectively
        if 'x' in inst:
            width = axis
        if 'y' in inst:
            height = axis

    print("Part 2:" + get_bold_print(dots, height, width))


def get_dots_and_instructions(lines):
    dots = {}
    instructions = []
    for line in lines:
        if ',' in line:
            x, y = line.split(',')
            dots[(int(x), int(y))] = True
        if 'fold' in line:
            instructions.append(line)
    return dots, instructions


def fold(dots, instruction):
    direction = instruction.split(' ')[-1].split('=')[0]
    axis = int(instruction.split('=')[1])
    new_dots = copy.deepcopy(dots)
    for dot in dots.keys():
        if direction == 'x':
            if dot[0] < axis:
                continue
            new_x = axis - (dot[0] - axis)
            new_dot = (new_x, dot[1])
            new_dots.pop(dot)
            new_dots[new_dot] = True
        if direction == 'y':
            if dot[1] < axis:
                continue
            new_y = axis - (dot[1] - axis)
            new_dot = (dot[0], new_y)
            new_dots.pop(dot)
            new_dots[new_dot] = True

    return new_dots


def get_bold_print(dots, height, width):
    serial = ''
    for y in range(height):
        line = '--'
        for x in range(width):
            line = line + ('##' if (x, y) in dots else '--')
        serial = serial + '\n' + line
    return serial


if __name__ == '__main__':
    day13()
