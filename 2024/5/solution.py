import collections


def main():
    rules = getRules()
    # [Answer to Part 1, Answer to Part 2]
    ans = [0,0]
    f = open("input.txt", "r")

    for line in f.readlines():
        line = line.rstrip()
        nums = line.split(",")
        nums, invalid = fix(nums, rules)
        ans[invalid] += int(nums[(len(nums) // 2)])

    f.close()
    
    print(ans)
        

def fix(nums, rules):
    invalid = 0
    i = 1

    while i < len(nums):
        ruleSet = rules[nums[i]]
        movement = 1

        for j in range(i-1,-1,-1):
            if nums[j] in ruleSet:
                nums.insert(i+1, nums[j])
                nums.pop(j)
                movement -= 1
                invalid = 1

        i += movement 
    
    return nums, invalid


def getRules():
    f = open("rules.txt", "r")

    rules = collections.defaultdict(set)
    for line in f.readlines():
        line = line.rstrip()
        rule = line.split("|")
        rules[rule[0]].add(rule[1])
    
    f.close()
    
    return rules


if __name__ == "__main__":
    main()