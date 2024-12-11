import re

f = open("input.txt", "r")
file = f.read()
# Put nums in parentheses so they will be in subgroups later
nums = "([0-9]+)"
mulRegex = "mul\(" + nums + "," + nums + "\)"

# List of tuples of form (index, 168,23) from mul(168, 23)
muls = [(i.start(), i.group(1), i.group(2)) for i in re.finditer(mulRegex, file)] 

ans = 0
for index, a, b in muls:
    ans += int(a) * int(b)
print(ans)


# Part 2

doRegex = "do\(\)"
dontRegex = "don\'t\(\)"

dos = [(int(i.start()), True) for i in re.finditer(doRegex, file)] 
donts = [(int(i.start()), False) for i in re.finditer(dontRegex, file)] 
dos.insert(0,(0, True))

cmds = sorted(dos + donts)

ans = 0
i = 1
doing = True
for index, a, b in muls:
    if i < len(cmds) and index > cmds[i][0]:
        doing = cmds[i][1]
        i += 1
    if doing:
        ans += int(a) * int(b)

print(ans)

