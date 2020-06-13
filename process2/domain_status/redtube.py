import requests
from bs4 import BeautifulSoup
import time
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}


def redtube_status(link):
    try:
        response = requests.get(
            link,
            headers=headers)

        soup = BeautifulSoup(response.text, 'html.parser')


        if response.status_code == 404:
            status = 'dead'
        else:
            status = 'alive'

        viewCountBox = soup.select_one("span.video_view_count")
        if viewCountBox :
            viewCount=viewCountBox.text
            viewCount = viewCount.split(" ")[0]
            viewCount=viewCount.strip()
        else :
            viewCount = None

    except Exception as e:
        status = 'dead'
        viewCount = None
        print(e)

    time.sleep(5)

    return status , viewCount
