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

anob = []

for line in mor_neko():
    if len(line) > 2:
        for i in range(1, len(line) -2):
            if line[i]['surface'] == 'の' \
                and line[i-1]['pos'] == '名詞' and line[i+1]['pos'] == '名詞':
                anob.append(line[i-1]['surface'] + 'の' + line[i+1]['surface'])

anob = set(anob)
print(anob)
