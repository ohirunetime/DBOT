import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}


def extremetube_status(link,proxies):
    try:
        response = requests.get(
            link,
            proxies={"http": proxies, "https": proxies},
            headers=headers)

        # response = requests.get(link,headers=headers)

        soup = BeautifulSoup(response.text, 'html.parser')
        removed = soup.select("div.deleted-video-msg")

        if removed or response.status_code == 404:
            status = 'dead'
        else:
            status = 'alive'

        viewCountBox = soup.select("div.ibLine1 strong")
        if viewCountBox:
            viewCount = viewCountBox[1].text
            viewCount = viewCount.strip()
        else:
            viewCount = None

    except Exception as e:
        status = 'dead'
        viewCount=None
        print(e)


    return status , viewCount


# extremetube_status('https://www.extremetube.com/video/k417honjo-0000012-43113361')
