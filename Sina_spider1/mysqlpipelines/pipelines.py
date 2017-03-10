from .sql import Sql
from Sina_spider1.items import ContentItem

class WeiboItemsPipeline(object):

    def process_item(self,contentitem,spider):
        if isinstance(contentitem,ContentItem):
            comments_content = contentitem['comments_content']
            ret = Sql.select_name(comments_content)
            if ret[0]==1:
                print('已经存在了')
                pass
            else:
                comments_content = contentitem['comments_content']
                comments_times = contentitem['comments_times']
                comments_likes = contentitem['comments_likes']
                Sql.insert_comments(comments_content,comments_times,comments_likes)
                print('开始存档')