import scrapy
from ..items import QuotestutorialItem
from scrapy.http import FormRequest

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/login']


    def parse(self, response):
        token = response.css('form input::attr(value)').get()
        return FormRequest.from_response(response, formdata={
            'csrf_token' : token,
            'username':'teste@gmail.com',
            'password': 'teste'
        }, callback=self.start_scraping)

    def start_scraping(self, response):
        all_div_quotes = response.css('div.quote')
        items = QuotestutorialItem()

        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').get()
            author = quotes.css('.author::text').get()
            tag = quotes.css('.tag::text').getall()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items
        
        next_page = response.css('.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.start_scraping)
