import scrapy
from doubanMovie250.items import Doubanmovie250Item


class DoubanMovie250Spider(scrapy.Spider):
    name = 'doubanMovie250'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }

# 使用start_requests函数而不是start_urls = ['https://movie.douban.com/top250']，对初始URL的处理有更多权利，比如给初始URL增加请求头User-Agent
    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        item = Doubanmovie250Item()
        movies = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            item['ranking'] = movie.xpath('.//div[@class="pic"]/em/text()').extract()[0]
            item['title'] = movie.xpath('.//div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['score'] = movie.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            item['quote'] = movie.xpath('.//p[@class="quote"]/span/text()').extract()
            yield item
            next_url = response.xpath('//span[@class="next"]/a/@href').extract()
            if next_url:
                next_url = 'https://movie.douban.com/top250' + next_url[0]
                yield scrapy.Request(next_url, headers=self.headers)
