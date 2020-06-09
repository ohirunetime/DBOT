import requests
import time

from domain_status.pornhub import pornhub_status
from domain_status.tube8 import tube8_status
from domain_status.extremetube import extremetube_status
from domain_status.javynow import javynow_status
from domain_status.redtube import redtube_status
from domain_status.youporn import youporn_status
from domain_status.spankbang import spankbang_status


def domain_check(rows, proxies):
    for row in rows:
        link = row[0]
        embedlink = row[1]
        domain = row[2]
        actress = row[3]

        if domain == 'pornhub':

            status = pornhub_status(link, proxies)

        elif domain == 'tube8':

            status = tube8_status(link, proxies)

        elif domain == 'extremetube':

            status = extremetube_status(link, proxies)

        elif domain == 'youporn':

            status = youporn_status(link, proxies)

        elif domain == 'redtube':

            status = redtube_status(link, proxies)

        elif domain == 'javynow':

            status = javynow_status(link, proxies)

        elif domain in 'spankbang':

            status = spankbang_status(link, proxies)

        else:
            status = 'dead'

        if status == 'alive':

            print(status,link, embedlink, domain, actress)
