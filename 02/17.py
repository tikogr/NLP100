ken = set()

with open('hightemp.txt') as f:
    for line in f:
        col = line.split('\t')
        ken.add(col[0])

print(list(ken))

# cut -f 1 hightemp.txt | sort | uniq
