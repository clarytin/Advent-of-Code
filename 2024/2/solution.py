def main():
    f = open("input.txt", "r")
    
    safes = 0
    alsoSafes = 0
    for line in f.readlines():
        nums = [int(i) for i in line.split()]
        safe = checkSafety(nums)
        safes += safe
        if not safe:
            for i in range(len(nums)):
                if checkSafety(nums[:i] + nums[i+1:]):
                    alsoSafes += 1
                    break
        
    f.close()

    print(safes)
    print(alsoSafes)


def checkSafety(nums):
    if len(nums) < 2:
        return 1
    
    inc = nums[1] - nums[0]
    if inc == 0:
        return 0

    for i in range(1, len(nums)):
        if inc > 0 and nums[i] < nums[i - 1]:
            return 0
        if inc < 0 and nums[i] > nums[i - 1]:
            return 0
        diff = abs(nums[i] - nums[i - 1])
        if diff < 1 or diff > 3:
            return 0
    
    return 1


if __name__ == "__main__":
    main()