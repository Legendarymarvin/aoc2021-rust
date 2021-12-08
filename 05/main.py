import collections

def day06():
    with open('input', 'r') as f:
        lines = f.readlines()

    hits = []
    for line in lines:
        st, fi = line.split(' -> ')
        s = st.split(',')
        f = fi.split(',')
        if s[0] == f[0]:
            y1 = int(s[1].strip())
            y2 = int(f[1].strip())
            for i in range(min(y1, y2), max(y1, y2) + 1):
                hits.append((int(s[0]), i))

        if s[1] == f[1].strip():
            x1 = int(s[0])
            x2 = int(f[0])
            for j in range(min(x1, x2), max(x1, x2) + 1):
                hits.append((j, int(s[1].strip())))

        x1 = int(s[0].strip())
        y1 = int(s[1].strip())
        x2 = int(f[0].strip())
        y2 = int(f[1].strip())
        dx = abs(x2-x1)
        dy = abs(y2-y1)

        if dx == dy:
            newHits = []
            if y1 == x1 and y2 == x2:
                for i in range(0, dx + 1):
                    if y1 < y2:
                        newHits.append((y1 + i, x1 + i))
                    else:
                        newHits.append((x2 + i, y2 + i))
            elif x1 > x2 and y1 > y2:
                for i in range(0, dx + 1):
                    newHits.append((x1 - i, y1 - i))
            elif x1 < x2 and y1 < y2:
                for i in range(0, dx + 1):
                    newHits.append((x1 + i, y1 + i))
            elif x1 < x2 and y1 > y2:
                for i in range(0, dx + 1):
                    newHits.append((x1 + i, y1 - i))
            elif x1 > x2 and y1 < y2:
                for i in range(0, dx + 1):
                    newHits.append((x1 - i, y1 + i))
            hits.extend(newHits)

    c2 = collections.Counter(collections.Counter(hits).values())
    result = 0

    for key in c2.keys():
        if int(key) > 1:
            result += int(c2[key])

    print(result)


if __name__ == '__main__':
    day06()
