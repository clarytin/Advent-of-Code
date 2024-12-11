def main(): 

    topMap = getMap()
    res1 = 0
    res2 = 0

    for i in range(len(topMap)):
        for j in range(len(topMap[i])):
            if topMap[i][j] == 0:
                nines = bfs(topMap, i, j)
                res1 += len(set(nines))
                res2 += len(nines)

    print(res1)
    print(res2)


def bfs(topMap, row, col):
    q = [(-1, row, col)]
    nines = []

    while q:
        prev, r, c = q.pop(0)
        if r < 0 or c < 0 or r >= len(topMap) or c >= len(topMap[0]):
            continue

        curr = topMap[r][c]
        if curr - prev != 1:
            continue

        if curr == 9:
            nines.append((r, c))
        else:
            q.append((curr, r+1, c))
            q.append((curr, r-1, c))
            q.append((curr, r, c+1))
            q.append((curr, r, c-1))

    return nines


def getMap():
    f = open("input.txt", "r")

    topMap = []
    for line in f.readlines():
        topMap.append([int(ch) for ch in line[:-1]])

    f.close()
    return topMap
  

if __name__ == "__main__":
    main()