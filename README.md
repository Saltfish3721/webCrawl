目标：使用selenium爬去旅法师营地文章的基本信息和评论，作为数据分析的来源。

爬去单个网页的完整代码：参考 get_whole_html.py

##网页分析：
打开任意营地文章的网页，并尝试用requests获取，可以发现营地的网页是动态加载的，requests后者urllib并不能爬去网页，这时，可以使用selenium。

##环境配置
selenium
任意一种浏览器驱动，本文采取的是 chromedriver

##代码分析

    from selenium import webdriver
    import time
    driver = webdriver.Chrome(executable_path='/Users/apple/Downloads/chromedriver')
    
 直接运行这段代码，会发现脚本帮我们打开了一个Chorme浏览器。
 
     driver.get(url)
     time.sleep(10)
     
 将一个url传进去，浏览器就会打开对应网页，并选择让程序暂停10秒，等待网页加载完成。当然，selenium有内置的方法来等待网页加载完成，但我目前还没有看懂。