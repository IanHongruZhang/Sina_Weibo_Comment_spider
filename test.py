from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup

a = '<input name="mp" type="hidden" value="2">'
print(a[-3])
page = requests.get("http://weibo.cn/comment/EdxaoxBxG?uid=1985757342rl=0&page2&page=2")
j = BeautifulSoup(page.text,'lxml')
print(j)

http://weibo.cn/comment/DwSG4vwxl?uid=1985757342rl=0&page=1
http://weibo.cn/comment/DzgxPoRL7?uid=1985757342rl=0&page2