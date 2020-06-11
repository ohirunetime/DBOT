import psycopg2
from process2_sub import domain_check

# 環境変数
import configparser
config = configparser.ConfigParser()
config.read('../setting.ini')
section = 'development'
proxies = config.get(section, 'proxies')

LocalDatabaseURI = config.get(section, 'LocalDatabaseURI')

herokuURI = config.get(section, 'herokuURI')

print(proxies)


kensaku = input("女優名を入力 : ")


def main():
    rows = get_process1()
    domain_check(rows, proxies, herokuURI)


def get_process1():
    conn = psycopg2.connect(LocalDatabaseURI)
    try:
        cur = conn.cursor()
        sql = 'select distinct(link) , embedlink , domain , actress from process1 where actress = %s '
        cur.execute(sql, (kensaku,))
        rows = cur.fetchall()
        print(rows)
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(e)

    return rows


main()
