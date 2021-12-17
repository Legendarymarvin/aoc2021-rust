import time


def do_step(point, velocity):
    x, y = point
    x = x + velocity[0]
    y = y + velocity[1]
    new_height = point[1] + velocity[1]
    return (x, y), new_height


def adjust(velocity):
    y = velocity[1] - 1
    if velocity[0] > 0:
        return velocity[0] - 1, y
    elif velocity[0] == 0:
        return velocity[0], y
    else:
        return velocity[0] + 1, y


def day17():
    start_time = time.time()
    with open('input', 'r') as f:
        target = [x.strip() for x in f.readlines()][0]

    target = target.replace("target area: x=", "").replace("y=", "")
    x_min, x_max = [int(x) for x in target.split(', ')[0].split('..')]
    y_min, y_max = [int(x) for x in target.split(', ')[1].split('..')]
    print(x_min, x_max, y_min, y_max)

    start = (0, 0)
    correct = []
    max_heights = []
    for i in range(1000, 0, -1):
        for j in range(1000, -1000, -1):
            velocity = (i, j)
            still_on_route = True
            point = start
            max_height = 0
            while still_on_route:
                point, height = do_step(point, velocity)
                max_height = max(height, max_height)
                velocity = adjust(velocity)
                if x_min <= point[0] <= x_max and y_min <= point[1] <= y_max:
                    correct.append((i, j))
                    max_heights.append(max_height)
                    still_on_route = False
                if point[0] > x_max + 10 or point[1] < y_min:
                    still_on_route = False

    print(max(max_heights))
    print(len(correct))
    end = time.time() - start_time
    print("And it only took like ... " + str(end) + " seconds ... ")
    # I know there is a nice mathematical way of implementing this, probably using parabolas, might implement later


if __name__ == '__main__':
    day17()
