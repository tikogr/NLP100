import random

def Typoglycemia(s):
    r = []

    for word in s.split(' '):
        if len(word) <= 4:
            r.append(word)
        else:
            c = list(word[1:-1])
            random.shuffle(c)
            r.append(word[0] + ''.join(c) + word[-1])

    return ' '.join(r)

s = input()

print(Typoglycemia(s))
