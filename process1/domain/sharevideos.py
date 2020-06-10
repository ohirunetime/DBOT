from bs4 import BeautifulSoup
import requests
import time

from domain.pornhub import pornhub_finishing
from domain.tube8 import tube8_finishing
from domain.javynow import javynow_finishing
from domain.redtube import redtube_finishing
from domain.youporn import youporn_finishing
from domain.spankbang import spankbang_finishing


# test
# from pornhub import pornhub_finishing
# from tube8 import tube8_finishing
# from javynow import javynow_finishing
# from redtube import redtube_finishing
# from youporn import youporn_finishing
# from spankbang import spankbang_finishing


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}



def sharevideos_crawl(link,driver):
    sharevideos_link=sharevideos_setting(link)

    video_url = sharevideos_bs4(sharevideos_link,driver)
    domain_link = sharevideos_domain_check(video_url)
    return domain_link


def sharevideos_setting(link) :

    sharevideos_list = []
    keyword = 'share-videos.se'

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
                        emb='https://share-videos.se/auto/video/' + emb.split('/')[5].stripe()

                        sharevideos_list.append(emb)
                except Exception as e:
                    print(e)
        if links:
            for link in links:
                link_href = link.get("href")
                if keyword in str(link_href):
                    sharevideos_list.append(link_href)

            sharevideos_list = list(set(sharevideos_list))
            sharevideos_link=sharevideos_list[0]
            # print(sharevideos_link)

    except Exception as e:
        sharevideos_link=None
        print(e)


    return sharevideos_link



def sharevideos_bs4(sharevideos_link,driver) :


    try:
        # chrome_option = webdriver.ChromeOptions()
        # driver = webdriver.Chrome(executable_path='../chromedriver.exe')

        driver.get(sharevideos_link)
        time.sleep(3)

        html = driver.page_source.encode('utf-8')
        # driver.close()
        # driver.quit()

        soup = BeautifulSoup(html, "html.parser")
        soup2=soup.select_one("#video_tag")
        link_all=soup2.find_all('a',href=True,text=True)

        get_link=[]
        for i in link_all :
            get_link.append(i.get("href"))

        video_url=get_link[-1]

    except Exception as e:
        video_url=[]
        print(e)

    return video_url


def sharevideos_domain_check(video_url) :

    pornhub_keyword="pornhub.com"
    tube8_keyword="tube8.com"
    youporn_keyword="youporn.com"
    redtube_keyword="redtube.com"
    javynow_keyword = "javynow.com"
    spankbang_keyword="spankbang.com"

    # PornHub
    if pornhub_keyword in video_url :
        pornhub_list = []
        pornhub_list.append(video_url)

        print("pornhub_finishing ... by sharevideos")
        domain_link = pornhub_finishing(pornhub_list)

    # Tube8
    elif tube8_keyword in video_url :
        tube8_list = []
        tube8_list.append(video_url)
        domain_link = tube8_finishing(tube8_list)

    # youporn
    elif youporn_keyword in video_url :
        youporn_list = []
        youporn_list.append(video_url)
        domain_link = youporn_finishing(youporn_list)

    # RedTube
    elif redtube_keyword in video_url :
        redtube_list = []
        redtube_list.append(video_url)
        domain_link = redtube_finishing(redtube_list)

    # JavyNow
    elif javynow_keyword in video_url :
        javynow_list = []
        javynow_list.append(video_url)
        domain_link = javynow_finishing(javynow_list)

    # Spankbang
    elif spankbang_keyword in video_url :
        spankbang_list = []
        spankbang_list.append(video_url)
        domain_link = spankbang_finishing(spankbang_list)

    else :
        domain_link = []

    print(domain_link)

    return domain_link



# sharevideos_crawl('http://dougamuryouchannel.fc2.xxx/blog-entry-1260.html')
