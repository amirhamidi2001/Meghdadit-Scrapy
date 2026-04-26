import re

import scrapy

from meghdadit.items import MeghdaditItem


class MeghdaditSpider(scrapy.Spider):
    name = "meghdadit"
    allowed_domains = ["meghdadit.com"]
    start_urls = [
        "https://meghdadit.com/product/119611/sapphire-graphic-card-model-"
        "toxic-radeon-rx-6900-xt-extreme-edition-16gb/"
    ]

    def parse(self, response):
        # Extract data from the response using XPath or CSS selectors
        title = response.css("title::text").get()
        url = response.url
        price = response.xpath("//input[@id='hfdPrices']/@value").get()

        if price is not None:
            price = price.strip()
            product_exist = True
        else:
            price = None
            product_exist = False

        product_id = re.search(r"/(\d+)/", response.url).group(1)
        categories = response.css("a.bread-link::text").getall()

        # Create a new item with the extracted data
        item = MeghdaditItem()
        item["title"] = title.strip()
        # item["price"] = price   # commented out as per original
        item["product_exist"] = product_exist
        item["product_id"] = product_id
        item["url"] = url
        item["domain"] = "meghdadit.com"
        item["categories"] = [category.strip() for category in categories][:-1]
        item["currency"] = "تومان"

        yield item
