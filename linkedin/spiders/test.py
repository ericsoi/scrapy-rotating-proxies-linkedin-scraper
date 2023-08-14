import scrapy


class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["test.com"]
    start_urls = ["https://test.com"]

    def start_requests(self):
        yield scrapy.Request(url='http://httpbin.org/ip',  meta={"pyppeteer": True})
    def parse(self, response):
        print(response.ip_address)
        yield{
            "Origin Ip": str(response.ip_address),
            "User Agent": response.request.headers["User-Agent"]
        }
