import os
import requests
import time
import bs4
from selenium import webdriver


def download_image(url, folder_name, num):
    response = requests.get(url)
    # wb (write binary) opens the file in binary format for writing
    if response.status_code == 200:
        with open(os.path.join(folder_name, str(num) + ".jpg"), "wb") as file:
            file.write(response.content)


# chromeDriverPath = "/home/akshay/Desktop/tim-scraper/chromedriver"
driver = webdriver.Safari()
searchUrl = "https://www.google.com/search?q=car+road+images&sxsrf=APwXEdeGFQR-JosTtFkQHgkpJSAjeqOShQ:1681381166830&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiAsrT50Kb-AhXyTmwGHWhlAGMQ_AUoAXoECAEQAw&biw=946&bih=964&dpr=1"

driver.execute_script("window.scrollTo(0,0);")
driver.get(searchUrl)

page_html = driver.page_source

pageSoup = bs4.BeautifulSoup(page_html, "html.parser")
containers = pageSoup.find_all("div", {"class": "isv-r PNCib MSM1fd BUooTd"})

for i in range(1, len(containers) + 1):
    if i % 25 == 0:
        continue
    xPath = f'//*[@id="islrg"]/div[1]/div[{i}]'

    previewImageXPath = f'//*[@id="islrg"]/div[1]/div[4]/a[1]/div[1]/img'
    previewImageElement = driver.find_element("xpath", previewImageXPath)
    previewImageURL = previewImageElement.get_attribute("src")

    driver.find_element("xpath", xPath).click()

    timeStarted = time.time()

    while True:
        try:
            imageElement = driver.find_element(
                "xpath",
                '//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div[2]/div[1]/a/img[1]',
            )
            imageURL = imageElement.get_attribute("src")

            print(f"\n\n{imageElement=}")

            if imageURL != previewImageURL:
                print("Full res image", imageURL)
                break
            else:
                curretcTime = time.time()
                if curretcTime - timeStarted > 10:
                    print("Downloading lower resolution image and moving to next one")
                break
        except Exception as e:
            print(e)
