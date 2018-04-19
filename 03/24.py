import gzip
import json
import re

def Wiki_UK():
    with gzip.open('jawiki-country.json.gz', 'r') as f:
        for line in f:
            json_data = json.loads(line)
            if json_data['title'] == 'イギリス':
                return json_data['text']

#pattern = r"\[\[File\:(.*?)(?:\|.*)?\]\]"
pattern = r"(?:File|ファイル):([^|]*)"
category = re.findall(pattern, Wiki_UK())
for line in category:
    print(line)
