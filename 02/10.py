f = open('hightemp.txt')

line = f.readline()
count = 0

while line:
    count += 1
    line = f.readline()

f.close
print(count)

# wc -l hightemp.txt
