import re


def main():
    robots = getRobots()
    xs, ys = 101, 103

    print(part1(xs, ys, robots))
    print(part2(xs, ys, robots))


def part1(xs, ys, robots):
    quads = [0, 0, 0, 0]
    midx = xs // 2
    midy = ys // 2

    for robot in robots:
        x, y = getPosition(xs, ys, 100, robot)
        
        if x < midx and y < midy: quads[0] += 1
        if x < midx and y > midy: quads[1] += 1
        if x > midx and y < midy: quads[2] += 1
        if x > midx and y > midy: quads[3] += 1

    return(quads[0] * quads[1] * quads[2] * quads[3])


def part2(xs, ys, robots):
    for seconds in range(xs * ys):
        locs, visited = set(), set()

        for robot in robots:
            locs.add(getPosition(xs, ys, seconds, robot))

        for x, y in locs:
            if bfs(x, y, locs, visited) > 15:
                return seconds


def bfs(x, y, locs, visited):
    connected = 0
    q = [(x, y)]

    while q:
        x, y = q.pop()
        if (x, y) in visited:
            continue

        connected += 1
        visited.add((x, y))

        if (x+1, y) in locs: q.append((x+1, y))
        if (x-1, y) in locs: q.append((x-1, y))
        if (x, y+1) in locs: q.append((x, y+1))
        if (x, y-1) in locs: q.append((x, y-1))

    return connected


def getPosition(xs, ys, seconds, robot):
    x, y, vx, vy = robot

    x = (x + (seconds * vx)) % xs
    y = (y + (seconds * vy)) % ys

    return x, y


def getRobots():
    numPat = "(-?[0-9]+)"
    coords = numPat + "," + numPat
    pattern = re.compile("p=" + coords + " v=" + coords )

    robots = []
    f = open("input.txt", "r")
    for line in f.readlines():
        m = re.match(pattern, line)
        robots.append((int(m.group(1)), int(m.group(2)), \
                       int(m.group(3)), int(m.group(4))))

    f.close()
    return robots


if __name__ == "__main__":
    main()