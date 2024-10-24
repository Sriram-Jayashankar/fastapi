import psycopg2
import time

def connecttodb():
    while(True):
        try:
            conn=psycopg2.connect("dbname=fastapiDatabase user=postgres password=builafisory")
            break
        except Exception as e:
            print(f"error while connecting\n{e}")
        time.sleep(5)
    cursor=conn.cursor()
    return (conn,cursor)