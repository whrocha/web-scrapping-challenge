import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.item import Item, Field


class PageContentItem(Item):

    url = Field()
    prev_url = Field()
    content = Field()

class LinkCrawler(CrawlSpider):

    name = 'LinkCrawler'

    start_urls = [
        'http://www.example.com/',
    ]

    rules = (
        # Extract link from this path only
        Rule(
            LxmlLinkExtractor(
                allow=r'^(http|https)://',
            ), 
            callback='parse_page', 
            follow=True # this will continue crawling through the previously extracted links
        ),
    )

    custom_settings = {
        'DEPTH_LIMIT': '2',
    }

    def parse_page(self, response):

        item = PageContentItem()
        item['url'] = response.url
        item['content'] = response.text
        item['prev_url'] = None
        
        if response.request.headers.get('Referer') is not None:

            item['prev_url'] = response.request.headers.get('Referer').decode('utf-8')

        yield item