import collections


def main():
    rows, cols, antennas = getAntennas()

    antinodes = set()
    for coords in antennas.values():
        antinodes |= getAntinodes(coords, rows, cols)
        
    print(len(antinodes))


def getAntinodes(coords, rows, cols):
    pairs = getPairs(coords)

    antinodes = set()
    for (r1, c1), (r2, c2) in pairs:
        rd = r1 - r2
        cd = c1 - c2

        i = 0
        r3, c3 = r1, c1
        while valid(r3, c3, rows, cols):
            antinodes.add((r3, c3))
            i += 1
            r3 = r1 + (rd * i)
            c3 = c1 + (cd * i)

        i = 0
        r4, c4 = r2, c2
        while valid(r4, c4, rows, cols):
            antinodes.add((r4, c4))
            i += 1
            r4 = r2 - (rd * i)
            c4 = c2 - (cd * i)

    return antinodes


def valid(row, col, rows, cols):
    return row >= 0 and row < rows and col >= 0 and col < cols


def getPairs(coords):
    pairs = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            pairs.append((coords[i], coords[j]))
    return pairs


def getAntennas():
    f = open("input.txt", "r")
    antennas = collections.defaultdict(list)
    rows, cols = 0, 0
    for line in f.readlines():
        # Subtract 1 because of newline
        cols = len(line) - 1
        for col in range(len(line)):
            if line[col] != ".":
                antennas[line[col]].append((rows, col))
        rows += 1
    f.close()
    return rows, cols, antennas


if __name__ == "__main__":
    main()