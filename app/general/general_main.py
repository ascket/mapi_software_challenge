import csv, os
from typing import List
from datetime import datetime


class GeneralMain:
    def __init__(self, path_to_crawling_products, crawler_object):
        self.crawler = crawler_object
        self.path_to_crawling_products = path_to_crawling_products
        self.results = None

    def get_products_to_crawling(self, data_path: str):
        pc = []
        with open(data_path, newline='') as csvfile:
            products = csv.reader(csvfile, delimiter=';')
            header = next(products)
            for product in products:
                pc.append({"brand_name": product[0], "product_name": product[1]})
        return pc

    def get_crawling_results(self):
        data = self.get_products_to_crawling(self.path_to_crawling_products)
        self.results = self.crawler.main_crawler(data)
        return self.results
