import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import configparser
config = configparser.ConfigParser()
config.read('../setting.ini')
section = 'development'
proxy_host = config.get(section, 'proxy_host')
proxy_port = config.get(section,'proxy_port')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % proxy_host + ":" + proxy_port)
print(chrome_options)

driver = webdriver.Chrome(executable_path='../chromedriver.exe',options=chrome_options)
driver.get("https://share-videos.se/auto/video/149362322?uid=13")
driver.implicitly_wait(30) # 秒

element = driver.find_elements_by_css_selector("#video_tag li a")

for i in element :
    print(i.get_attribute("href"))
print(element)
