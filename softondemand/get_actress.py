import time
from selenium import webdriver
import requests
import psycopg2

import configparser
config = configparser.ConfigParser()
config.read('../setting.ini')
section = 'development'

herokuURI = config.get(section, 'herokuURI')

driver = webdriver.Chrome(executable_path='../chromedriver.exe')
driver.get('https://www.google.com/')


actress = input("女優名を入力 : ")
page = int(input("ページ数 : "))

time.sleep(3)

for i in range(0, page):
    url = 'https://ec.sod.co.jp/prime/videos/genre/?search_type=1&sodsearch=' + \
        actress + '&page=' + str(i) + '&sort=2'
    driver.get(url)
    time.sleep(10)
    title_Box = driver.find_elements_by_css_selector('div.videis_s_txt h2')
    image_box = driver.find_elements_by_css_selector('div.videis_s_img img')
    link_box = driver.find_elements_by_css_selector('div.videis_s_txt a')

    for title, link in zip(title_Box, link_box):
        title = title.text
        link = link.get_attribute("href")

        conn = psycopg2.connect(herokuURI)
        cur = conn.cursor()

        cur.execute('insert into product (title,link,actress) values (%s,%s,%s)', (title, link,actress))
        conn.commit()
        cur.close()
        conn.close()
        print("insert database success")


driver.quit()
