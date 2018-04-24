stop_words = ["a", "an", "for", "in", "off", "the", "by", "so"]

def check_stop_word(sentence):
    for word in stop_words:
        if word in sentence.split(" "):
            return True
    return False

sentence = input()
print(check_stop_word(sentence))
