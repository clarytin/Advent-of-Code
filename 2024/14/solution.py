import re


def main():
    quads = [0, 0, 0, 0, 0]
    robots = getRobots()
    for robot in robots:
        i = getPosition(101, 103, 100, robot)
        quads[i] += 1

    print(quads[1] * quads[2] * quads[3] * quads[4])


def getPosition(rows, cols, seconds, robot):
    x, y, vx, vy = robot
    midx = rows // 2
    midy = cols // 2

    for _ in range(seconds):
        x += vx
        y += vy

        if x < 0: x += rows
        if y < 0: y += cols
        if x >= rows: x -= rows
        if y >= cols: y -= cols

    if x < midx and y < midy: return 1
    if x < midx and y > midy: return 2
    if x > midx and y < midy: return 3
    if x > midx and y > midy: return 4

    return 0


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