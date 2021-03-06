import numpy
from collections import Counter
from matplotlib import pyplot
from matplotlib.font_manager import FontProperties

def mor_neko():
    morphemes = []

    with open('neko.txt.mecab') as f:
        for line in f:
            cols = line.split('\t')

            if len(cols) >= 2:
                info = cols[1].split(',')

                morpheme = {
                'surface': cols[0],    # 表層系
                'base': info[6],       # 基本形
                'pos': info[0],        # 品詞
                'pos1': info[1]        # 品詞細分類
                }
                morphemes.append(morpheme)

                if cols[0] == '。':
                    yield morphemes
                    morphemes = []

words = []

for line in mor_neko():
    for morpheme in line:
                words.append(morpheme['surface'])

mycounter = Counter(words)
labels = []
data = []

for word in mycounter.most_common(10):
    labels.append(word[0])
    data.append(word[1])

pyplot.rcParams['font.family'] = 'IPAPGothic'
#pyplot.rcParams['font.family'] = 'AppleGothic'

pyplot.title("頻度上位10語")
pyplot.bar(numpy.array(range(len(data))), data, tick_label=labels, align="center")
pyplot.show()
