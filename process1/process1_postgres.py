import psycopg2
import datetime


def InsertDatabase(link, embedlink,domain, actress, LocalDatabaseURI):
    try:
        conn = psycopg2.connect(LocalDatabaseURI)
        cur = conn.cursor()

        cur.execute('insert into process1 (domain,link,embedlink,actress)\
        values (%s,%s,%s,%s)', (domain, link, embedlink, actress))
        conn.commit()
        cur.close()
        conn.close()
        print("insert database success")

    except Exception as e:
        print("database error", e)
