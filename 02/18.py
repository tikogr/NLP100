col = []

with open('hightemp.txt') as f:
    for line in f:
        col.append(line.split('\t'))

col.sort(key = lambda x: x[2], reverse=True)

for line in col:
    print('\t'.join(line), end='')

# sort -k 3 -t $'\t' -r hightemp.txt
# sort -k 3 -n -r hightemp.txt
