# -*- coding: utf-8 -*-
import scrapy

from doubanmovie.items import DoubanmovieItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['duoban.com']
    start_urls = ['https://movie.douban.com/chart']

    def parse(self, response):
        movies = response.xpath('//tr[@class="item"]')
        for movie_item in movies:
            item = DoubanmovieItem()
            item['name'] = movie_item.xpath('.//a[@class="nbg"]/img/@alt').extract_first()
            item['url'] = movie_item.xpath('.//a/@href').extract_first()
            item['rating'] = movie_item.xpath('.//span[@class="rating_nums"]/text()').extract_first()
            yield item
        pass
