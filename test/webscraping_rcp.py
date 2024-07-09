from bs4 import BeautifulSoup
import json
import html_to_json

contents = open('data_files/Polls_RealClearPolitics.html', 'r', encoding='utf-8')
read_contents = contents.read()
soup = BeautifulSoup(read_contents, 'html.parser')

pretty_soup = soup.prettify()

with open('realclearpolitics.txt', 'w') as outfile:
    outfile.write(pretty_soup)