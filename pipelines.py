
# created file by yadollah Shahryary

import psycopg2

from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.utils.project import get_project_settings
from twisted.enterprise import adbapi
from scraphse.processors import PostTimeEst

SETTINGS = get_project_settings()


class hsePipeline(object):

    """""
        Passing scrapy container items into a PostgreSQL database.
        Assume the db is already created.
    """""
    def __init__(self):
        self.postTimeEst = PostTimeEst()
        self.isql = "INSERT INTO homePage(title, author, postTime, postsByLink, postTags, postText, dlTimestamp)" \
                    " VALUES (%s, %s, %s, %s, %s, %s, %s)"
        dispatcher.connect(self.spider_opened, signals.spider_opened)

    # make db connection as soon as spider is open
    def spider_opened(self, spider):
        self.dbpool = adbapi.ConnectionPool("psycopg2",
                                            host=SETTINGS['DB_HOST'],
                                            port=SETTINGS['DB_PORT'],
                                            database=SETTINGS['DB_DB'],
                                            user=SETTINGS['DB_USER'],
                                            password=SETTINGS['DB_PASSWD'],
                                            cp_min=3,
                                            cp_max = 10,
                                            cp_noisy =True ,
                                            cp_reconnect =True ,
                                            cp_good_sql="SELECT 1"
                                            )

    def spider_closed(self, spider):
        pass

    def process_item(self, item, spider):
        input = self.dbpool.runInteraction(self.postgreSQL_Query, item)
        input.addErrback(self.handle_error, item)

    def postgreSQL_Query(self, tx, item):

        itemDict = dict(item)
        title = itemDict['headLine']
        author = itemDict['author']
        postTime = itemDict['postTime']
        postsByLink = itemDict['postsByLink']
        postTags = itemDict['postTags']
        postText = itemDict['postText']
        dlTimestamp = itemDict['dlTimestamp']

        tx.execute(self.isql,(title, author, postTime, postsByLink,postTags,postText, dlTimestamp))

    def handle_error(self, e, item):
        print (e)
