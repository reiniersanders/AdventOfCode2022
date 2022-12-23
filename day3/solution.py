# Part 1
with open("day3/input.txt", 'r') as f:
    input = f.readlines()

input = [line.strip() for line in input]

def priority(c):
    items = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
             'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    return items.index(c) + 1

score = 0

for line in input:
    length = len(line)
    left   = line[:length//2]
    right  = line[length//2:]
    
    for x in left:
        for y in right:
            if x == y:
                common_item = x
                break
    
    score += priority(common_item)

print(f'Total of all priorities is: {score}.')

# Part 2
score   = 0
line_nr = 0
buffer  = []

for line in input:
    buffer.append(line)
    line_nr += 1
    if line_nr == 3:
        bag1 = buffer[0]
        bag2 = buffer[1]
        bag3 = buffer[2]
        for x in bag1:
            for y in bag2:
                for z in bag3:
                    if x == y == z:
                        badge = x
                        break
        score  += priority(badge)
        buffer  = []
        line_nr = 0

print(f'Total sum of badge priorities: {score}.')