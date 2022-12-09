# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# Scraped data - > Items Containers -> Storing in database
# Scraped data - > Items Containers -> Pipeline -> Storing in database
from turtle import title
import scrapy


class QuotestutorialItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()
    
    

