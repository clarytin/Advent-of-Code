def main():
    maze = getInput()
    r, c = getPosition(maze)
    times, path = bfs(maze, r, c)
  
    print(getShortcuts(maze, times, path, 2))
    print(getShortcuts(maze, times, path, 20))


def getShortcuts(maze, times, path, length):
    steps = set()
    for dR in range(length + 1):
        for dC in range(length + 1 - dR):
            for mR, mC in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                steps.add((dR * mR, dC * mC))

    shortcuts = []
    for r, c in path:
        for sR, sC in steps:
            nR, nC = r + sR, c + sC
            if nR < 0 or nC < 0 or nR >= len(maze) or nC >= len(maze[0]):
                continue

            if maze[nR][nC] != "#":
                length = times[nR][nC] - (times[r][c] + abs(sR) + abs(sC))
                shortcuts.append(length)

    return len([i for i in shortcuts if i >= 100])


def bfs(maze, r, c):
    dirs = [(-1,0), (0, 1), (1, 0), (0, -1)]
    times = [([None] * len(maze[0])) for _ in maze]
   
    visited = set()
    q = [(r, c, 0, [(r, c)])]

    while q:
        r, c, time, path = q.pop(0)
        if (r, c) in visited:
            continue
        if maze[r][c] == "#":
            continue

        times[r][c] = time
        if maze[r][c] == "E":
            return times, path
        
        visited.add((r, c))        
        for dR, dC, in dirs:
             nR, nC = r + dR, c + dC
             q.append((nR, nC, time + 1, path + [(nR, nC)]))        
      
      
def getPosition(maze):
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == "S":
                return r, c
    

def getInput():
    f= open("input.txt", "r")

    maze = []
    for line in f.readlines():
        maze.append(line.strip())

    f.close()
    return maze


if __name__ == "__main__":
    main()