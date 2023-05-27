import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/")
sup = BeautifulSoup(res.text, "html.parser")

links = sup.select(".titleline")
subtext = sup.select(".subtext")


def create_custom(links, subtext):
    hn = []
    for indx, item in enumerate(links):
        title = links[indx].getText()
        link_element = links[indx].find("a")  # Find the <a> tag within the link element
        href = link_element.get("href") if link_element else None
        votes = subtext[indx].select(".score")
        if len(votes):
            points = int(votes[0].getText().replace("points", ""))
            if points > 99:
                hn.append({"title": title, "link": href, "votes": points})
    return hn


pprint.pprint(create_custom(links, subtext))
