# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import mysql.connector


class QuotestutorialPipeline:

    """ def __init__(self):
        self.create_connection()
        self.create_table() """

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="eureka01",
            database="scrapyQuotes"
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes""")
        self.curr.execute(""" CREATE TABLE quotes(title text, author varchar(50), tag text)""")

    def process_item(self, item, spider):
        """ self.store_db(item) """
        return item
    
    def store_db(self, item):
        self.curr.execute("""INSERT INTO quotes values(%s,%s,%s)""", 
                         (item['title'], item['author'], ', '.join(item['tag'])))
        self.conn.commit()
