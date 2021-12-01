with open("input.txt", "r") as f:
    measurements = [int(x) for x in f.readlines()]

threes = []

for i in range(len(measurements)):
    if i + 2 < len(measurements):
        threes.append(sum([measurements[i], measurements[i+1], measurements[i+2]]))

prev = None
increase_count = 0
for three_sum in threes:
    if prev is not None and three_sum > prev:
        increase_count += 1
    prev = three_sum

print(increase_count)
