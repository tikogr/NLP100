n = int(input())

with open('hightemp.txt') as f:
    lines = f.readlines()
    for line in lines[-n:]:
        print(line.strip())

# tail -n 2 hightemp.txt
