with open("input.txt", "r") as f:
    lines = [line.split(" -> ") for line in f.read().split("\n")]
    for line in lines:
        line[0] = int(line[0].split(",")[0]), int(line[0].split(",")[1])
        line[1] = int(line[1].split(",")[0]), int(line[1].split(",")[1])

vents = {}

for line in lines:
    x0, y0 = line[0]
    x1, y1 = line[1]

    if x0 == x1:
        for y in range(min(y0, y1), max(y0, y1) + 1):
            v = x0, y
            if v in vents:
                vents[v] += 1
            else:
                vents[v] = 1

    elif y0 == y1:
        for x in range(min(x0, x1), max(x0, x1) + 1):
            v = x, y0
            if v in vents:
                vents[v] += 1
            else:
                vents[v] = 1

print(len([vent for vent in vents if vents[vent] > 1]))
