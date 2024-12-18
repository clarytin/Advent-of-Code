def main():
    coords = getInput()
    print(bfs(coords[:1024], 70, 70))

    lo, hi = 1024, len(coords)
    while lo != hi:
        mid = (lo + hi) // 2
        if bfs(coords[:mid + 1], 70, 70) == -1:
            hi = mid
        else:
            lo = mid + 1

    print(str(coords[lo][0]) + "," + str(coords[lo][1]))


def bfs(coords, endX, endY):
    dirs = [(-1,0), (0, 1), (1, 0), (0, -1)]
    visited = set()
    q = [(0, 0, 0)]

    while q:
        x, y, score = q.pop(0)
        if (x == endX) and (y == endY):
            return score
        if (x < 0) or (y < 0) or (x > endX) or (y > endY):
            continue
        if (x, y) in visited or (x, y) in coords:
            continue

        visited.add((x, y))
        for addX, addY in dirs:
            q.append((x + addX, y + addY, score + 1))

    return -1


def getInput():
    f= open("input.txt", "r")

    coords = []
    for line in f.readlines():
        coord = line.strip().split(",")
        coords.append((int(coord[0]), int(coord[1])))

    f.close()
    return coords


if __name__ == "__main__":
    main()