from typing import Literal

# this code is very stupid i do realise that

with open("input.txt", "r") as f:
    str_binary_nums = [x for x in f.read().split("\n")]


def get_winning_num(col: list[str], mode: Literal["oxygen", "co2"]) -> str:
    zero_count = col.count("0")
    one_count = col.count("1")

    if mode == "oxygen":
        if zero_count > one_count:
            return "0"
        elif zero_count < one_count:
            return "1"
        else:
            return "1"
    elif mode == "co2":
        if zero_count < one_count:
            return "0"
        elif zero_count > one_count:
            return "1"
        else:
            return "0"


cols = []
for col_num in range(len(str_binary_nums[0])):
    cols.append([row[col_num] for row in str_binary_nums])

oxygen_dont_count_indexes = []
final_oxygen_num = ""
for col in cols:
    only_counted_indexes_col = [num for inum, num in enumerate(col) if inum not in oxygen_dont_count_indexes]
    if len(only_counted_indexes_col) == 1:
        only_counted_indexes_cols = [[num for inum, num in enumerate(col) if inum not in oxygen_dont_count_indexes] for col in cols]
        final_oxygen_num = "".join([num for col in only_counted_indexes_cols for num in col])
        break
    winning_num = get_winning_num(only_counted_indexes_col, "oxygen")
    final_oxygen_num += winning_num
    oxygen_dont_count_indexes += [loosing_index for loosing_index, num in enumerate(col) if num != winning_num]

final_oxygen_num = int(final_oxygen_num, 2)

co2_dont_count_indexes = []
final_co2_num = ""
for col in cols:
    only_counted_indexes_col = [num for inum, num in enumerate(col) if inum not in co2_dont_count_indexes]
    if len(only_counted_indexes_col) == 1:
        only_counted_indexes_cols = [[num for inum, num in enumerate(col) if inum not in co2_dont_count_indexes] for col in cols]
        final_co2_num = "".join([num for col in only_counted_indexes_cols for num in col])
        break
    winning_num = get_winning_num(only_counted_indexes_col, "co2")
    final_co2_num += winning_num
    co2_dont_count_indexes += [loosing_index for loosing_index, num in enumerate(col) if num != winning_num]
    co2_dont_count_indexes = list(set(co2_dont_count_indexes))

final_co2_num = int(final_co2_num, 2)

print(final_oxygen_num * final_co2_num)
