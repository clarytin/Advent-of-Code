import collections


def main():
    parties = set()
    graph = getInput()
    
    for key, val in graph.items():
        if key[0] != "t":
            continue
        cpus = list(val)
        for i in range(len(cpus)):
            for j in range(i+1, len(cpus)):
                if cpus[i] in graph[cpus[j]]:
                    parties.add(tuple(sorted([key, cpus[i], cpus[j]])))
    
    print(len(parties))


def getInput():
    f = open("input.txt", "r")
    graph = collections.defaultdict(set)

    for line in f.readlines():
        graph[line[:2]].add(line[3:5])
        graph[line[3:5]].add(line[:2])

    f.close()
    return graph


if __name__ == "__main__":
    main()