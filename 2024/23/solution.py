import collections


def main():
    graph = getInput()
    triplets = getTriplets(graph)

    ans = 0
    for i in triplets:
        if i[0][0] == "t" or i[1][0] == "t" or i[2][0] == "t":
            ans += 1

    print(ans)

    cliques = set()

    maximum = 0
    largest = None
    for clique in cliques:
        largest = clique if len(clique) > maximum else largest
        maximum = max(maximum, len(clique))
 
    string = str(sorted(list(largest)))[1:-1]
    print(string.replace(" ", "").replace("\'", ""))


def BronKerbosch(R, P, X, graph, cliques):
    if len(P) == 0 and len(X) == 0:
        cliques.add(tuple(R))
        return
    for v in set(P):
        BronKerbosch(R | {v}, P & graph[v], X & graph[v], graph, cliques)
        P -= {v}
        X | {v} 


def connected(comp, key, graph):
    for c in comp:
        if c not in graph[key]:
            return False
    return True
  
    
def getTriplets(graph):
    parties = set()

    for key, val in graph.items():
        cpus = list(val)
        for i in range(len(cpus)):
            for j in range(i+1, len(cpus)):
                if cpus[i] in graph[cpus[j]]:
                    parties.add(tuple(sorted([key, cpus[i], cpus[j]])))
    
    return parties


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