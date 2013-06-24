from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request
from camwar.items import CamwarItem
import urlparse

class CamwarSpider(BaseSpider):
    name = "camwar"
    allowed_domains = ["atenlabs.com"]
    start_urls = [
        "http://www.atenlabs.com/camwar/index.php?action=topcams"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        cams = hxs.select('//a[contains(@href, "http")]/img/@src').extract()
        
        for cam in cams:
            item = CamwarItem()
            item['url'] = cam
            yield item

        for url in hxs.select('//a[contains(@href, "offset")]/@href').extract():
            yield Request(urlparse.urljoin(response.url, url), callback=self.parse)