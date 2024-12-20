def main():
    inputs = getInputs()
    ans = 0

    for i in inputs:
        minimum = 10000
        strings = bfs(i)

        for string in strings:
            code = getCode(getCode(string))
            minimum = min(minimum, len(code))

        ans += int(i[:3]) * minimum

    print(ans)


def getCode(line):
    dp = {}
    dp["<"] = {"^": ">^A", ">": ">>A", "v": ">A", "<": "A", "A": ">>^A"}
    dp["v"] = {"^": "^A", ">": ">A", "v": "A", "<": "<A", "A": ">^A"}
    dp[">"] = {"^": "<^A", ">": "A", "v": "<A", "<": "<<A", "A": "^A"}
    dp["^"] = {"^": "A", ">": "v>A", "v": "vA", "<": "<vA", "A": ">A"}
    dp["A"] = {"^": "<A", ">": "vA", "v": "<vA", "<": "v<<A", "A": "A"}

    string = ""
    for prev, curr in zip("A" + line, line):
        string += dp[prev][curr]
    return string
    
    
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
    main()