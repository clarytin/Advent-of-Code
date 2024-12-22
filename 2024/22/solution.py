def main():
    inputs = getInputs()

    ans = 0
    for num in inputs:
        for _ in range(2000):
            num = getNextNumber(num)
        ans += num
    print(ans)

    d = getSequences(inputs)
    maximum = 0
    for prices in d.values():        
        bananas = sum(prices.values())
        maximum = max(bananas, maximum)
        
    print(maximum)


def getSequences(inputs):
    d = {}

    for num in inputs:
        curr = num
        
        prices = [curr % 10]
        for _ in range(2000):
            curr = getNextNumber(curr)
            prices.append(curr % 10)

        changes = []
        for i in range(1, len(prices)):
            changes.append(prices[i] - prices[i-1])

        for i in range(4, len(changes) + 1):
            seq = tuple(changes[i-4:i])
            result = prices[i]

            if seq not in d: 
                d[seq] = {}
            if num not in d[seq]: 
                d[seq][num] = result

    return d  


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