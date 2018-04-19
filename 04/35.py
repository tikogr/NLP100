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

max_nouns = []

for line in mor_neko():
    nouns = []
    for morpheme in line:
        if morpheme['pos'] == '名詞':
            nouns.append(morpheme['surface'])
        else:
            if len(nouns) > 1:
                max_nouns.append("".join(nouns))
            nouns = []
    if len(nouns) > 1:
        max_nouns.append("".join(nouns))

max_nouns = set(max_nouns)
print(max_nouns)
