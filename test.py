import requests
from bs4 import BeautifulSoup

url = ('http://music.163.com/#/artist?id=13193')
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
url_a = requests.get(url = url,headers = header)
# print(url_a.status_code,url_a.text)


soup = BeautifulSoup(url_a.text,'lxml') #声明beautifulsoup 对象
print(soup.title) #查找title标签
print(soup.a)     #查找第一个a标签

#对标签的直接子节点进行循环
title_tag = soup.li
for child in title_tag.children:
    print(child)

soup.parent #父节点

#所有父节点
link = soup.a
for parent in link.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)


#兄弟节点
# sibling_soup.b.next_sibling #后面的兄弟节点
# sibling_soup.c.previous_sibling #前面的兄弟节点

#所有兄弟节点
# for sibling in soup.a.next_siblings:
#     print(repr(sibling))

# for sibling in soup.find(id="link3").previous_sibling:
#     print(repr(sibling))
