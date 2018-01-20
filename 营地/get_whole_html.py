from selenium import webdriver
import time

def load_(url):
    driver = webdriver.Chrome(executable_path='/Users/apple/Downloads/chromedriver')
    driver.get(url)
    time.sleep(10)

    moreComments = driver.find_element_by_class_name('toCheckMoreComment')
    while moreComments!= None:
        moreComments.click()
        time.sleep(3)
        try:
            moreComments = driver.find_element_by_class_name('toCheckMoreComment')
        except:
            moreComments=None
            
    time.sleep(1)
    elem = driver.find_element_by_class_name('checkMoreReplyComment')
    while elem !=None:
        elem.click()
        time.sleep(0.5)
        try:
            elem= driver.find_element_by_class_name('checkMoreReplyComment')
        except:
            elem=None
    #driver.close()
    return driver.page_source


if __name__=='__main__':
    url='http://www.iyingdi.cn/web/article/hearthstone/49439?title=%E6%80%9D%E8%80%83%E4%B8%8E%E6%80%BB%E7' \
        '%BB%93%20%E5%AE%9E%E6%88%98%E5%88%9D%E7%BA%A7%E5%A4%8D%E7%9B%98'

    html=load_(url)
    
    with open('ydhtml.txt','w') as f:
        f.write(html)
