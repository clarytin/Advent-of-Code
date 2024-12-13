import collections


def main(): 
    field = getField()
    visited = [[False] * len(field[0]) for _ in field]

    price1, price2 = 0, 0
    for r in range(len(field)):
        for c in range(len(field[r])):
            if not visited[r][c]:

                region = bfs(r, c, field, visited)
                area = len(region)
                perimeter = getPerimeter(region)
                sides = getNumSides(region)

                price1 += area * perimeter
                price2 += area * sides

    print(price1)
    print(price2)


def getNumSides(region):
    sides = collections.defaultdict(list)
    
    for r, c in region:
        if (r-1, c) not in region:
            sides[("r", r, "top")].append(c)
        if (r+1, c) not in region:
            sides[("r", r+1, "bottom")].append(c)
        if (r, c-1) not in region:
            sides[("c", c, "left")].append(r)
        if (r, c+1) not in region:
            sides[("c", c+1, "right")].append(r)

    count = len(sides.values())

    for indexes in sides.values():
        indexes = sorted(indexes)
        for i in range(1, len(indexes)):
            if indexes[i] - indexes[i-1] > 1:
                count += 1

    return count


def getPerimeter(region):
    perimeter = 0

    for r, c in region:
        if (r-1, c) not in region:
            perimeter += 1
        if (r+1, c) not in region:
            perimeter += 1
        if (r, c-1) not in region:
            perimeter += 1
        if (r, c+1) not in region:
            perimeter += 1

    return perimeter


def bfs(r, c, field, visited):
    region = set()
    q = [(field[r][c], r, c)]

    while q:
        prev, r, c = q.pop(0)

        if r < 0 or c < 0 or r >= len(field) or c >= len(field[0]):
            continue
        if visited[r][c]:
            continue

        curr = field[r][c]
        if prev != curr:
            continue

        region.add((r, c))
        visited[r][c] = True

        q.append((curr, r+1, c))
        q.append((curr, r-1, c))
        q.append((curr, r, c+1))
        q.append((curr, r, c-1))

    return region


def getField():
    f = open("input.txt", "r")
    field = []
    for line in f.readlines():
        field.append(line.strip())
    return field


if __name__ == "__main__":
    main()