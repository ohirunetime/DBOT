import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
     (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}

def youporn_crawl(link) :
    youporn_list=[]
    keyword = 'youporn.com'

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
                        youporn_list.append(emb)
                except:
                    pass

        if links:
            for link in links:
                link_href = link.get("href")

                if keyword in str(link_href):
                    youporn_list.append(link_href)

            youporn_list = list(set(youporn_list))
            return youporn_finishing(youporn_list)

    except :
        print("youporn_crawl() : http connection error ")


def youporn_finishing(youporn_list):
    domain_link=[]

    for link in youporn_list:
        viewkey = link.split('/')[4].strip()

        link = "https://www.youporn.com/watch/" + viewkey
        embedlink = "https://www.youporn.com/embed/" + viewkey
        domain = 'youporn'

        # print(domain)
        # print(link)
        # print(embedlink)

        domain_box=[link,embedlink,domain]
        domain_link.append(domain_box)

    return domain_link


# youporn_crawl('https://manyoppai.com/474094')
