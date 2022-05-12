from pymongo import MongoClient
from pymongo.cursor import CursorType
import requests
from bs4 import BeautifulSoup

mongo = MongoClient("localhost", 20000)


def mongo_save(mongo, datas, db_name=None, collection_name=None):
    result = mongo[db_name][collection_name].insert_many(datas).inserted_ids
    return result


navers = []
aid = 0
sid = 100

status_count = 0
for x in range(1, 21):
    try:

        num_str = str(aid)
        html = requests.get(
            f"https://n.news.naver.com/mnews/article/005/{num_str.zfill(10)}?sid={sid}")
        soup = BeautifulSoup(html.text, 'html.parser')
        time_el = soup.select_one(
            ".media_end_head_info_datestamp_bunch span")
        title_el = soup.select_one(
            ".media_end_head_headline")
        company_el = soup.select_one(
            ".media_end_linked_more_point")

        aid = aid+1

        if(html.status_code == 200):
            dict = {"date": time_el.get_text(), "title": title_el.get_text(),
                    "company": company_el.get_text()}
            navers.append(dict)
            print(title_el.get_text())

    except Exception as e:
        pass


mongo_save(mongo, navers, "greendb", "navers")
