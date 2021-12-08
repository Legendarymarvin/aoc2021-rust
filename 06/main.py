import collections


def day06():
    with open('input', 'r') as f:
        fish = dict(collections.Counter([int(x.strip()) for x in f.readlines()[0].split(',')]))

    for c in range(1, 257):
        after_today = {}
        new_parents = fish[0] if 0 in fish.keys() else 0

        for key in list(range(1, 9)):
            if key != 0 and key in fish.keys():
                after_today[key - 1] = fish[key]

        if new_parents > 0:
            after_today[8] = new_parents
            after_today[6] = new_parents + (after_today[6] if 6 in after_today.keys() else 0)

        fish = after_today
        if c == 80:
            print("part1: " + str(sum(fish.values())))

    print("part2: " + str(sum(fish.values())))


if __name__ == '__main__':
    day06()
