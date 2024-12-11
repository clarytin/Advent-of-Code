ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def main():
    loc, row, col = getMapAndCoords()
    startRow, startCol = row, col

    posWithDir = checkLoop(loc, startRow, startCol, 0, row, col, True)
    positions = set()
    for r, c, _ in posWithDir:
        positions.add((r, c))

    count = 0
    for obsRow, obsCol in positions:
        count += checkLoop(loc, startRow, startCol, 0, obsRow, obsCol, False)

    print(len(positions))
    print(count)


def checkLoop(loc, row, col, d, obsRow, obsCol, returnPos):
    positions = set()
    positions.add((row, col, d))

    while True:
        row += ds[d][0]
        col += ds[d][1]
        
        if row < 0 or col < 0 or row >= len(loc) or col >= len(loc[0]):
            return positions if returnPos else 0
        
        if (row, col, d) in positions:
            return 1

        if loc[row][col] == "#" or (row == obsRow and col == obsCol):
            row -= ds[d][0]
            col -= ds[d][1]
            d = (d + 1) % 4
        
        positions.add((row, col, d))


def getMapAndCoords():
    f = open("input.txt", "r")

    loc = []
    row, col = 0, 0
    count = 0
    for line in f.readlines():
        for i in range(len(line)):
            if line[i] == "^":
                col = i
                row = count
        loc.append(line)
        count += 1

    return loc, row, col
  

if __name__ == "__main__":
    main()