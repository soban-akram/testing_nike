# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
from time import gmtime, strftime
from scrapy.conf import settings
con = None

class NikePipeline(object):

    def __init__(self):
        self.setupDBCon()

    def setupDBCon(self):
        self.con = sqlite3.connect(settings['DB_PATH'])
        self.cur = self.con.cursor()

    def closeDB(self):
        self.con.close()
        
    def __del__(self):
        self.closeDB()

    def process_item(self, item, spider):       
        self.storeInDb(item)
        return item


    def storeInDb(self,item):
        try:
            timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            self.cur.execute("INSERT INTO scraped_products(company, name, style_code, price, gender, category, sub_category, image_url, product_url, created_at, updated_at) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
                ('Nike', item['name'], item['code'], item['price'], item['gender'], item['category'], item['sub_category'], item['image'], item['product_url'], timestamp, timestamp))
            print '------------------------'
            print 'Data Stored in Database'
            print '------------------------'
            self.con.commit() 
        except Exception, e:
            print str(e)
