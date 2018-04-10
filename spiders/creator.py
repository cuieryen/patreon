import scrapy
from scrapy_splash import SplashRequest

class PatreonSpider(scrapy.Spider):
    name = "drawing"

    def start_requests(self):
        urls = [
            'https://www.patreon.com/search?q=drawing&t=creators&p=1'
        ]
        for url in urls:
            yield SplashRequest(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'drawing-1.html'
        links = response.css('div.s1mdim3j-0.kvPNQP > a.i4g0lx-0.kpKNya::attr(href)').extract()
        for link in links:
            yield SplashRequest(url=link, callback=self.parse_creator, args={'wait': 3.0})

    def parse_creator(self, response):
        num_patron = response.css('div.s1mdim3j-0.gNbSQm > h6.ipucgz-9.hOjVwZ::text').extract()
        per_patron = response.css('div.s1mdim3j-0.injlmc > h6.ipucgz-9.hOjVwZ::text').extract()
        unit = response.css('div.s1mdim3j-0.injlmc  span.ipucgz-1.fUKvjD::text').extract()
        print("here " + response.url)
        print(num_patron)
        print(per_patron)
        print(unit)






        #with open(filename, 'wb') as f:
        #    f.write(response.body)
        #self.log('Saved file %s' % filename)
