def main():
    A, B, C, program = getInput()
    print(part1(A, B, C, program))
    print(part2(B, C, program))

    '''
    B = A % 8
    B = B ^ 1
    C = A // (2 ** B)
    B = B ^ 5
    B = B ^ C
    A = A // 8
    output += B % 8
    go back to start
    '''


def part2(B, C, program):
    A = 0
    for i in range(1, len(program) + 1):
        newA = A << 3
        programSlice = ",".join(map(str, program[-i:]))

        while part1(newA, B, C, program) != programSlice:
            newA += 1

        A = newA
    return A


def part1(A, B, C, program):
    output = ""

    i = 0
    while i < len(program):
        if program[i+1] > 3:
            combo = [A, B, C][program[i+1] - 4]
        else:
            combo = program[i+1]

        match program[i]:
            case 0:
                A = A // (2 ** combo)
            case 1:
                B = B ^ program[i+1]
            case 2:
                B = combo % 8
            case 3:
                if A != 0: i = program[i+1] - 2
            case 4:
                B = B ^ C
            case 5:
                output += str(combo % 8)
                output += ","
            case 6:
                B = A // (2 ** combo)
            case 7:
                C = A // (2 ** combo)
        i += 2

    if output: output = output[:-1]
    return output
 

def getInput():
    f = open("input.txt", "r")

    A = int(f.readline().split(" ")[2])
    B = int(f.readline().split(" ")[2])
    C = int(f.readline().split(" ")[2])

    f.readline()

    program = f.readline().split(" ")[1].strip()
    program = [int(i) for i in program.split(",")]

    f.close()
    return A, B, C, program


if __name__ == "__main__":
    main()