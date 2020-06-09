import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}


def tube8_crawl(link):

    keyword = 'tube8.com'
    tube8_list = []

    try:
        response = requests.get(link, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.select("a")
        iframe_url = soup.select("iframe")


        if iframe_url:
            for i in iframe_url:
                try:
                    emb = i.get("src")
                    if keyword in emb:
                        tube8_list.append(emb)
                except:
                    pass

        if links:
            for link in links:
                link_href = link.get("href")
                if keyword in str(link_href):
                    # print(link_href)
                    tube8_list.append(link_href)

            tube8_list = list(set(tube8_list))
            return tube8_finishing(tube8_list)

    except :
        print("tube8_crawl() : http connection error")




def tube8_finishing(tube8_list):
    domain_link=[]
    domain = 'tube8'
    embedKeyword = 'embed'

    for link in tube8_list:

        if embedKeyword in link:
            viewkey = link.split('/')[6].strip()

        else:
            viewkey = link.split('/')[5].strip()

        link = "http://www.tube8.com/test/test/" + viewkey
        embedlink = "https://www.tube8.com/embed/test/test/" + viewkey

        domain_box=[link,embedlink,domain]
        domain_link.append(domain_box)

    return domain_link

# tube8_crawl('http://winav.work/page/1293/')
