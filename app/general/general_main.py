"""General method to run a crawler job"""

import csv, os
from typing import List
from datetime import datetime
from app.general.general_crawler import Crawler
from typing import List


class GeneralMain:
    def __init__(self, path_to_crawling_products: str, crawler_object: Crawler) -> None:
        """
        Initiates an object of this class

        Args:
            path_to_crawling_products: Path to the csv-file with information of crawling products
            crawler_object: Crawler object
        """
        self.crawler = crawler_object
        self.path_to_crawling_products = path_to_crawling_products
        self.results = None

    def get_products_to_crawling(self, data_path: str) -> List:
        """
        Gets crawling products from a .csv-file and returns them as a list

        Args:
            data_path: Path to the csv-file with information of crawling products

        Returns:
            List of crawling products
        """
        pc = []
        with open(data_path, newline='') as csvfile:
            products = csv.reader(csvfile, delimiter=';')
            header = next(products)
            for product in products:
                pc.append({"brand_name": product[0], "product_name": product[1]})
        return pc

    def get_crawling_results(self) -> List[object]:
        """
        Gets the crawling results from the crawler

        Returns:
            List of crawling results
        """
        data = self.get_products_to_crawling(self.path_to_crawling_products)
        self.results = self.crawler.main_crawler(data)
        return self.results
