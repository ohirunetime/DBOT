import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}


def pornhub_crawl(link):
    pornhub_list = []
    keyword = 'pornhub.com'

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
                        pornhub_list.append(emb)

                except Exception as e:
                    pass

        if links:
            for link in links:
                link_href = link.get("href")
                if keyword in str(link_href):
                    pornhub_list.append(link_href)

            pornhub_list = list(set(pornhub_list))
            return pornhub_finishing(pornhub_list)
    except :
        print("pornhub_crawl() : http connection error")


def pornhub_finishing(pornhub_list):
    domain_link=[]

    embedKeyword = "embed"

    for link in pornhub_list:

        if embedKeyword in link:
            viewkey = link.split('/')[-1]

        else:
            viewkey = link.split('=')[-1]

        try:
            viewkey = viewkey.split('&')[0]
            viewkey = viewkey.split('=')[1]
        except Exception as e:
            pass

        viewkey = viewkey.strip()



        link = "https://pornhub.com/view_video.php?viewkey=" + viewkey
        embedlink = "https://pornhub.com/embed/" + viewkey
        domain = 'pornhub'

        # print(domain)
        # print(link)
        # print(embedlink)

        domain_box=[link,embedlink,domain]
        domain_link.append(domain_box)

    return domain_link


# pornhub_crawl('https://nureman.net/?p=7207')
