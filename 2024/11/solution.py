import collections


def main(): 
    nums = getNums()

    for _ in range(75):
        adds = collections.defaultdict(int)
        items = [i for i in nums.items()]

        for num, count in items:
            del[nums[num]]
            if num == 0:
                adds[1] += count
            elif len(str(num)) % 2 == 0:
                k = len(str(num)) // 2
                adds[int(str(num)[:k])] += count
                adds[int(str(num)[k:])] += count
            else:
                adds[num * 2024] += count

        for num, count in adds.items():
            nums[num] += count

    print(getCount(nums))


def getCount(nums):
    count = 0
    for val in nums.values():
        count += val
    return count


def getNums():
    f = open("input.txt", "r")

    nums = collections.defaultdict(int)
    for i in f.read().split():
        nums[int(i)] += 1

    f.close()
    return nums


if __name__ == "__main__":
    main()