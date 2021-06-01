from lxml import etree

text = '''
<div>
<ul>
<li class = 'item-0'><a href = "link1.html">frist item</a></li>
<li class = 'item-1'><a href = "link2.html">second item</a></li>
<li class = 'item-inactive'><a href = "link3.html">third item</a></li>
<li class = 'item-1'><a href = "link4.html">fourth item</a></li>
<li class = 'item-0'><a href = "link5.html">fifth item</a>
</ul>
</div>
'''
# html = etree.HTML(text)
# resutl = etree.tostring(html)  # tostring 方法用于修正html代码，注意 tostring 方法后的结果是 bytes 类型，需要decode转换为 str
# print(resutl.decode('utf-8'))
#
# html = etree.parse('./text.html',etree.HTMLParser())
# result = etree.tostring(html)
# print(result.decode('utf-8'))

"""
所有节点
一般使用 // 开头的Xpath 来选取所有符合规则的节点，同时，xpath方法返回的都为列表，可以通过索引获取元素
"""
html = etree.parse('./text.html',etree.HTMLParser())
result = html.xpath('//*') # 选取所有节点  返回列表
print(result)

result2 = html.xpath('// a') #选取 所有 a 节点
print('result2',result2)
print('result2[0]',result2[0])
result3 = html.xpath('// li') #选取 所有 li 节点
print('result3',result3)

"""
子节点
通过 / 或者 // 来查找子元素 
/ 用来获取子节点
// 用来获取所有子孙节点
"""
result4 = html.xpath('//li/a') #获取所有li下的子节点 a  子节点
print('result4',result4)

result5 = html.xpath('//ul//a')  # 获取子孙节点， 及ul 下的孙子节点
print('result5',result5)

"""
父节点
通过子节点来查找父节点的方法
通过 .. 来实现（类比文件的相对位置路径的写法）
也可以通过 paretn:: 来获取父节点
"""
html = etree.parse('./text.html',etree.HTMLParser())
result6 = html.xpath('//a[@href="link4.html"]/..')   #通过子节点的属性获取到父节点
print('result6',result6)
result7 = html.xpath('//a[@href="link4.html"]/../@class') #获取到父节点的属性
print('result7',result7)
result8 = html.xpath('//a[@href="link4.html"]/parent::*/@class') #获取到父节点的属性
print('result8',result8)


"""
属性匹配
用 @ 符号过滤属性
"""
result9 = html.xpath('//li[@class = "item-inactive"]')  #通过匹配 item-inactive 这个class 属性，来找到这个li
print('result9',result9)


"""
文本获取
使用text()方法来获取节点中的文本
"""
result10 = html.xpath('//li[@class="item-0"]/text()')
print('result10',result10)  #获得的结果为 [] 为什么？

result11 = html.xpath('//li[@class="item-0"]/a/text()')  #该方法使用的为逐层选取的方法 即 // -> / 父节点到子节点的层层递进的方法
print('result11',result11)

result12 = html.xpath('//li[@class="item-0"]//text()')   #该方法通过 // 直接访问到孙子节点 a 中的文本
print('result12',result12)


"""
属性值获取
通过@ 就可以获取到属性值 
"""
result13 = html.xpath('//li/a/@href')   #通过 @ 符号获取属性值
print('result13',result13)

result14 = html.xpath('//li/@class')   #通过 @ 符号获取属性值
print('result14',result14)

"""
属性值多匹配
使用contains()函数来获取特定的属性值
"""
text = '''
<li class='li li-first'><a href='link.html'>first item</a></li>
'''
html = etree.HTML(text)
result15 = html.xpath('//li[@class="li"]/a/text()')
print('result15',result15) #获取到的值为空 是因为该节点拥有 li li-first 两个属性，使用 li 一个属性无法定位到该节点

result16 = html.xpath('//li[contains(@class,"li")]/a/text()') #使用contains()方法会匹配还有li的属性，只要该节点含有li的属性，就能匹配
print('result16',result16)

"""
多属性值匹配
即多个属性确定一个节点的情况下
也可以使用contains来确定节点
"""
text = '''
<li class='li li-first' name = 'name'><a href='link.html'>first item</a></li>
'''
html = etree.HTML(text)
result17 = html.xpath('//li[contains(@class,"li") and @name = "name"]/a/text()')  #多个属性匹配节点
print('result17',result17)
"""
按序选择
当属性匹配了多个节点是，但是只需要其中一个节点时候，就可以利用中括号传入索引的方法来获取想要的节点
"""
text = '''
<div>
<ul>
<li class = 'item-0'><a href = "link1.html"><span>frist item</span></a></li>
<li class = 'item-1'><a href = "link2.html">second item</a></li>
<li class = 'item-inactive'><a href = "link3.html">third item</a></li>
<li class = 'item-1'><a href = "link4.html">fourth item</a></li>
<li class = 'item-0'><a href = "link5.html">fifth item</a>
</ul>
</div>
'''
html = etree.HTML(text)
result18 = html.xpath('//li[1]/a/text()') #注意，这里的序号是从 1 开始 而非 0
print('result18',result18)

result19 = html.xpath('//li[last()]/a/text()') # last()方法，即选取最后一个
print('result19',result19)

result20 = html.xpath('//li[position()<=3]/a/text()') # position()方法，选定一个位置
print('result20',result20)

result21 = html.xpath('//li[last()-2]/a/text()') # last()-2方法，即选取从最后一个开始的往前两个
print('result21',result21)


"""
节点轴选择
获取子元素，兄弟元素，父元素，祖先元素等
"""
result22 = html.xpath('//li[1]/ancestor::*') #获取到了li[1]的所有 祖先元素
print('result22',result22)


result23 = html.xpath('//li[1]/ancestor::div') #获取到了li[1]的所祖先元素 div
print('result23',result23)

result24 = html.xpath('//li[1]/attribute::*') #获取到了li[1]的所有属性，因为attribute后面跟的*号
print('result24',result24)

result25 = html.xpath('//li[1]/child::a[@href="link1.html"]') #获取到了li[1]子节点的属性值为 link1.html 的子节点 a
print('result25',result25)

result26 = html.xpath('//li[1]/descendant::span') #获取到了li[1]所有的子孙节点且限定条件为span节点
print('result26',result26)

result27 = html.xpath('//li[1]/following-sibling::*') #获取到了li[1]的所有的兄弟节点 （兄弟节点即为 同父节点的节点）
print('result27',result27)