with open('hightemp.txt') as f1,\
        open('col1.txt', 'w') as f2, open('col2.txt', 'w') as f3:

    for line in f1:
        col = line.split('\t')
        f2.write(col[0] + '\n')
        f3.write(col[1] + '\n')

# cut -f 1 hightemp.txt
# cut -f 1 -d $'\t' hightemp.txt
