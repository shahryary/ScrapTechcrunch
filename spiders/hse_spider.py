# created file by yadollah Shahryary

from scrapy.spiders import BaseSpider
from scrapy.http import Request
from scraphse.items import ScraphseItem
from datetime import datetime
from bs4 import BeautifulSoup


class hse_spider(BaseSpider):
    name = 'hse'
    allowed_domains = ['techcrunch.com']

    def start_requests(self):
        # for debugging, crawl just 3 page
        # you can set calue for how many pages you want!
        # yield self.make_requests_from_url("http://techcrunch.com/page/2/")
        for num in range(1, 4):
            yield self.make_requests_from_url("http://techcrunch.com/page/%d/" % num)

    def parse(self, response):
        links = response.selector.xpath("//a[starts-with(@data-omni-sm, 'gbl_river_headline')]/@href")
        for link in links:
            yield Request(link.extract(), callback=self.parse_article)
        return

    def parse_article(self, response):
        item = ScraphseItem()
        item['author'] = response.selector.xpath("//*[contains(@rel, 'author')]/text()").extract()[0]
        item['headLine'] = response.selector.xpath("//h1[@class='alpha tweet-title']/text()").extract()[0]
        item['postTime'] = response.selector.xpath("//meta[@name='sailthru.date']").extract()[0][36:-2]
        item['postTags'] = response.selector.xpath("//meta[@name='sailthru.tags']").extract()[0][36:-2]
        rawBody = response.selector.xpath("//*[@class='article-entry text']").extract()[0]
        soup = BeautifulSoup(rawBody)
        [s.extract() for s in soup('script')]
        item['postText'] = soup.get_text()
        item['postsByLink'] = str(response.request.url)
        item['dlTimestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S %z")

        return item
