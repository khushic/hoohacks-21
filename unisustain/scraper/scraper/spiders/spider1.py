import scrapy

class EventsSpider(scrapy.Spider):
    name = 'events'

    def start_request(self):
        urls = ['https://waset.org/research-conferences']
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'events-%s.html'% page

        with open(filename, 'wb') as f:
            f.write(response.body)
            self.log('saved file %s' % filename)
