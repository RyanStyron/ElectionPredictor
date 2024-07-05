from bs4 import BeautifulSoup
import json
import html_to_json

contents = open('data_files/Polls_FiveThirtyEight.html', 'r', encoding='utf-8')
read_contents = contents.read()
soup = BeautifulSoup(read_contents, 'html.parser')

pretty_soup = soup.prettify()
json_soup = html_to_json.convert(pretty_soup);

with open('fivethirtyeight.txt', 'w') as outfile:
    outfile.write(pretty_soup)


# print(json_soup['cycles'])