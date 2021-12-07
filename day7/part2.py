with open("input.txt", "r") as f:
    crabs = [int(crab) for crab in f.read().split(",")]

best_usage = -1
for i in range(max(crabs)+1):
    usage = sum(map(lambda cr: (abs(cr-i) * (abs(cr-i) + 1)) // 2, crabs))
    if usage < best_usage or best_usage == -1:
        best_usage = usage

print(best_usage)
