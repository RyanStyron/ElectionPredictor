from bs4 import BeautifulSoup
import requests
import json
import html_to_json

def extractFromWeb(url):
    page = requests.get(url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html.parser')
        extracted_data = str(soup.find_all('script'))
        return extracted_data

def storeInformation(data):
    poll_dict = {}
    poll_dict["pollster"] = # need to figure out how to parse


url = 'https://www.realclearpolling.com/polls/president/general/2024/trump-vs-biden'
data = extractFromWeb(url)

with open('rcp_data.txt', 'w') as outfile:
    outfile.write(data)

