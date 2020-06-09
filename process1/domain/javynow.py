import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}


def javynow_crawl(link):
    javynow_list = []

    try:
        response = requests.get(link, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.select("a")

        iframe_url = soup.select("iframe")
        keyword = 'javynow.com'

        if iframe_url:
            for i in iframe_url:
                try:
                    emb = i.get("src")
                    if keyword in emb:
                        javynow_list.append(emb)
                except Exception as e:
                    print(e)

        if links:
            for link in links:
                link_href = link.get("href")

                if keyword in str(link_href):
                    javynow_list.append(link_href)

            javynow_list = list(set(javynow_list))
            return javynow_finishing(javynow_list)

    except Exception as e:
        print(e)


def javynow_finishing(javynow_list):
    domain = 'javynow'
    domain_link = []

    for link in javynow_list:
        viewkey = link.split('/')[4].strip()

        link = "https://javynow.com/video/" + viewkey + "/"
        embedlink = "https://javynow.com/player/" + viewkey + "/"

        # print(domain)
        # print(link)
        # print(embedlink)

        domain_box = [link, embedlink, domain]
        domain_link.append(domain_box)

    return domain_link


# javynow_crawl('https://share-douga.tokyo/blog-entry-4147.html')
