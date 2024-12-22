def main():
    inputs = getInputs()
    ans1, ans2 = 0, 0

    for i in inputs:
        strings = bfs(i)
        min1, min2 = float("inf"),  float("inf")

        for string in strings:
            min1 = min(min1, twoBots(string))
            min2 = min(min2, twentyFiveBots(string))
   
        ans1 += int(i[:3]) * min1
        ans2 += int(i[:3]) * min2

    print(ans1)
    print(ans2)


def twoBots(string):
    string = getCode(string)
    string = getCode(string)
    return len(string)


def twentyFiveBots(string):
    global twelveDict
    string = getCode(string)

    thirteenth = ""
    for prev, curr in zip("A" + string, string):
        thirteenth += twelveDict[prev][curr]

    length = 0
    for prev, curr in zip("A" + thirteenth, thirteenth):
        length += len(twelveDict[prev][curr])

    return length


def getCode(string):
    res = ""
    for prev, curr in zip("A" + string, string):
        res += charDict[prev][curr]
    return res

    
def bfs(line):
    paths, vis = [], {}
    pad = getNPad()
    q = [(line, "A", "")]

    while q:
        line, curr, path = q.pop(0)
        if line[0] == curr:
            line = line[1:]
            path += "A"

            if len(line) == 0:
                paths.append(path)
                continue

        if (line, curr) in vis and vis[(line, curr)] < len(path):
            continue
        vis[(line, curr)] = len(path)

        for symbol, direction in pad[curr]:
            q.append((line, symbol, path + direction))
    
    return [i for i in paths if len(i) == len(paths[0])]


def getTwelveDict():
    global charDict
    d = {}
    for ch in ["^", ">", "v", "<", "A"]:
        d[ch] = {}
        for nextCh in ["^", ">", "v", "<", "A"]:
            string = charDict[ch][nextCh]
            for _ in range(11):
                string = getCode(string)
            d[ch][nextCh] = string

    return d


def getCharDict():
    charDict = {}
    charDict["<"] = {"^": ">^A", ">": ">>A", "v": ">A", "<": "A", "A": ">>^A"}
    charDict["v"] = {"^": "^A", ">": ">A", "v": "A", "<": "<A", "A": "^>A"}
    charDict[">"] = {"^": "<^A", ">": "A", "v": "<A", "<": "<<A", "A": "^A"}
    charDict["^"] = {"^": "A", ">": "v>A", "v": "vA", "<": "v<A", "A": ">A"}
    charDict["A"] = {"^": "<A", ">": "vA", "v": "<vA", "<": "v<<A", "A": "A"}
    return charDict


def getNPad():
    np = {}
    np["A"] = [("0", "<"), ("3", "^")]
    np["0"] = [("A", ">"), ("2", "^")]
    np["1"] = [("2", ">"), ("4", "^")]
    np["2"] = [("3", ">"), ("5", "^"), ("1", "<"), ("0", "v")]
    np["3"] = [("6", "^"), ("2", "<"), ("A", "v")]
    np["4"] = [("5", ">"), ("7", "^"), ("1", "v")]
    np["5"] = [("6", ">"), ("8", "^"), ("4", "<"), ("2", "v")]
    np["6"] = [("9", "^"), ("5", "<"), ("3", "v")]
    np["7"] = [("8", ">"), ("4", "v")]
    np["8"] = [("9", ">"), ("7", "<"), ("5", "v")]
    np["9"] = [("8", "<"), ("6", "v")]
    return np


def getInputs():
    f = open("input.txt", "r")
    inputs = []
    for line in f.readlines():
        inputs.append(line.strip())
    f.close()
    return inputs


if __name__ == "__main__":
    charDict = getCharDict()
    twelveDict = getTwelveDict()
    main()