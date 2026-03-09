from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

def parse_content():
    response = requests.get("https://plato.stanford.edu/contents.html")
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")
    base_url = "https://plato.stanford.edu/"
    table = []

    titles = soup.select("li a strong")

    for item in titles: 
        link_tag = item.parent

        title = item.text 
        link = link_tag.get("href")
        full_url = urljoin(base_url, link)

        table.append({"url":full_url, "title":title })
    return table

if __name__ == "__main__": 
    text = parse_content()
    print(text)