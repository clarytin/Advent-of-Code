def main():
    f = open("input.txt", "r")
    
    count = 0
    for line in f.readlines():
        line = line.replace(":", "")
        nums = [int(i) for i in line.split()]
        if test(nums[0], nums[1:]):
            count += nums[0]
            
    print(count)
  

def test(res, ns):
    if len(ns) == 2:
        return (res == ns[0] + ns[1]) \
            or (res == ns[0] * ns[1]) \
            or (res == int(str(ns[0]) + str(ns[1])))
    
    return test(res, [ns[0] + ns[1]] + ns[2:]) \
        or test(res, [ns[0] * ns[1]] + ns[2:]) \
        or test(res, [int(str(ns[0]) + str(ns[1]))] + ns[2:])


if __name__ == "__main__":
    main()