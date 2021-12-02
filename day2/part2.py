with open("input.txt", "r") as f:
    commands = [(x.split()[0], int(x.split()[1])) for x in f.readlines()]

horizontal_pos, depth, aim = 0, 0, 0

for command in commands:
    if command[0] == "up":
        aim -= command[1]
    elif command[0] == "down":
        aim += command[1]
    elif command[0] == "forward":
        horizontal_pos += command[1]
        depth += aim * command[1]

print(horizontal_pos * depth)