import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}


def extremetube_crawl(link):
    extremetube_list = []

    try:
        response = requests.get(link, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.select("a")

        iframe_url = soup.select("iframe")
        keyword = 'extremetube'

        if iframe_url:
            for i in iframe_url:
                try:
                    emb = i.get("src")
                    if keyword in emb:
                        extremetube_list.append(emb)
                except:
                    pass

        if links:
            for link in links:
                link_href = link.get("href")

                if keyword in str(link_href):
                    extremetube_list.append(link_href)

            extremetube_list = list(set(extremetube_list))
            return extremetube_finishing(extremetube_list)

    except Exception as e:
        print(e)


def extremetube_finishing(extremetube_list):
    domain_link=[]

    for link in extremetube_list:
        viewkey = link.split('/')[4]

        try:
            viewkey = viewkey.split('&')[0]
            viewkey = viewkey.split('?')[0]
        except Exception as e:
            pass

        viewkey=viewkey.strip()



        link = "https://www.extremetube.com/video/" + viewkey
        embedlink = "https://www.extremetube.com/embed/" + viewkey
        domain = 'extremetube'

        # print(domain)
        # print(link)
        # print(embedlink)

        domain_box=[link,embedlink,domain]
        domain_link.append(domain_box)

    return domain_link


# extremetube_crawl("http://hmekumeku.blogterest.net/page/7855/")
