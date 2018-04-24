import codecs
import random

dataset = []

with codecs.open("rt-polaritydata/rt-polarity.neg", 'r','utf-8', 'ignore') as neg,\
        codecs.open("rt-polaritydata/rt-polarity.pos", 'r', 'utf-8', 'ignore') as pos:

    for (neg_line, pos_line) in zip(neg, pos):
        dataset.append("-1 " + neg_line)
        dataset.append("+1 " + pos_line)

random.shuffle(dataset)
neg_count = 0
pos_count = 0

with open("sentiment.txt", "w") as f:
    for line in dataset:
        if line[0] == '-':
            neg_count += 1
        if line[0] == '+':
            pos_count += 1
        f.write(line)

print("neg: " + str(neg_count))
print("pos: " + str(pos_count))
