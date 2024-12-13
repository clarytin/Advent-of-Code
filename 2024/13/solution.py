import re
import numpy as np
from math import isclose


def main():
    machines = getMachines()
    tokens1, tokens2 = 0, 0
    for machine in machines:

        tokens1 += countTokens(machine)
        machine[2][0] += 10000000000000
        machine[2][1] += 10000000000000
        tokens2 += countTokens(machine)

    print(tokens1)
    print(tokens2)
   

def countTokens(machine):
    aX, aY = machine[0]
    bX, bY = machine[1]
    prizeX = machine[2][0]
    prizeY = machine[2][1]

    A = np.array([[aX, bX], [aY, bY]])
    B = np.array([prizeX, prizeY])

    aTokens, bTokens = np.linalg.solve(A, B)

    if isclose(abs(aTokens - round(aTokens)), 0, abs_tol=1e-4):
        if isclose(abs(bTokens - round(bTokens)), 0, abs_tol=1e-4):
            return (round(aTokens) * 3) + round(bTokens)
    
    return 0


def getMachines():
    f = open("input.txt", "r")

    buttonPat = re.compile("X\+([0-9]+), Y\+([0-9]+)")
    prizePat = re.compile("X\=([0-9]+), Y\=([0-9]+)")

    machines, curr = [], []
    count = 0

    for line in f.readlines():
        if count < 2:
            m = re.search(buttonPat, line)
            curr.append((int(m.group(1)), int(m.group(2))))

        elif count == 2:
            m = re.search(prizePat, line)
            curr.append([int(m.group(1)), int(m.group(2))])
            machines.append(curr)
            curr = []

        count = (count + 1) % 4

    return machines


if __name__ == "__main__":
    main()