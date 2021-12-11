with open("input.txt", "r") as f:
    input_data: list[list[str]] = []
    for line in f.read().split("\n"):
        line_list = []
        for io in line.split(" | "):
            line_list.append(io.split())
        input_data.append(line_list)


def decode_line(line: list[str], i: int):
    solved = {}
    segments = {}
    line.sort(key=lambda x: len(x))

    for num in line:
        if len(num) == 2:
            solved[1] = num
        elif len(num) == 3:
            solved[7] = num
        elif len(num) == 4:
            solved[4] = num
        elif len(num) == 7:
            solved[8] = num

    line = [num for num in line if num not in solved.values()]

    for num in line:
        if len(num) == 6:
            if len([char for char in num if char not in solved[4]]) == 2:
                solved[9] = num
            elif len([char for char in num if char not in solved[1]]) == 5:
                solved[6] = num
            else:
                solved[0] = num
        elif len(num) == 5:
            if len([char for char in num if char not in solved[4]]) == 3:
                solved[2] = num
            elif len([char for char in solved[1] if char not in num]) == 0:
                solved[3] = num
            else:
                solved[5] = num

    for key in solved:
        solved[key] = "".join(sorted(solved[key]))
    return solved


outputs = []
for i, line in enumerate(input_data):
    decoded_nums = {v: k for k, v in decode_line(line[0], i).items()}
    output = ""
    for num in line[1]:
        output += str(decoded_nums["".join(sorted(num))])
    outputs.append(int(output))

print(sum(outputs))
