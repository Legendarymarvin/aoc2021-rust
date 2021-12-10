from statistics import median
closer_scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
completion_scores = {")": 1, "]": 2, "}": 3, ">": 4}
openings = ["(", "[", "{", "<"]
closings = [")", "]", "}", ">"]
closing_for_open = {"(": ")", "{": "}", "[": "]", "<": ">"}
opening_for_closed = {")": "(", "}": "{", "]": "[", ">": "<"}


def day10():
    with open('input', 'r') as f:
        lines = [x.strip() for x in f.readlines()]
    invalids = []
    invalid_lines = []
    incomplete_closers = []

    for line in lines:
        open_brackets = {}
        corrupt = False
        for idx, char in enumerate(line):
            if corrupt:
                break
            if char in openings:
                open_brackets[idx] = True
            else:
                closed = False
                for i in range(idx, -1, -1):
                    if corrupt or closed:
                        break
                    if i in open_brackets.keys() and open_brackets[i]:
                        if line[i] == opening_for_closed[char]:
                            open_brackets[i] = False
                            closed = True
                        else:
                            invalid_lines.append(idx)
                            invalids.append(char)
                            corrupt = True

        # part2
        if not corrupt:
            closers = []
            open_idx = [x for x in open_brackets.keys() if open_brackets[x]]
            open_idx.reverse()
            for idx in open_idx:
                closers.append(closing_for_open[line[idx]])
            incomplete_closers.append(closers)

    # part1
    print(sum([closer_scores[x] for x in invalids]))

    # part2
    scores = []
    for res in incomplete_closers:
        score = 0
        for char in res:
            score = score * 5
            score = score + completion_scores[char]
        scores.append(score)
    print(median(scores))


def day10_better():
    with open('input', 'r') as f:
        lines = [x.strip() for x in f.readlines()]

    parsed_lines = []

    for line in lines:
        not_done = True
        new_line = line
        while not_done:
            # basically recursion
            before = new_line
            new_line = new_line.replace("()", "").replace("{}", "").replace("[]", "").replace("<>", "")
            if len(new_line) == len(before):
                not_done = False
        parsed_lines.append(new_line)

    invalid = []
    invalid_idx = []
    for idx, line in enumerate(parsed_lines):
        if line in invalid:
            break
        for char in closings:
            if char in line and line not in invalid:
                invalid.append(line)
                invalid_idx.append(idx)

    result = 0
    for line in invalid:
        result = result + closer_scores[[c for c in line if c in closings][0]]
    print(result)

    scores = []
    for idx, line in enumerate(parsed_lines):
        if idx in invalid_idx:
            continue
        score = 0
        for char in reversed(list(line)):
            score = score * 5
            score = score + completion_scores[closing_for_open[char]]
        scores.append(score)
    print(median(scores))





if __name__ == '__main__':
    day10()
    day10_better()
