def main():
    inputs = getInputs()
    ans = 0
    for num in inputs:
        for _ in range(2000):
            num = getNextNumber(num)
        ans += num
    print(ans)


def getNextNumber(num):
    num = (num ^ (num << 6)) % 16777216
    num = (num ^ (num >> 5)) % 16777216
    num = (num ^ (num << 11)) % 16777216
    return num


def getInputs():
    f = open("input.txt", "r")
    inputs = []
    for line in f.readlines():
        inputs.append(int(line.strip()))
    f.close()
    return inputs


if __name__ == "__main__":
    main()