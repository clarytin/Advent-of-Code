def main():
    coords = getInput()
    path, score = bfs(coords[:1024], 70, 70)
    print(score)

    for i in range(1024, len(coords)):
        if coords[i] in path:
            path, score = bfs(coords[:i+1], 70, 70)

            if score == -1:
                print(str(coords[i][0]) + "," + str(coords[i][1]))
                break


def bfs(coords, endX, endY):
    dirs = [(-1,0), (0, 1), (1, 0), (0, -1)]
    visited = set()
    q = [(0, 0, 0, set())]

    while q:
        x, y, score, path = q.pop(0)
        if (x == endX) and (y == endY):
            return path, score
        if (x < 0) or (y < 0) or (x > endX) or (y > endY):
            continue
        if (x, y) in visited or (x, y) in coords:
            continue

        visited.add((x, y))
        for addX, addY in dirs:
            q.append((x + addX, y + addY, score + 1, path | {(x, y)}))

    return [], -1



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