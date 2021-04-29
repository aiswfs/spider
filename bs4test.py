from bs4 import BeautifulSoup
html_doc = html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" id="sc"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

#Tag:查找标签
soup = BeautifulSoup(html_doc,'lxml') #声明beautifulsoup 对象
find = soup.find('p') #find方法，查找到第一个p标签/find_all 返回一个可迭代对象合集
print("find's return type is ",type(find))
print("find's content is ,", find)
print("find's Tag Name is ",find.name)
print("find's attribute(class) is ",find['class']) #输出class值

#NavigableString ：获取便签中的文本内容（不包括标签）
print("NavigableString is : ",find.string)

#BeautifulSoup： BeautifulSoup对象表示一个文档的全部内容。支持遍历文档树和搜索文档树

#Comment:该对象就是html和xml中的注释
# markup = "<b><!--Hey,buddy.Want to buy a user parser?--></b>"
# soup = BeautifulSoup(markup)
# comment = soup.b.string
# print(comment)
# print(type(comment))

print(soup.title) #查找title标签
print(soup.a)     #查找第一个a标签

#对标签的直接子节点进行循环
# title_tag = soup.li
# for child in title_tag.children:
#     print(child)


# #兄弟节点
# sibling_soup.b.next_sibling #后面的兄弟节点
# sibling_soup.c.previous_sibling #前面的兄弟节点

#所有兄弟节点
for sibling in soup.a.next_siblings:
    print(repr(sibling))

for sibling in soup.find(id="link3").previous_sibling:
    print(repr(sibling))



#find_all :find_all(name,attrs,recursive,sting,**kwargs)
# name 参数：可以查找所有名字为 name 的tag。
# attr 参数：就是tag里的属性。
# string 参数：搜索文档中字符串的内容。
# recursive 参数： 调用tag的 find_all() 方法时，Beautiful Soup会检索当前tag的所有子孙节点。如果只想搜索tag的直接子节点，可以使用参数 recursive=False 。


soup.find_all("title")
# [<title>The Dormouse's story</title>]
#
soup.find_all("p", "title")
# [<p class="title"><b>The Dormouse's story</b></p>]
# 
soup.find_all("a")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
#
soup.find_all(id="link2")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
#
import re
soup.find(string=re.compile("sisters"))
# u'Once upon a time there were three little sisters; and their names were\n'

# find()
# 与find_all()类似，只不过只返回找到的第一个值。返回值类型是bs4.element.Tag。
# 完整语法：
# find( name , attrs , recursive , string , **kwargs )
# 比如

print(soup.find('title'))
# <title>The Dormouse's story</title>
#
print(soup.find("head").find("title"))
# <title>The Dormouse's story</title>
