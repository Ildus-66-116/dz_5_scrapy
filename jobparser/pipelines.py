# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from pymongo import MongoClient
import json
from random import randint


class JobparserPipeline:
    def __init__(self):
        self.fantasy = []

    def process_item(self, item, spider):
        try:
            id_int = int(item['_id'].split(': ')[1])
            item['_id'] = id_int
        except:
            item['_id'] = randint(1000000, 9999999)

        try:
            name_str = str(item['name'].split(': ')[1])
            item['name'] = name_str
        except:
            item['name'] = None

        try:
            item['price'] = int(item['price'])
        except:
            item['price'] = None

        try:
            num_pag_str = str(item['number_of_pages'].split(': ')[1])
            num_pag = int(num_pag_str.split(' ')[0])
            item['number_of_pages'] = num_pag
        except:
            item['number_of_pages'] = None

        item_dict = dict(item)
        self.fantasy.append(item_dict)
        return item

    def close_spider(self, spider):
        with open(f'{spider.name}.json', 'w', encoding='utf-8') as file:
            json.dump(self.fantasy, file)

