import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text, "html.parser")
links = soup.select(".titleline")
votes = soup.select(".score")  # . stand for class


def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):  # enumerate = (0, 'cherry'), (1, 'banana')
        link = item.find("a")["href"]
        title = item.getText()

        # title = links[idx].getText()
        # href = links[idx].get('href', None)
        hn.append({"title": title, "link": link if link.startswith("http") else None})
    return hn


print(create_custom_hn(links, votes))
