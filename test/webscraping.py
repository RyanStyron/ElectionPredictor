from bs4 import BeautifulSoup

contents = open('data_files/Polls_FiveThirtyEight.html', 'r', encoding='utf-8')
read_contents = contents.read()
soup = BeautifulSoup(read_contents, 'html.parser')

print(soup.prettify())