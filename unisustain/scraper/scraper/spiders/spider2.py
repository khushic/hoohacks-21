import scrapy

class GrantsSpider(scrapy.Spider):
    name = 'grants'

    def start_request(self):
        urls = ['https://www.nsf.gov/crssprgm/reu/reu_search.jsp']
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'grants-%s.html'% page

        with open(filename, 'wb') as f:
            f.write(response.body)
            self.log('saved file %s' % filename)
