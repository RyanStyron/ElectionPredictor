from bs4 import BeautifulSoup
import json

"""
contents = open('data_files/Polls_FiveThirtyEight.html', 'r', encoding='utf-8')
read_contents = contents.read()
soup = BeautifulSoup(read_contents, 'html.parser')

pretty_soup = soup.prettify()
print(pretty_soup)
"""

with open('data_files/Polls_FiveThirtyEight.html', 'r', encoding='utf-8') as contents:
    read_contents = contents.read()

soup = BeautifulSoup(read_contents, 'html.parser')

script_tag = soup.find('script', {'type': 'application/json'})

if script_tag:
    data = script_tag.string.strip()
    json_data = json.loads(data)
    pretty_json = json.dumps(json_data, indent=4)
    print(pretty_json)
else:
    print("No script tag found")
