# Scrapy settings for camwar project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'camwar'

SPIDER_MODULES = ['camwar.spiders']
NEWSPIDER_MODULE = 'camwar.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'camwar (+http://www.yourdomain.com)'

ITEM_PIPELINES = ['camwar.pipelines.CamwarPipeline',]