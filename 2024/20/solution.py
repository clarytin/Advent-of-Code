def main():
    maze = getInput()
    r, c = getPosition(maze)
    times, path = bfs(maze, r, c)
  
    shortcuts = getShortcuts(maze, times, path)
    count = 0
    for sh in shortcuts:
        if sh >= 100:
            count += 1
        else:
            break
    print(count)


def getPosition(maze):
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == "S":
                return r, c


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
        for dr, dc, in dirs:
             q.append((r + dr, c + dc, time + 1, path + [(r + dr, c + dc)]))        
          

def getShortcuts(maze, times, path):
    dirs = [(-1,0), (0, 1), (1, 0), (0, -1)]
    pathSet = set(path)
    shortcuts = []
    for (r, c) in path:
        for (dr, dc) in dirs:
            newR, newC = r + dr, c + dc
            if (newR, newC) in pathSet:
                continue
            if maze[newR][newC] == ".":
                continue
            
            newR, newC = newR + dr, newC + dc
            if newR < 0 or newC < 0 or newR == len(maze) or newC == len(maze[0]):
                continue
            if maze[newR][newC] == ".":
                shortcuts.append(times[newR][newC] - times[r][c] - 2)

    return sorted(shortcuts, reverse = True)



def getInput():
    f= open("input.txt", "r")

    maze = []
    for line in f.readlines():
        maze.append([i for i in line.strip()])

    f.close()
    return maze


if __name__ == "__main__":
    main()