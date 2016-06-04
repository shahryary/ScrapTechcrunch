# -*- coding: utf-8 -*-
# created file by yadollah Shahryary

BOT_NAME = 'scraphse'

SPIDER_MODULES = ['scraphse.spiders']
NEWSPIDER_MODULE = 'scraphse.spiders'


DOWNLOAD_DELAY = 3

PATH_DEBUG = True
PATH_DEBUG_URL_LENGTH = 95
ITEM_PIPELINES = ['scraphse.pipelines.hsePipeline']
CONCURRENT_ITEMS = 100
CONCURRENT_REQUESTS = 1
CONCURRENT_REQUESTS_PER_DOMAIN = 8
CONCURRENT_REQUESTS_PER_IP = 0

DOWNLOADER_STATS = True
RANDOMIZE_DOWNLOAD_DELAY = True

# Data base Settings
DB_HOST = 'mbpsql.cbeodvh2mxmc.us-west-2.rds.amazonaws.com'
DB_PORT = 5432
DB_USER = 'postgres'
DB_PASSWD = 'Vt3hq7Sk'
DB_DB = 'yashakhriaridizazhi'
cp_min = 3
cp_max = 10
cp_noisy = True
cp_reconnect = True

