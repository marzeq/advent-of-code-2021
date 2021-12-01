with open("input.txt", "r") as f:
    measurements = [int(x) for x in f.readlines()]

prev = None
increase_count = 0
for measurement in measurements:
    if prev is not None and measurement > prev:
        increase_count += 1
    prev = measurement

print(increase_count)
