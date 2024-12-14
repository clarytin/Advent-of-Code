import re


def main():
    quads = [0, 0, 0, 0, 0]
    robots = getRobots()
    xs, ys = 101, 103

    for robot in robots:
        x, y, i = getPosition(xs, ys, 100, robot)
        quads[i] += 1

    print(quads[1] * quads[2] * quads[3] * quads[4])


def getPosition(xs, ys, seconds, robot):
    x, y, vx, vy = robot
    midx = xs // 2
    midy = ys // 2

    x = (x + (seconds * vx)) % xs
    y = (y + (seconds * vy)) % ys

    if x < midx and y < midy: return x, y, 1
    if x < midx and y > midy: return x, y, 2
    if x > midx and y < midy: return x, y, 3
    if x > midx and y > midy: return x, y, 4

    return x, y, 0


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