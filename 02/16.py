import math

n = int(input())

with open('hightemp.txt') as f1:
    lines = f1.readlines()

sp = math.ceil(len(lines) / n)

for i in range(n):
    with open('split' + str(i+1) + '.txt', 'w') as f2:
        for j, line in enumerate(lines[i*sp:]):
            if j == sp:
                break
            f2.write(line)

# split -l 5 hightemp.txt
