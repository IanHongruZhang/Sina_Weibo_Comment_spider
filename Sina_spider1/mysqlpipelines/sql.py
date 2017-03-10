import mysql.connector
from Sina_spider1 import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = mysql.connector.connect(user = MYSQL_USER,password = MYSQL_PASSWORD,host = MYSQL_HOSTS, database = MYSQL_DB)
cur = cnx.cursor(buffered = True)

class Sql:

    @classmethod
    def insert_comments(cls,comments_content,comments_time,comments_like):
        sql = 'INSERT INTO comments (`comments_content`,`comments_time`,`comments_like`) VALUES (%(comments_content)s,%(comments_time)s,%(comments_like)s)'
        value = {'comments_content':comments_content,
                 'comments_time':comments_time,
                 'comments_like':comments_like,
                 }
        cur.execute(sql,value)
        cnx.commit()

#去重
    @classmethod
    def select_name(cls,comments_content):
        sql = "SELECT EXISTS(SELECT 1 FROM comments WHERE comments_content = %(comments_content)s)"
        value = {
            'comments_content':comments_content
        }
        cur.execute(sql,value)
        return cur.fetchall()[0]