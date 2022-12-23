# Part 1

'''
Rock     (X) = 1 point
Paper    (Y) = 2 points
Scissors (Z) = 3 points

Loss = 0 points
Draw = 3 points
Win  = 6 points

  A B C
X 4 1 7
Y 8 5 2
Z 3 9 6
'''

outcome1 = [[4, 1, 7],
            [8, 5, 2],
            [3, 9, 6]]

# Part 2

'''
Loss (X) vs A = Scissors = 0 + 3 = 3 points
Draw (Y) vs A = Rock     = 3 + 1 = 4 points
Win  (Z) vs A = Paper    = 6 + 2 = 8 points

Loss (X) vs B = Rock     = 0 + 1 = 1 point
Draw (Y) vs B = Paper    = 3 + 2 = 5 points
Win  (Z) vs B = Scissors = 6 + 3 = 9 points

Loss (X) vs C = Paper    = 0 + 2 = 2 points
Draw (Y) vs C = Scissors = 3 + 3 = 6 points
Win  (Z) vs C = Rock     = 6 + 1 = 7 points

  A B C
X 3 1 2
Y 4 5 6
Z 8 9 7
'''

outcome2 = [[3, 1, 2],
            [4, 5, 6],
            [8, 9, 7]]

with open("day2/input.txt", "r") as f:
    input = f.readlines()

input = [line.strip() for line in input]

score = 0

for line in input:
    for character in line:
        if character == 'A':
            y = 0
        if character == 'B':
            y = 1
        if character == 'C':
            y = 2
        if character == 'X':
            x = 0
        if character == 'Y':
            x = 1
        if character == 'Z':
            x = 2
    score += outcome2[x][y]

print(f'The total score is: {score}.')