from selenium import webdriver
import time

url='http://www.iyingdi.cn/web/article/hearthstone?seed=2'

driver = webdriver.Chrome(executable_path='/Users/apple/Downloads/chromedriver')
driver.get(url)
time.sleep(5)


for i in range(100):
    js = "var q=document.documentElement.scrollTop=8800000"
    driver.execute_script(js)
    time.sleep(1)

html=driver.page_source
with open('yingdi/head_page_all.txt','w',encoding='utf-8') as f:
    f.write(html)


'''import pymysql

db = pymysql.connect("localhost",'root','',"test1")
cursor = db.cursor()

sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

db.close()'''