import re
from math import isclose


def main():
    machines = getMachines()
    tokens1, tokens2 = 0, 0
    for machine in machines:

        tokens1 += countTokens(machine)
        machine[2][0] += 10000000000000
        machine[2][1] += 10000000000000
        tokens2 += countTokens(machine)

    print(int(tokens1))
    print(int(tokens2))
   

def countTokens(machine):
    aX, aY = machine[0]
    bX, bY = machine[1]
    prizeX = machine[2][0]
    prizeY = machine[2][1]

    # Get determinant and check if invertible
    det = ((aX * bY) - (aY * bX))

    # A = | aX, aY |   X = | a |    B = | prizeX | 
    #     | bX, bY |       | b |        | prizeY |      
    
    # A * X = B
    # X = A^-1 * B
    # A^-1 = 1/determinant * | bY, -aY |
    #                        | -bX, aX | 
    if det != 0: 
        a = (1 / det) * ((bY * prizeX) + (-bX * prizeY))
        b = (1 / det) * ((-aY * prizeX) + (aX * prizeY))
        if isclose(a - round(a), 0, abs_tol=1e-4):
            if isclose(b - round(b), 0, abs_tol=1e-4):
                return (a * 3) + b
            
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