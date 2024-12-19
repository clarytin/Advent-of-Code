import collections


def main():
    towelList, patterns = getInput()
    
    towels = collections.defaultdict(list)
    for towel in towelList:
        towels[towel[0]].append(towel)

    count = 0
    prev = {}
    for pattern in patterns:
        count += makePattern(towels, pattern, prev)
    print(count)


def makePattern(towels, pattern, prev):
    if pattern == "":
        return 1
    
    if pattern in prev:
        return prev[pattern]
    for towel in towels[pattern[0]]:
        if towel == pattern[:len(towel)]:

            if makePattern(towels, pattern[len(towel):], prev) == 1:
                prev[pattern] = 1
                return 1
        
    prev[pattern] = 0
    return 0


def getInput():
    f = open("input.txt", "r")

    towels = f.readline().strip().replace(" ", "").split(",")
    f.readline()

    patterns = []
    for line in f.readlines():
        patterns.append(line.strip())

    f.close()
    return towels, patterns


if __name__ == "__main__":
    main()