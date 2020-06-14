import requests
import time

from domain_status.pornhub import pornhub_status
from domain_status.tube8 import tube8_status
from domain_status.extremetube import extremetube_status
from domain_status.javynow import javynow_status
from domain_status.redtube import redtube_status
from domain_status.youporn import youporn_status
from domain_status.spankbang import spankbang_status
from domain_status.xvideos import xvideos_status

from process2_postgres import process2_database


def domain_check(rows, proxies, herokuURI):
    for row in rows:
        link = row[0]
        embedlink = row[1]
        domain = row[2]
        actress = row[3]

        if domain == 'pornhub':

            status, viewCount = pornhub_status(link, proxies)

        elif domain == 'tube8':

            status, link, embedlink, viewCount = tube8_status(link, proxies)

        elif domain == 'extremetube':

            status, viewCount = extremetube_status(link, proxies)

        elif domain == 'youporn':

            status, viewCount = youporn_status(link, proxies)

        elif domain == 'redtube':

            status, viewCount = redtube_status(link)

        elif domain == 'javynow':

            status, viewCount = javynow_status(link, proxies)

        elif domain in 'spankbang':

            status, viewCount = spankbang_status(link, proxies)

        elif domain in 'xvideos':

            status, link, embedlink, viewCount = xvideos_status(link, proxies)

        else:
            status = 'dead'
            viewCount = None

        if status == 'alive':

            print(status, link, embedlink, domain, actress, viewCount)

        process2_database(link, embedlink, domain, actress,
                          status, viewCount, herokuURI)
