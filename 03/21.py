import gzip
import json
import re

def Wiki_UK():
    with gzip.open('jawiki-country.json.gz', 'r') as f:
        for line in f:
            json_data = json.loads(line)
            if json_data['title'] == 'イギリス':
                return json_data['text']

pattern = r".*Category.*"
category = re.findall(pattern, Wiki_UK())
for line in category:
    print(line)

'''
for line in Wiki_UK().split('\n'):
    if "Category" in line:
        print(line)
'''
