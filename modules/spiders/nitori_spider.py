# -*- coding: utf-8 -*-
import scrapy


class NitoriSpider(scrapy.Spider):
    name = 'nitorispider'

    start_urls = ['https://www.nitori-net.jp/store/ja/ec/']

    def parse(self, response):
        for url in response.css('ul > li > a::attr("href")').extract():
            yield scrapy.Request(response.urljoin(url), self.parse_products)

    def parse_products(self, response):
        for product in response.css('div.product_info'):
            title = product.css('div.product_name > a::text').extract()
            price = product.css('div.product_price > span.package_price b::text').extract()
            color = product.css('div.product_color_swatches > div.color_swatch_list img::attr(alt)').extract()
            description = product.css('div.product_description > p::text').extract()
            yield {'title': title,
                   'price': price,
                   'color': color,
                   'description': description}

