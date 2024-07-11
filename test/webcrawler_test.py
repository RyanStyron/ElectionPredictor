import requests
from bs4 import BeautifulSoup
import json

def crawler(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    link_elements = soup.select("a[href]")

    urls = []
    for link_element in link_elements:
        href = link_element['href']
        if "https://www.realclearpolling.com/" in href:
            urls.append(href)
    
    return urls

def retrieveData(url, polls):
    new_poll = {}
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    script_tags = soup.find_all('script')

    for script_tag in script_tags:
        try:
            json_data = json.loads(str(script_tag))

            new_poll["id"] = json_data.get("id", "")
            new_poll["type"] = json_data.get("type", "")
            new_poll["pollster"] = json_data.get("pollster", "")
            new_poll["updated"] = json_data.get("updated", "")
            new_poll["link"] = json_data.get("link", "")
            new_poll["date"] = json_data.get("date", "")
            new_poll["data_start_date"] = json_data.get("data_start_date", "")
            new_poll["data_end_date"] = json_data.get("data_end_date", "")
            new_poll["confidenceInterval"] = json_data.get("confidenceInterval", "")
            new_poll["sampleSize"] = json_data.get("sampleSize", "")
            new_poll["marginError"] = json_data.get("marginError", "")
            new_poll["partisan"] = json_data.get("partisan", "")
            new_poll["pollster_type"] = json_data.get("pollster_type", "")
            new_poll["data_show"] = json_data.get("data_show", "")
            new_poll["candidate"] = json_data.get("candidate", "")
            new_poll["undecided"] = json_data.get("undecided", "")
            new_poll["spread"] = json_data.get("spread", "")

            polls.append(new_poll)
        
        except json.JSONDecodeError as e:
            # print(f"Error decoding JSON from {url}: {e}")
            continue
    
    print(f"No valid JSON found in {url}")



if __name__ == "__main__":
    base_url = 'https://www.realclearpolling.com/polls/president/general/2024/trump-vs-biden'
    url_list = crawler(base_url)
    # print(url_list)

    polls = []

    for url in url_list:
        retrieveData(url, polls)

    with open('polls_data.json', 'w') as json_file:
        json.dump(polls, json_file, indent=4)

    print("Data saved successfully")
    