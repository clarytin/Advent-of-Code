import collections


def main():
    towels, patterns = getInput()

    allWays = 0
    prev = {}
    for pattern in patterns:
        allWays += makePattern(towels, pattern, prev)

    count = 0
    for pattern in patterns:
        if prev[pattern] != 0:
            count += 1

    print(count)
    print(allWays)


def makePattern(towels, pattern, prev):
    if pattern == "":
        return 1
    
    if pattern in prev:
        return prev[pattern]
    
    count = 0
    for towel in towels[pattern[0]]:
        if towel == pattern[:len(towel)]:
            count += makePattern(towels, pattern[len(towel):], prev)
        
    prev[pattern] = count
    return count


def getInput():
    f = open("input.txt", "r")

    towelList = f.readline().strip().replace(" ", "").split(",")
    
    towels = collections.defaultdict(list)
    for towel in towelList:
        towels[towel[0]].append(towel)

    f.readline()

    patterns = []
    for line in f.readlines():
        patterns.append(line.strip())

    f.close()
    return towels, patterns


if __name__ == "__main__":
    main()