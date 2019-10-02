# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanmoviePipeline(object):
    def process_item(self, item, spider):
        str = item['name'] + '\t' + item['url'] + '\t' + item['rating']
        print(str)  # 这里只做简单的输出，也可将其存入文件或者数据库等
        return item
