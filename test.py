 	
#coding:utf-8  
''''' 
@author: zhangpf
'''  
import requests
from bs4 import BeautifulSoup

import pokemon

# 这个是
allSimplePokemonInfoUrl = 'http://wiki.52poke.com/wiki/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%85%A8%E5%9B%BD%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89/%E7%AE%80%E5%8D%95%E7%89%88'

pokeMon = pokemon.PokemonParser(allSimplePokemonInfoUrl)

pokeMon.printName()

pokeMon.parserAllPokemon()

# file = open('./1.html', 'rb') 
# html = file.read() 
# bs = BeautifulSoup(html,"html.parser") # 缩进格式


# print(bs.prettify()) # 格式化html结构
# print(bs.title) # 获取title标签的名称
# print(bs.title.name) # 获取title标签的文本内容
# print(bs.title.string) # 获取head标签的所有内容
# print(bs.head) # 获取第一个div标签中的所有内容
# print(bs.div) # 获取第一个div标签的id的值
# print(bs.div["id"]) # 获取第一个a标签中的所有内容
# print(bs.a) # 获取所有的a标签中的所有内容
# print(bs.find_all("a")) # 获取id="u1"
# print(bs.find(id="u1")) # 获取所有的a标签，并遍历打印a标签中的href的值
# for item in bs.find_all("a"): 
#     print(item.get("href")) # 获取所有的a标签，并遍历打印a标签的文本值
# for item in bs.find_all("a"): 
#     print(item.get_text())


#res = requests.get('https://doc.qt.io/qt-5/qabstractaxis.html')

#r.text获取文本信息，通过r.content获取图片文件

# print(r.text)

# #获取网页编码

# print(r.encoding)

# #获取响应状态码

# print(r.status_code)

#bs = BeautifulSoup(res.text,"html.parser")

#print(bs.prettify())
#prettifyText = bs.prettify()

#print(prettifyText)

#bs1 = BeautifulSoup(prettifyText,"html.parser")


#uls = bs1.find_all('div', attrs={'class':'context'})


#print(uls[0])

#f = open("123.html",'w')

# htmlTite = "<!DOCTYPE html>"

#
# message = """
# <html>
# <head>
#     <meta content="text/html;charset=utf-8" http-equiv="content-type" />
# </head>
# <body>
# %s
# </body>
# </html>"""%(uls[0])


#f = open("1.html",'w')

#f.write(message)
#关闭文件
#f.close()

#print(message)