from urllib import request
import scrapy


class MangaSpider(scrapy.Spider):
    name = 'manga'
    start_urls = [
        'https://muitomanga.com/manga/solo-leveling',
        'https://muitomanga.com/manga/kaguya-sama-wa-kokurasetai-tensai-tachi-no-renai-zunousen'
    ]


    def parse(self, response):
        for item in response.css('.content'):
            yield {
                "manga": response.css('.subtitles_menus::text').get(),
                "chapters": [[x, item.css('.single-chapter small::attr(title)').getall()[i-1]] for i, x in enumerate(set(item.css('.single-chapter > a::text').getall()))], 
            }
            

