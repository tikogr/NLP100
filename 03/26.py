import gzip
import json
import re

def Wiki_UK():
    with gzip.open('jawiki-country.json.gz', 'r') as f:
        for line in f:
            json_data = json.loads(line)
            if json_data['title'] == 'イギリス':
                return json_data['text']

flag = False

dict = {}
for line in Wiki_UK().split('\n'):
    if re.match(r'\{\{基礎情報', line):
        flag = True
    elif re.match(r'\}\}', line):
        break
    elif flag:
        if re.match(r'\|', line):
            info = re.search(r'^\|(.*?)\s*=\s*(.*)', line).groups()
            dict[info[0]] = re.sub(r'\'\'+', '', info[1])
        else:
            dict[info[0]] += re.sub(r'\'\'+', '', line)

print(dict)
