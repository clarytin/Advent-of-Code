def main():
    wh, moves = getInput()

    r, c = getRobotCoords(wh)
    for move in moves:
        r, c = moveRobot(wh, r, c, move)

    gps = 0
    for r in range(len(wh)):
        for c in range(len(wh[0])):
            if wh[r][c] == "O": 
                gps += (100 * r) + c

    print(gps)


def moveRobot(wh, r, c, m):
    def move():
        wh[nR][nC] = wh[r][c]
        wh[r][c] = "."
        return nR, nC

    moves = {"^": (-1, 0),
             "v": (1,  0),
             "<": (0, -1),
             ">": (0,  1)}
    
    nR = r + moves[m][0]
    nC = c + moves[m][1]

    if wh[nR][nC] == "#":
        return r, c
    
    elif wh[nR][nC] == ".":
        return move()
    
    else:
        boxR, boxC = moveRobot(wh, nR, nC, m)
        if boxR == nR and boxC == nC:
            return r, c
        return move()

        
def getRobotCoords(wh):
    for r in range(len(wh)):
        for c in range(len(wh[0])):
            if wh[r][c] == '@':
                return r, c

def getInput():
    f= open("input.txt", "r")
    
    border = 0
    warehouse, moves = [], []

    for line in f.readlines():
        if border < 2:
            warehouse.append([i for i in line[:-1]])
        else:
            moves += [i for i in line[:-1]]
        if line.find("########") != -1:
            border += 1

    f.close()
    return warehouse, moves


if __name__ == "__main__":
    main()