import time
from selenium import webdriver
import requests

driver = webdriver.Chrome(executable_path='../chromedriver.exe')
driver.get('https://www.google.com/')


actress = input("女優名を入力 : ")
page = int(input("ページ数 : "))

time.sleep(3)

count = 0
for i in range(0, page):
    url = 'https://ec.sod.co.jp/prime/videos/genre/?search_type=1&sodsearch=' + \
        actress + '&page=' + str(i) + '&sort=2'
    driver.get(url)
    time.sleep(10)
    title_Box = driver.find_elements_by_css_selector('div.videis_s_txt h2')
    image_box = driver.find_elements_by_css_selector('div.videis_s_img img')
    link_box = driver.find_elements_by_css_selector('div.videis_s_txt a')

    for title, image, link in zip(title_Box, image_box, link_box):
        title = title.text
        image = image.get_attribute("src")
        link = link.get_attribute("href")

        thumbnail='/static/images'+ actress + str(count)

        print(title, "\n", image, "\n", link)

        file_name = "C:/Users/shinnosuke/Desktop/SODIMAGE/" + actress +'/'+ str(count)+'.jpg'

        response = requests.get(image,stream=True)

        with open(file_name, 'wb') as f:
            f.write(response.content)

        count+=1
        time.sleep(1)

driver.quit()
