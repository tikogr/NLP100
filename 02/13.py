with open('col1.txt') as f1, \
        open('col2.txt') as f2, open('marge.txt', 'w') as f3:

    for line1, line2 in zip(f1, f2):
        f3.write(line1.strip() + '\t' + line2)

# paste col1.txt col2.txt
