import scrapy
from spiders.items import SpidersItem
from scrapy.selector import Selector


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = f'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url = url, callback=self.parse, dont_filter=False)

    def parse(self, response):
        print(response.url)

        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]') #//dl[@class="movie-list"]
        for movie in movies[:10]:
            item = SpidersItem()
            m_name = movie.xpath('./div[1]/span[1]/text()')
            m_type = movie.xpath('./div[2]/text()')
            m_time = movie.xpath('./div[4]/text()')
            # print('------------------------------')
            # print(m_name.extract())
            # print(m_type.extract()[1].replace('\n', '').replace(' ', ''))
            # print(m_time.extract()[1].replace('\n', '').replace(' ', ''))
            # print('------------------------------')
            item['m_name'] = m_name.extract_first().strip()
            item['m_type'] = m_type.extract()[1].replace('\n', '').replace(' ', '')
            item['m_time'] = m_time.extract()[1].replace('\n', '').replace(' ', '')
            yield item