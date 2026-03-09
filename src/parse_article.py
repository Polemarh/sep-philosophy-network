from bs4 import BeautifulSoup
import requests

def parse_article(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')

    preamble = soup.find("div", id = "preamble").get_text(separator = " ", strip = True)
    main_text = soup.find("div", id = "main-text").get_text(separator = " ", strip = True)
    content = preamble + " " + main_text

    table = {
        "text":content
    }

    return content

if __name__ == "__main__": 
    test_url = "https://plato.stanford.edu/entries/abhidharma/"
    text = parse_article(test_url)
    print(text)