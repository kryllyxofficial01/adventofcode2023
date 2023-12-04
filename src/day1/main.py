import pathlib, re

input_path = str(pathlib.Path(__file__).parent.absolute()) + "/input.txt"

lines = []
with open(input_path, "r") as file:
    lines = [line.strip() for line in file.readlines()]

total_calibration = 0
for line in lines:
    matches = "".join(re.findall(r"\d+", line))

    total_calibration += int(matches[0] + matches[-1])

print(total_calibration)