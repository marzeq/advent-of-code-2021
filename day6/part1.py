with open("input.txt", "r") as f:
    fish_list = [int(fish) for fish in f.read().split(",")]

for day in range(80):
    for ifish in range(len(fish_list)):
        if fish_list[ifish] == 0:
            fish_list[ifish] = 6
            fish_list.append(8)
        else:
            fish_list[ifish] = fish_list[ifish] - 1

print(len(fish_list))
