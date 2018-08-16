# -*- coding: utf-8 -*-
import scrapy
import datetime

class NitoriSpider(scrapy.Spider):
    name = 'nitorispider'

    start_urls = ['https://www.nitori-net.jp/store/ja/ec/']

    allowed_domains = ['www.nitori-net.jp']

    now = datetime.datetime.now()

    def parse(self, response):
        for url in response.css('ul > li > a::attr("href")').extract():
            yield scrapy.Request(response.urljoin(url), self.parse_products)

    def parse_products(self, response):
        for product in response.css('div.product.product-box'):
            site = 'ニトリ'
            my_datetime = self.now
            l_category = 'To Be Inserted'
            m_category = 'To Be Inserted'
            url = product.css('div.product_image > div.image > a.product-link::attr(href)').extract()[0]
            title = product.css('div.product_name > a::text').extract()
            img_url = 'https://' + self.allowed_domains[0] + product.css('div.product_image > div.image > a > div.image_area > img::attr(src)').extract()[0]
            price = product.css('div.product_price > span.package_price b::text').extract()
            size = 'To Be Inserted'
            color = product.css('div.product_color_swatches > div.color_swatch_list img::attr(alt)').extract()
            description = product.css('div.product_description > p::text').extract()

            yield {'site': site,
                   'datetime': my_datetime,
                   'l_category': l_category,
                   'm_category': m_category,
                   'url': url,
                   'title': title,
                   'img_url': img_url,
                   'price': price,
                   'size': size,
                   'color': color,
                   'description': description,
                   }
