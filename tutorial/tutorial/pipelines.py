# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
from scrapy.exceptions import DropItem

class TutorialPipeline(object):

    def __init__(self, mysql_conn):
        self.mysql_conn = mysql_conn

    @classmethod
    def from_crawler(cls, crawler):
        return cls(MySQLdb.connect(host='172.17.0.2', user='root', db='bestbooks', charset='utf8'))

    def close_spider(self, spider):
        self.mysql_conn.commit()
        self.mysql_conn.close()

    def process_item(self, item, spider):
        if item['title'] is not None:
            cursor = self.mysql_conn.cursor()
            cursor.execute("SET NAMES utf8")
            cursor.execute(
                """INSERT INTO books (title, catalog, download_link, password, origin) VALUES (%s, %s, %s, %s, %s)""",
                (item['title'], item['catalog'], item['download_link'], item['password'], item['origin'],)
            )
            cursor.close()
            return item
        else:
            raise DropItem("Missing title")
