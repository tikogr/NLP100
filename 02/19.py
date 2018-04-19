with open('hightemp.txt') as f:
    col1 = [line.split('\t')[0] for line in f]

count = {ken:col1.count(ken) for ken in col1}

for ken, freq in sorted(count.items(), key=lambda x: x[1], reverse=True):
    print(str(freq) + '\t' + ken)

# cut -f 1 hightemp.txt | sort | uniq -c | sort -r
