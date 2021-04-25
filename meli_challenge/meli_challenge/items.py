import scrapy


class MeliChallengeItem(scrapy.Item):
    
    name = scrapy.Field()
    link = scrapy.Field()
