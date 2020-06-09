import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}


def spankbang_crawl(link):
    spankbang_list = []
    keyword = 'spankbang.com'

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
                        spankbang_list.append(emb)

                except Exception as e:
                    print(e)

        if links:
            for link in links:
                link_href = link.get("href")
                if keyword in str(link_href):
                    spankbang_list.append(link_href)

            spankbang_list = list(set(spankbang_list))
            return spankbang_finishing(spankbang_list)

    except Exception as e :
        print("spankbang_crawl() : http connection error",e)


def spankbang_finishing(spankbang_list):
    domain_link=[]

    embedKeyword = "embed"

    for link in spankbang_list:

        viewkey = link.split('/')[3].strip()

        link = "https://spankbang.com/" + viewkey + "/video/"
        embedlink = "https://spankbang.com/" + viewkey + "/embed/"
        domain = 'spankbang'

        # print(domain)
        # print(link)
        # print(embedlink)

        domain_box=[link,embedlink,domain]
        domain_link.append(domain_box)


    return domain_link


# spankbang_crawl('http://mokkolink.com/2020/06/07/2020060521160936/')
