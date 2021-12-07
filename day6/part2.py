with open("input.txt", "r") as f:
    fish_list = [int(i) for i in f.read().split(",")]

fish_count = [0 for _ in range(7)]

age_8s, age_7s = 0, 0

for i in range(7):
    fish_count[i] += fish_list.count(i)

for day in range(256):
    fish_count.append(fish_count.pop(0))
    temp_age_8 = fish_count[6]
    fish_count[6] += age_7s
    age_7s = age_8s
    age_8s = temp_age_8

print(sum(fish_count) + age_7s + age_8s)
