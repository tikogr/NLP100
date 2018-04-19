str1 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
first = {1, 5, 6, 7, 8, 9, 15, 16, 19}

words = str1.split(' ')

str2 = {}

for (num, word) in enumerate(words, 1):
    if num in first:
        str2[word[0:1]] = num
    else:
        str2[word[0:2]] = num

print(str2)
