with open("input.txt", "r") as f:
    lines = f.read().split("\n")


opening_to_closing = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

closing_to_points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

score = 0

for line in lines:
    brace_stack = []
    for char in line:
        if char in ["{", "[", "(", "<"]:
            brace_stack.append(char)
        elif char in ["}", "]", ")", ">"]:
            if opening_to_closing[brace_stack[-1]] == char:
                brace_stack.pop()
            else:
                score += closing_to_points[char]
                break

print(score)
