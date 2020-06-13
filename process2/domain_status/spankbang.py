import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}


def spankbang_status(link, proxies):
    try:
        response = requests.get(
            link,
            proxies={"http": proxies, "https": proxies},
            headers=headers)

        soup = BeautifulSoup(response.text, 'html.parser')
        removed = soup.select_one("div.video_removed_page")

        if removed or response.status_code == 404:
            status = 'dead'
        else:
            status = 'alive'

        viewCountBox = soup.select_one("span.i-plays")
        if viewCountBox:
            viewCount = viewCountBox.text
            viewCount = viewCount.split(" ")[0]
            viewCount = viewCount.strip()
        else:
            viewCount = None

    except Exception as e:
        status = 'dead'
        viewCount = None
        print(e)

    return status, viewCount
