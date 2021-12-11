with open("input.txt", "r") as f:
    content = f.read()
    rows, columns = len(content.split("\n")), len(content.split("\n")[0])

    height_map = []
    for row in content.split("\n"):
        height_map.append([int(x) for x in row])


def get_neighbours(x, y, rowc, colc):
    if x != 0:
        yield (x - 1, y)
    if y != 0:
        yield (x, y - 1)
    if x != rowc - 1:
        yield (x + 1, y)
    if y != colc - 1:
        yield (x, y + 1)


n = 0
for i in range(rows):
    for j in range(columns):
        num = height_map[i][j]
        mapped_neighbours = [height_map[x][y] for (x, y) in get_neighbours(i, j, rows, columns)]
        if min(mapped_neighbours + [num]) == num and mapped_neighbours.count(num) == 0:
            n += num + 1

print(n)
