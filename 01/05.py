def n_gram(target, n: int):
    result = []

    for i in range(0, len(target)-n+1):
        result.append(target[i:i+n])

    return result

target = "I am an NLPer"

# 単語bi-gram
words = target.split(' ')
print(n_gram(words, 2))

# 文字bi-gram
print(n_gram(target, 2))
