import configparser
from eroterest import get_articles, get_eroblog
from eroblog import domain_judge
from selenium import webdriver



config = configparser.ConfigParser()
config.read('../setting.ini')
section = 'development'
proxies = config.get(section, 'proxies')
LocalDatabaseURI = config.get(section, 'LocalDatabaseURI')
print(proxies)


chrome_option = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path='../chromedriver.exe')


def main():

    start_url, finish_page, actress = init()

    count = 0

    for i in range(1, finish_page):

        current_page = start_url + "&c=&page=" + str(i)

        print("現在 : ", i, "ページ目")

        try:
            article_list = get_articles(current_page, proxies)
            eroblog_list = get_eroblog(article_list, proxies)
            domain_judge(eroblog_list, actress,LocalDatabaseURI,driver)

        except Exception as e:
            print(e)
            count += 1

    driver.close()
    driver.quit()

    print("finish!! not catch url =", count)


def init():
    print("女優名を入力してください")
    actress = str(input())
    print("URLを入力してください")
    start_url = input()
    print("finish_pageを入力してください")
    finish_page = int(input())
    return start_url, finish_page , actress


main()
