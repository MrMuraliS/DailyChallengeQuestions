import os
import requests
import time
import bs4


def download_image(url, folder_name, num):
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(folder_name, str(num) + ".jpg"), "wb") as file:
            file.write(response.content)


chromeDriverPath = "/home/akshay/Desktop/tim-scraper/chromedriver"
searchUrl = "https://www.google.com/search?q=car+road+images&sxsrf=APwXEdeGFQR-JosTtFkQHgkpJSAjeqOShQ:1681381166830&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiAsrT50Kb-AhXyTmwGHWhlAGMQ_AUoAXoECAEQAw&biw=946&bih=964&dpr=1"

# Send a GET request to the search URL and get the page source
response = requests.get(searchUrl)
if response.status_code == 200:
    page_html = response.content

pageSoup = bs4.BeautifulSoup(page_html, "html.parser")
containers = pageSoup.find_all("div", {"class": "isv-r PNCib MSM1fd BUooTd"})


for i in range(1, len(containers) + 1):
    if i % 25 == 0:
        continue
    xPath = f'//*[@id="islrg"]/div[1]/div[{i}]'

    previewImageXPath = f'//*[@id="islrg"]/div[1]/div[4]/a[1]/div[1]/img'
    previewImageElement = pageSoup.select_one(previewImageXPath)
    previewImageURL = previewImageElement.get("src")

    # Clicking on the image is not required in this case since we can get the full-res image URL directly
    fullResImageElement = pageSoup.select_one('div[jsname="I4Sytb"] img.n3VNCb')
    fullResImageURL = fullResImageElement.get("src")

    print("Full res image", fullResImageURL)

    # Download the full-resolution image
    download_image(fullResImageURL, "folder_name", i)
