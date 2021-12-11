with open("input.txt", "r") as f:
    content = f.read()
    rows, columns = len(content.split("\n")), len(content.split("\n")[0])

    height_map = []
    for row in content.split("\n"):
        height_map.append([int(x) for x in row])


def get_neighbours(x, y, colc, rowc):
    if x != 0:
        yield (x - 1, y)
    if y != 0:
        yield (x, y - 1)
    if x < colc - 1:
        yield (x + 1, y)
    if y < rowc - 1:
        yield (x, y + 1)


def find_basin(x, y, visited=[]):
    visited = visited.copy()
    if height_map[y][x] == 9:
        return visited
    visited.append((x, y))
    for nx, ny in get_neighbours(x, y, columns, rows):
        if (nx, ny) not in visited and height_map[ny][nx] > height_map[y][x]:
            visited = find_basin(nx, ny, visited)
    return visited


basins: list[list[tuple[int, int]]] = []
for y in range(rows):
    for x in range(columns):
        basins.append(find_basin(x, y))

basins = sorted(basins, key=lambda x: len(x), reverse=True)[:3]
lens = [len(x) for x in basins]
print(lens[0] * lens[1] * lens[2])
