from bs4 import BeautifulSoup
import pymongo
import re

connection = pymongo.MongoClient('127.0.0.1',27017)
db = connection.yingdi
post = db.hsarticle


'''with open('yingdi/head_page_all.txt',mode='r') as f:
    prettyhtml=BeautifulSoup(f,'lxml').prettify()
    with open('yingdi/prettyhead.txt',mode='w') as h:
        h.write(prettyhtml)'''

post.remove({})

with open('yingdi/head_page_all.txt',mode='r') as f:

    prettyhtml=BeautifulSoup(f,'lxml')
    feed_lists=prettyhtml.find('ul',class_='feeds-list-ul')

    normal_lists=feed_lists.findAll('li',class_='articleFeedItem-normalStyle')
    for li in normal_lists:
        title=li.find('span',class_='articleFeedItem-feedTitle').find('a').text
        long_url=li.find('span',class_='articleFeedItem-feedTitle').find('a').attrs['href']
        id_article=re.findall('(\d{5})',long_url)[0]
        try:
            author=li.find('span',class_='articleFeedItem-authorName').text
        except: print('loss one name')
        replyNum=li.find('span',class_='articleFeedItem-replyNum').text
        time=li.find('span',class_='articleFeedItem-timeCreate').text
        data={'title':title,'author':author,'replyNum':replyNum,'time':time,'id':id_article}
        #print(data)
        post.insert(data)

    double_lists = feed_lists.findAll('li', class_='articleFeedItem-doubleStyle')
    for li in normal_lists:
        title=li.find('div',class_='articleFeedItem-footer').find('div').text
        long_url=li.find('a').attrs['href']
        id_article=re.findall('(\d{5})',long_url)[0]
        author='None'
        replyNum=li.find('span',class_='articleFeedItem-replyNum').text
        time='None'
        data={'title':title,'author':author,'replyNum':replyNum,'time':time,'id':id_article}
        #print(data)
        post.insert(data)
