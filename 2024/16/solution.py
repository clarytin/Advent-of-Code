def main():
    maze = getInput()
    minimum = bfs(maze, len(maze) - 2, 1, 1)
    print(minimum)


def bfs(maze, r, c, d):
    dirs = [(-1,0), (0, 1), (1, 0), (0, -1)]
    minimum = float("inf")
    visited = {}
    q = [(r, c, d, 0)]

    while q:
        r, c, d, score = q.pop(0) 
        if maze[r][c] == '#':
            continue
        if maze[r][c] == 'E':
            minimum = min(minimum, score)
            continue
        if (r, c, d) in visited:
            if visited[(r, c, d)] <= score:
                continue

        visited[(r, c, d)] = score
        q.append((r + dirs[d][0], c + dirs[d][1], d, score + 1))
        d1 = (d - 1) % 4
        q.append((r + dirs[d1][0], c + dirs[d1][1], d1, score + 1001))
        d2 = (d + 1) % 4
        q.append((r + dirs[d2][0], c + dirs[d2][1], d2, score + 1001))

    return minimum


def getInput():
    f= open("input.txt", "r")

    maze = []
    for line in f.readlines():
        maze.append([i for i in line.strip()])

    f.close()
    return maze


if __name__ == "__main__":
    main()