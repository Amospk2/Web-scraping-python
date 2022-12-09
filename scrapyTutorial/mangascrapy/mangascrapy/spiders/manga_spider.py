from gc import callbacks
import scrapy
from ..items import MangascrapyItem



class MangaSpider(scrapy.Spider):
    name = "manga"
    start_urls = [
        'https://mangalivre.net/series/index/nota?page=1'
    ]
    page_navitation = 1

    def parse(self, response, **kwargs):
        items = MangascrapyItem()
        touchcarousel = response.css(".touchcarousel")
        for container in touchcarousel:
            author = container.css('.series-author::text').getall()[0].split(' ')
            author = (''.join([author_name for author_name in author if author_name not in ['', '\n']]))
            items['title'] = container.css('h1::text').get()
            items['author'] = author
            items['rate'] = container.css('.rating .button .nota::text').get()
            items['tags'] = container.css(".touch-carousel-item+ .touch-carousel-item .button .nota::text").getall()
            yield items
        
        self.page_navitation += 1
        next_page = f"https://mangalivre.net/series/index/nota?page={self.page_navitation}"

        if self.page_navitation <= 5:
            yield response.follow(next_page, callback=self.parse)



            



    