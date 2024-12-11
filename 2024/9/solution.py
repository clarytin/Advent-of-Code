def main(): 
    line, dm = getDiskmap()
    #dm = compress(dm)
    dm = compress2(line, dm)
    hashSum = getHashSum(dm)

    print(hashSum)


def getHashSum(dm):
    hashSum = 0
    i = 0
    while i < len(dm):
        if dm[i] is not None:
            hashSum += (dm[i] * i)
        i += 1
    return hashSum


def compress2(line, dm):
    free = getBlocks(line, False)
    taken = getBlocks(line, True)

    for block in taken[::-1]:
        num = block[0]
        size = block[1]
        index = block[2]
        i = 0

        while free[i][2] < index:
            fSize = free[i][1]
            fIndex = free[i][2]

            if size <= fSize:
                for j in range(size):
                    dm[fIndex + j] = num
                    dm[index + j] = None
                if size < fSize:
                    free.insert(i+1, (0, fSize - size, fIndex + size))
                free.pop(i)
                break
            i += 1

    return dm


def getBlocks(line, taken):
    blocks = []
    index = 0
    blockNum = 0
    for ch in line[:-1]:
        if taken:
            blocks.append((blockNum, int(ch), index))
            blockNum += 1
        index += int(ch)
        taken = not taken
    return blocks


def compress(dm):
    i = dm.index(None)

    while i < len(dm):
        if dm[-1] is not None:
            dm[i] = dm[-1]
            while dm[i] is not None and i < len(dm):
                i += 1
        dm.pop()
    return dm[:i]

    
def getDiskmap():
    dm = []
    free = False
    index = 0
    f = open("input.txt", "r")
    line = f.read()
    for ch in line[:-1]:
        for _ in range(int(ch)):
            dm.append(None if free else index)
        if not free:
            index += 1
        free = not free
    f.close()
    return line, dm
    

if __name__ == "__main__":
    main()