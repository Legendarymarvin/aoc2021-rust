import math
import time
from statistics import mean
from statistics import median


def calculate_fuel_cost_for_steps(steps):
    cost = 0
    if steps == 0:
        return cost
    elif steps == 1:
        return 1
    else:
        for i in range(1, steps + 1):
            cost = cost + i
    return cost


def day07():
    start = time.time()
    with open ('input', 'r') as f:
        positions = [int(x.strip()) for x in f.readlines()[0].split(",")]

    positions.sort()
    med = median(positions)
    fuel = 0
    for p in positions:
        fuel = fuel + abs(p-med)

    print("Part 1: " + str(int(fuel)))

    floored_median_for_some_reason = round(math.floor(mean(positions)))
    more_fuel = 0
    for p in positions:
        more_fuel = more_fuel + calculate_fuel_cost_for_steps(int(abs(p-floored_median_for_some_reason)))

    print("Part 2: " + str(int(more_fuel)))
    print("Time: " + str(time.time() - start))

    print("\n##############\n##############\n##############\nBut can you bruteforce it?\n##############\n##############\n##############\n")
    start = time.time()
    maxi = max(positions)
    fuel_costs = []

    for i in range(1, maxi + 1):
        fuel = 0
        for p in positions:
            fuel = fuel + abs(p-i)
        fuel_costs.append(fuel)
    print("Part 1: " + str(min(fuel_costs)) + " Time: " + str(time.time() - start))

    start = time.time()
    more_fuel_costs = []

    for i in range(1, maxi + 1):
        fuel = 0
        for p in positions:
            fuel = fuel + calculate_fuel_cost_for_steps(abs(p-i))
        more_fuel_costs.append(fuel)

    print("Part 2: " + str(min(more_fuel_costs)) + " Time: " + str(time.time() - start))
    print("I guess you can ...")

    print("\n##############\n##############\n##############\nBut can you bruteforce ... better?\n##############\n##############\n##############\n")

    start = time.time()
    maxi = max(positions)
    fuel_costs = []

    for i in range(1, maxi + 1):
        fuel = 0
        over = False
        for p in positions:
            fuel = fuel + abs(p-i)
            if len(fuel_costs) > 1 and fuel > min(fuel_costs):
                over = True
                break
        if over:
            break
        fuel_costs.append(fuel)
    print("Part 1: " + str(min(fuel_costs)) + " Time: " + str(time.time() - start))

    start = time.time()
    more_fuel_costs = []

    for i in range(1, maxi + 1):
        fuel = 0
        over = False
        for p in positions:
            fuel = fuel + calculate_fuel_cost_for_steps(abs(p-i))
            if len(more_fuel_costs) > 1 and fuel > min(more_fuel_costs):
                over = True
                break
        if over:
            break
        more_fuel_costs.append(fuel)
    print("Part 2: " + str(min(more_fuel_costs)) + " Time: " + str(time.time() - start))


if __name__ == '__main__':
    day07()
