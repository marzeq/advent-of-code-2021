with open("input.txt", "r") as f:
    lines = f.read().split("\n")

opening_to_closing = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

closing_to_points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}


def get_incomplete(lines):
    for line in lines:
        yield_line = True
        brace_stack = []
        for char in line:
            if char in ["{", "[", "(", "<"]:
                brace_stack.append(char)
            elif char in ["}", "]", ")", ">"]:
                if opening_to_closing[brace_stack[-1]] == char:
                    brace_stack.pop()
                else:
                    yield_line = False
                    break
        if yield_line:
            yield line


scores = []

for line in get_incomplete(lines):
    brace_stack = []
    score = 0
    for char in line:
        if char in ["{", "[", "(", "<"]:
            brace_stack.append(char)
        elif char in ["}", "]", ")", ">"]:
            brace_stack.pop()
    completion = [opening_to_closing[char] for char in brace_stack[::-1]]
    for char in completion:
        score *= 5
        score += closing_to_points[char]
    scores.append(score)

print(sorted(scores)[len(scores) // 2:len(scores) // 2 + 1][0])
