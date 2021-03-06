import psycopg2
import datetime


def process2_database(link, embedlink, domain, actress, status, viewCount, herokuURI):
    try:

        date = datetime.date.today()

        conn = psycopg2.connect(herokuURI)
        cur = conn.cursor()

        cur.execute('insert into copy_content (domain,link,embedlink,actress,status,viewCount,create_date)\
        values (%s,%s,%s,%s,%s,%s,%s)', (domain, link, embedlink, actress, status, viewCount, date))
        conn.commit()
        cur.close()
        conn.close()
        print("insert database success")

    except Exception as e:
        print("database error", e)
