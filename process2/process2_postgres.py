import psycopg2
import datetime


def process2_database(link, embedlink, domain, actress, status, LocalDatabaseURI):
    try:

        date = datetime.date.today()

        conn = psycopg2.connect(LocalDatabaseURI)
        cur = conn.cursor()

        cur.execute('insert into copy_link (domain,link,embedlink,actress,status,create_date)\
        values (%s,%s,%s,%s,%s,%s)', (domain, link, embedlink, actress, status, date))
        conn.commit()
        cur.close()
        conn.close()
        print("insert database success")

    except Exception as e:
        print("database error", e)
