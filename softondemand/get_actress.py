import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='../chromedriver.exe')
driver.get('https://www.google.com/')


actress = input("女優名を入力 : ")
page = int(input("ページ数 : "))

time.sleep(10)
mainBox=driver.find_elements_by_css_selector('div.videis_s_txt h2')
for i in mainBox :
    print(i.text)


for i in range(0,page) :
    url = 'https://ec.sod.co.jp/prime/videos/genre/?search_type=1&sodsearch=' + actress + '&page='+ str(i) + '&sort=2'
    driver.get(url)
    time.sleep(10)
    mainBox=driver.find_elements_by_css_selector('div.videis_s_txt h2')
    images = driver.find_elements_by_css_selector('div.videis_s_img img')

    for i in mainBox :
        print(i.text)

    for img in images :
        print(img.text)


driver.quit()
