# -*- coding: utf-8 -*-
# created file by yadollah Shahryary

from scrapy.item import Item, Field


class ScraphseItem(Item):

    author = Field()
    postsByLink = Field()
    postTime = Field()
    headLine = Field()
    headLineLink = Field()
    dlTimestamp = Field()
    postTags = Field()
    postText = Field()
