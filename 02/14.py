n = input()

with open('hightemp.txt') as f:
    for i, line in enumerate(f):
        if i >= int(n):
            break
        print(line.strip())

# head -n 5 hightemp.txt
#デフォルトは10行
