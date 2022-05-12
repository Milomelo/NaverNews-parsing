import requests
from bs4 import BeautifulSoup

aid = 1
sid = 100

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


print(time_el.get_text())


print(title_el.get_text())

print(company_el.get_text())
