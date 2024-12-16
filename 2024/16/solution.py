def main():
    maze = getInput()
    minimum, bestSeats = bfs(maze, len(maze) - 2, 1, 1)
    print(minimum)
    print(len(bestSeats))


def bfs(maze, r, c, d):
    ds = [(-1,0), (0, 1), (1, 0), (0, -1)]
    minimum = float("inf")
    best = set()
    visited = {}
    q = [(r, c, d, 0, set())]

    while q:
        r, c, d, score, seats = q.pop(0) 
        seats.add((r, c))

        if maze[r][c] == '#':
            continue
        if maze[r][c] == 'E':
            if score < minimum:
                best, minimum = seats, score
            elif score == minimum:
                best |= seats
            continue
        if (r, c, d) in visited and visited[(r, c, d)] < score:
            continue

        visited[(r, c, d)] = score
        q.append((r + ds[d][0], c + ds[d][1], d, score + 1, seats.copy()))
        d1 = (d - 1) % 4
        q.append((r + ds[d1][0], c + ds[d1][1], d1, score + 1001, seats.copy()))
        d2 = (d + 1) % 4
        q.append((r + ds[d2][0], c + ds[d2][1], d2, score + 1001, seats.copy()))

    return minimum, best


def getInput():
    f= open("input.txt", "r")

    maze = []
    for line in f.readlines():
        maze.append([i for i in line.strip()])

    f.close()
    return maze


if __name__ == "__main__":
    main()