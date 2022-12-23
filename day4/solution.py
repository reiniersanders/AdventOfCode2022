# Part 1
with open("day4/input.txt", 'r') as f:
    input = f.readlines()

input = [line.strip() for line in input]

score = 0

for line in input:
    range_strings = line.split(',')
    ranges = []
    for range_string in range_strings:
        first, second = range_string.split('-')
        ranges.append([int(first), int(second)])
    if (ranges[0][0] >= ranges[1][0] and ranges[0][1] <= ranges[1][1]) or (ranges[0][0] <= ranges[1][0] and ranges[0][1] >= ranges[1][1]):
        score += 1

print(f'Number of ranges fully contained within the other: {score}.')

# Part 2
score = 0

for line in input:
    range_strings = line.split(',')
    ranges = []
    for range_string in range_strings:
        first, second = range_string.split('-')
        ranges.append([int(first), int(second)])
    if not (ranges[0][1] < ranges[1][0] or ranges[1][1] < ranges[0][0]):
        score += 1

print(f'Number of pairs that overlap at all: {score}.')