from itertools import groupby


def day08():
    with open('input', 'r') as f:
        lines = f.readlines()

    part1(lines)
    part2(lines)


def part2(lines):
    result = 0
    for line in lines:
        codes = {}
        values = line.replace(' | ', ' ').split(' ')

        get_obvious_digits(codes, values)
        get_six_line_digits(codes, values)
        get_five_line_digits(codes, values)

        output = line.split(' | ')[1]
        number = ''
        for digit in output.strip().split(' '):
            for key in codes.keys():
                if len([x for x in codes[key] if x not in list(digit)]) == 0 and len(
                        [x for x in list(digit) if x not in codes[key]]) == 0:
                    number = number + key
        result = result + int(number)
    print(result)


def get_five_line_digits(codes, values):
    for v in values:
        v = list(v.strip())
        if len(v) != 5:
            continue
        if len([x for x in v if x in codes["1"]]) == len(codes["1"]):
            # contains 1 => 3
            codes["3"] = v
        elif len([x for x in v if x in codes["9"]]) == len(v):
            # is completely in 9 => 5
            codes["5"] = v
        else:
            # two remaining
            codes["2"] = v


def get_six_line_digits(codes, values):
    for v in values:
        v = list(v.strip())
        if len(v) != 6:
            continue
        # not containing 1 => 6
        if len([x for x in v if x in codes["1"]]) != len(codes["1"]):
            codes["6"] = v
        elif len([x for x in v if x in codes["4"]]) != len(codes["4"]):
            # not 6 and not containing the four lines => 0
            codes["0"] = v
        else:
            # only remaining
            codes["9"] = v


def get_obvious_digits(codes, values):
    # get the obvious ones
    for v in values:
        v = list(v.strip())
        if len(v) == 2:
            codes["1"] = v
        if len(v) == 3:
            codes["7"] = v
        if len(v) == 4:
            codes["4"] = v
        if len(v) == 7:
            codes["8"] = v


def part1(lines):
    counts = {}
    for line in lines:
        line = line.split(' | ')[1]
        for seq in line.split(' '):
            seq = seq.strip()
            if seq != '':
                if len(seq) in counts.keys():
                    counts[len(seq)] = counts[len(seq)] + 1
                else:
                    counts[len(seq)] = 1
    print(counts[2] + counts[4] + counts[7] + counts[3])


if __name__ == '__main__':
    day08()
