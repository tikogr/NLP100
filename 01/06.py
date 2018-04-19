def n_gram(target, n: int):
    result = []

    for i in range(0, len(target)-n+1):
        result.append(target[i:i+n])

    return result

str1 = 'paraparaparadise'
str2 = 'paragraph'

x = set(n_gram(str1, 2))
y = set(n_gram(str2, 2))
print('X:'+ str(x))
print('Y:'+ str(y))
print('和集合：' + str(x|y))
print('積集合：' + str(x&y))
print('差集合：' + str(x-y))

print('\'se\' in X: ' + str('se' in x))
print('\'se\' in Y: ' + str('se' in y))
