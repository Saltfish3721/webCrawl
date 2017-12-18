from bs4 import BeautifulSoup
import pymongo
import re
import collections

connection = pymongo.MongoClient('127.0.0.1',27017)
db = connection.yingdi
post = db.hsarticle

lists=post.find()
print(lists.count())
result={}
for i in range(lists.count()):
    if lists[i]['time'][2]=='月':
        #sad[i]['time']=re.findall('(\d{2})',sad[i]["time"])[0]+re.findall('(\d{2})',sad[i]["time"])[1]
        data=lists[i]['time'][0]+lists[i]['time'][1]+lists[i]['time'][3]+lists[i]['time'][4]
        if data not in result.keys():
            result[data]=0
        else:
            result[data]+=int(lists[i]["replyNum"])

order_result=collections.OrderedDict(sorted(result.items()))

with open("replycount.text",'w') as f:
    f.write(str(order_result))

print(order_result)
y=[]
for _,value in order_result.items():
    y.append(value)
print(y)
import numpy as np
import matplotlib.pyplot as plt

x =range(len(y))

plt.figure()
plt.plot(x, y)
plt.show()



