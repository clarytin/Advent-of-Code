import collections

def main():
    f = open("input.txt", "r")

    first, second = [], []

    for line in f.readlines():
        nums = line.split()
        first.append(int(nums[0]))
        second.append(int(nums[1]))

    f.close()

    part1(first, second)
    part2(first, second)


def part2(first, second):
    d = collections.defaultdict(int)
    for num in second:
        d[num] += 1
    
    score = 0
    for num in first:
        if num in d:
            score += num * d[num]
    
    print(score)


def part1(first, second):
    ans = 0

    first.sort()
    second.sort()

    for a, b in zip(first, second):
        ans += abs(a - b)

    print(ans)


if __name__ == "__main__":
    main()