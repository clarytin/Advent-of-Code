import numpy as np
import re

def main():
    part3()
    part4()

def part4():
    A = getArray()

    count = 0
    for row in range(1, len(A) - 1):
        for col in range(1, len(A[0]) - 1):
            if A[row][col] == "A":
                count += checkMas(A, row, col)
        
    print(count)
                
def checkMas(A, row, col):
    tl = A[row-1][col-1]
    tr = A[row-1][col+1]
    bl = A[row+1][col-1]
    br = A[row+1][col+1]
    if (tl == "M" and br == "S") or (tl == "S" and br == "M"):
        if (tr == "M" and bl == "S") or (tr == "S" and bl == "M"):
            return 1
        
    return 0

def part3():
    A = np.array(getArray())

    count = 0

    # Rows
    for i in range(len(A)):
        count += countXmas(A[i, :])
    # Cols
    for i in range(len(A[0])):
        count += countXmas(A[:, i])

    # Get both Top left-bottom right and TR-BL diagonals
    arrays = [A, np.fliplr(A)]
    for array in arrays:
        # Diagonals to left of main diagonal
        for i in range(len(array[0])):
            count += countXmas(np.diagonal(array, i))
        # Diagonals to right of main diagonal
        for i in range(1, len(array)):
            count += countXmas(np.diagonal(array, -i))

    print(count)

def getArray():
    f = open("input.txt", "r")

    A = []
    for line in f.readlines():
        row = []
        for ch in line:
            row.append(ch)
        row.pop()
        A.append(row)

    return A

def countXmas(line):
    string = "".join(line)
    count = 0
    xmas = [i for i in re.finditer("XMAS", string)]
    count += len(xmas)
    samx = [i for i in re.finditer("SAMX", string)]
    count += len(samx)
    return count

if __name__ == "__main__":
    main()