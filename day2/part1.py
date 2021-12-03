with open("input.txt", "r") as f:
    commands = [(x.split()[0], int(x.split()[1]))
                for x in f.read().split("\n")]

horizontal_pos, depth = 0, 0

for command in commands:
    if command[0] == "up":
        depth -= command[1]
    elif command[0] == "down":
        depth += command[1]
    elif command[0] == "forward":
        horizontal_pos += command[1]

print(horizontal_pos * depth)
