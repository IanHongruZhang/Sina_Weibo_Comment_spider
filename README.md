# Sina_Weibo_Comment_spider

### 这个爬虫所需要的环境/ Environment
* Anaconda 4.3

* Pycharm as IDE, Python 3.5.2 or 3.6

* Scrapy 1.3, you could setup it by pip install Scrapy == 1.3

### 执行begin.py 则可以开始挖掘

### 怎么使用？
1.在spider.py的id池里换上你要爬的用户（和3要一起改，就是步骤3里url的那串数字）
![挖掘id池](http://p1.bpimg.com/4851/5d530e26aab3c496.png)
2.在cookies.py里换上你的号子和密码（反正我不用微博，四个僵尸粉号子就放这里吧）
![账号密码](http://p1.bpimg.com/4851/9d0aba21116c7c89.png)
3.想爬哪条微博，在这里改数据(注意此微博的入口是weibo.cn,wap端微博，所以找需要的数据得从weibo.cn里面找)
![改数据](http://p1.bpimg.com/4851/e80a8f759cd8043d.png)
4.执行begin.py
5.此爬虫支持mysql,mongodb,以及直接导出JSON格式，在pipeline和settings里面改。。。
6.这个版本现在默认是导出JSON
