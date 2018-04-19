sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

words = sentence.split(" ")

word = []

for i in words:
	word.append(len(i) - i.count(',') - i.count('.'))

print(word)
