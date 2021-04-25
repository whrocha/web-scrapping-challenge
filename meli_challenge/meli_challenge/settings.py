BOT_NAME = 'meli_challenge'

SPIDER_MODULES = ['meli_challenge.spiders']
NEWSPIDER_MODULE = 'meli_challenge.spiders'

ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 64

DOWNLOAD_DELAY = 1

COOKIES_ENABLED = False

ITEM_PIPELINES = {
   'meli_challenge.pipelines.MeliChallengePipeline': 200,
}
