# Part 1
with open("day1/input.txt", "r") as f:
    input = f.readlines()

input = [line.strip() for line in input]

calories = []
current_elf = 0

for line in input:
    if line == '':
        current_elf += 1
    else:
        if current_elf >= len(calories):
            calories.append(0)
        calories[current_elf] += int(line)

max_calories = max(calories)
max_elf = calories.index(max_calories)

print(f'Elf {max_elf} is carrying {max_calories} calories.')

# Part 2
top_3 = []

for i in range(3):
    top_3.append(max_calories)
    calories.remove(max_calories)
    max_calories = max(calories)

total = sum(top_3)

print(f'The top 3 elves have a total of {total} calories.')