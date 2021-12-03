with open("input.txt", "r") as f:
    str_binary_nums = [x for x in f.read().split("\n")]

cols = []
for col_num in range(len(str_binary_nums[0])):
    cols.append([row[col_num] for row in str_binary_nums])

gamma_binary_str = ""
for col in cols:
    gamma_binary_str += max(set(col), key=col.count)

gamma_rate = int(gamma_binary_str, 2)

epsilon_binary_str = ""
for col in cols:
    epsilon_binary_str += min(set(col), key=col.count)

epsilon_rate = int(epsilon_binary_str, 2)

print(gamma_rate * epsilon_rate)
