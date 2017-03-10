#encoding=utf-8
import pymongo
from Sina_spider1.items import InformationItem, TweetsItem, FollowsItem, FansItem, ContentItem

#JSON PIPELINE

import codecs
import json

class SoccerPipeline(object):
    def __init__(self):
        self.file = codecs.open(
        'scraped_data_utf8.json','w',encoding = 'utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item),ensure_ascii = False) + '\n'
        self.file.write(line)
        return item

    def spider_closed(self,spider):
        self.file.close()

#Mongodb pipelines
'''
class MongoDBPipleline(object):
    def __init__(self):
        clinet = pymongo.MongoClient("localhost", 27017)
        db = clinet["Sina"]
        #self.Information = db["Information"]
        #self.Tweets = db["Tweets"]
        #self.Follows = db["Follows"]
        #self.Fans = db["Fans"]
        self.Content = db["Content"]

    def process_item(self, item, spider):
        """ 判断item的类型，并作相应的处理，再入数据库 """
        """ After making sure the type of items, adding those items to database """
        if isinstance(item,ContentItem):
            try:
                self.Content.insert(dict(item))
            except Exception:
                pass
'''
'''
        if isinstance(item, InformationItem):
            try:
                self.Information.insert(dict(item))
            except Exception:
                pass
        elif isinstance(item, TweetsItem):
            try:
                self.Tweets.insert(dict(item))
            except Exception:
                pass
        elif isinstance(item, FollowsItem):
            followsItems = dict(item)
            follows = followsItems.pop("follows")
            for i in range(len(follows)):
                followsItems[str(i + 1)] = follows[i]
            try:
                self.Follows.insert(followsItems)
            except Exception:
                pass
        elif isinstance(item, FansItem):
            fansItems = dict(item)
            fans = fansItems.pop("fans")
            for i in range(len(fans)):
                fansItems[str(i + 1)] = fans[i]
            try:
                self.Fans.insert(fansItems)
            except Exception:
                pass
        return item
'''
