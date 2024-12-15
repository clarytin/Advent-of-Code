def main():
    wh, moves = getInput()
    wideWh = widen(wh)

    r, c = getRobotCoords(wh)
    for move in moves:
        r, c = moveRobot(wh, r, c, move)
    printGps(wh, "O")

    r, c = getRobotCoords(wideWh)
    for move in moves:
        if move == "<" or move == ">":
            r, c = moveRobot(wideWh, r, c, move)
        else:
            r, c = moveSpecial(wideWh, r, c, move)
    printGps(wideWh, "[")


def moveRobot(wh, r, c, m):
    moves = {"^": (-1, 0),
             "v": (1,  0),
             "<": (0, -1),
             ">": (0,  1)}
    
    nR = r + moves[m][0]
    nC = c + moves[m][1]

    if wh[nR][nC] == "#":
        return r, c
    elif wh[nR][nC] == ".":
        return move(wh, nR, nC, r, c)
    else:
        boxR, boxC = moveRobot(wh, nR, nC, m)
        if boxR == nR and boxC == nC:
            return r, c
        return move(wh, nR, nC, r, c)


def moveSpecial(wh, r, c, m):
    nR = r + (-1 if m == "^" else 1)

    if wh[nR][c] == "#":
        return r, c
    elif wh[nR][c] == ".":
        return move(wh, nR, c, r, c)
    
    left = c if wh[nR][c] == "[" else c-1
    if canMove(wh, nR, left, m):
        moveNextBox(wh, nR, left, m)
        return move(wh, nR, c, r, c)
    
    return r, c


def moveNextBox(wh, r, c, m):
    nR = r + (-1 if m == "^" else 1)
    
    if wh[nR][c] == "]":
        moveNextBox(wh, nR, c-1, m)
    if wh[nR][c] == "[":
        moveNextBox(wh, nR, c, m)
    if wh[nR][c+1] == "[":
        moveNextBox(wh, nR, c+1, m)

    move(wh, nR, c, r, c)
    move(wh, nR, c+1, r, c+1)


def canMove(wh, r, c, m):
    nR = r + (-1 if m == "^" else 1) 

    if wh[nR][c] == "#" or wh[nR][c+1] == "#":
        return False
    
    can = True
    if wh[nR][c] == "]":
        can = can and canMove(wh, nR, c-1, m)
    if wh[nR][c] == "[":
        can = can and canMove(wh, nR, c, m)
    if wh[nR][c+1] == "[":
        can = can and canMove(wh, nR, c+1, m)
        
    return can


def move(wh, nR, nC, r, c):
    wh[nR][nC] = wh[r][c]
    wh[r][c] = "."
    return nR, nC


def widen(wh):
    wides = {"#": ["#", "#"],
             "O": ["[", "]"],
             ".": [".", "."],
             "@": ["@", "."]}
    new = []
    for row in wh:
        newRow = []
        for ch in row:
            newRow += wides[ch]
        new.append(newRow)
    return new
        
        
def getRobotCoords(wh):
    for r in range(len(wh)):
        for c in range(len(wh[0])):
            if wh[r][c] == '@':
                return r, c
            
        
def printGps(wh, ch):
    gps = 0
    for r in range(len(wh)):
        for c in range(len(wh[0])):
            if wh[r][c] == ch: 
                gps += (100 * r) + c
    print(gps)


def getInput():
    f= open("input.txt", "r")
    
    border = 0
    warehouse, moves = [], []

    for line in f.readlines():
        if border < 2:
            warehouse.append([i for i in line[:-1]])
        else:
            moves += [i for i in line[:-1]]
        if line.find("#######") != -1:
            border += 1

    f.close()
    return warehouse, moves


if __name__ == "__main__":
    main()