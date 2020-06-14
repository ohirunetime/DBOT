import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}


def tube8_status(link,proxies):
    try:
        response = requests.get(
            link,
            proxies={"http": proxies, "https": proxies},
            headers=headers)

        # response = requests.get(link,headers=headers)

        link = response.url
        category = link.split('/')[3]
        category2 = link.split('/')[4]
        tube8_id  = link.split('/')[5]

        embedlink='https://www.tube8.com/embed/'+category+'/'+category2+'/'+tube8_id+'/'

        if response.status_code == 404:
            status = 'dead'
        else:
            status = 'alive'

        soup = BeautifulSoup(response.text, 'html.parser')
        viewCountBox = soup.select("div.stats dl dd")
        if viewCountBox :
            viewCount = viewCountBox[-1].text
            viewCount = viewCount.strip()
        else :
            viewCount=None


    except Exception as e:
        status = 'dead'
        link = ''
        embedlink=''
        viewCount=None
        print(e)


    return status,link,embedlink,viewCount
