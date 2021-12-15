import sys
import os

newday = sorted([int(day.replace("day", "")) for day in os.listdir(".") if day.startswith("day")])[-1] + 1
os.mkdir(f"day{newday}")
print(f"Created directory for day {newday}")

print("What's the problems sample input?")
sample_data = "".join(sys.stdin.readlines())[:-1]
with open(f"day{newday}/sample.txt", "w") as f:
    f.write(sample_data)

print("What's the problems input?")
input_data = "".join(sys.stdin.readlines())[:-1]
with open(f"day{newday}/input.txt", "w") as f:
    f.write(input_data)

print("Creating part1.py and part2.py")
with open(f"day{newday}/part1.py", "w") as f:
    f.write(f"""with open(\"sample.txt\", \"r\") as f:
    data = f.read()""")

with open(f"day{newday}/part2.py", "w") as f:
    f.write(f"""with open(\"sample.txt\", \"r\") as f:
    data = f.read()""")

print("Done!")
