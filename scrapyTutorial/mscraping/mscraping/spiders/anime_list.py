from urllib.request import Request
import scrapy


class BricksetSpider(scrapy.Spider):
    name = 'anime_list'
    
    def start_requests(self):
        yield scrapy.Request('https://myanimelist.net/topanime.php?limit=0', callback=self.parse)
        
    def parse(self, response):
        for animes in response.css('.detail'):
            yield{
                'name': animes.css('.detail a::text').get(),
            }

        for animes in response.css('.score'):
            yield{
                'score': animes.css('.score span::text').get(),
            }
        
        NEXT_PAGE_SELECTOR = '.next::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()

        if next_page != '?limit=200':
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
            