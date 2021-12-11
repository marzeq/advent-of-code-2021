with open("input.txt", "r") as f:
    input_data = [char for line in f.read().split("\n") for char in line.split(" | ")[1].split(" ")]

print(len(list(filter(lambda x: len(x) in [2, 3, 4, 7], input_data))))
