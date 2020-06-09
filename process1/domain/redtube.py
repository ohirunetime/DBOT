import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}


def redtube_crawl(link):
    redtube_list = []
    keyword = 'redtube.com'

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
                        redtube_list.append(emb)
                except Exception as e:
                    print(e)

        if links:
            for link in links:
                link_href = link.get("href")
                if keyword in str(link_href):
                    redtube_list.append(link_href)

            redtube_list = list(set(redtube_list))
            return redtube_finishing(redtube_list)

    except Exception as e:
        print(e)




def redtube_finishing(redtube_list):
    domain_link=[]

    embedKeyword = "embed"

    for link in redtube_list:

        if embedKeyword in link:
            viewkey = link.split('=')[1].strip()

        else:
            viewkey = link.split('/')[3].strip()

        link = "https://redtube.com/" + viewkey
        embedlink = "https://embed.redtube.com/?id=" + viewkey
        domain = 'redtube'

        # print(domain)
        # print(link)
        # print(embedlink)

        domain_box=[link,embedlink,domain]
        domain_link.append(domain_box)

    return domain_link




# redtube_crawl('https://adultcurator.site/archives/53043')
