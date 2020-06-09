import requests
from bs4 import BeautifulSoup
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}

def get_articles(current_page,proxies):
    article_list = []

    try:
        response = requests.get(current_page,
         headers=headers,
         proxies={"http": proxies, "https": proxies}
         )
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.select("div.listWrapper div.itemTitle a")

        if articles:
            for article in articles:
                print(article.get("title"))
                print(article.get("href"))
                article_list.append(article.get("href"))

    except :
        print("get_articles(): http error")

    return article_list


def get_eroblog(article_list,proxies):
    eroblog_list = []
    count = 0

    for article in article_list:
        count += 1

        try:
            response = requests.get(
                article,
                proxies={"http": proxies, "https": proxies},
                headers=headers,
            )
            soup = BeautifulSoup(response.text, 'html.parser')
            blog_link = soup.select_one("div.gotoBlog a").get("href")
            domain = soup.select_one("span.proName").text
            box = [blog_link, domain]
            eroblog_list.append(box)

        except Exception as e:
            print(e)

        print(count, "/", len(article_list), " : ", article)

    return eroblog_list
