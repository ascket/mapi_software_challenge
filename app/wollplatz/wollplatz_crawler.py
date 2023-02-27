import requests
from bs4 import BeautifulSoup
from typing import List, Dict
import re
from app.wollplatz.wollplatz_crawling_url import wollplatz_product_url
from app.general.general_crawler import Crawler
from app.general.own_data_types import WollBall
import json
from datetime import datetime

URL = f"https://dynamic.sooqr.com/suggest/script/"
ACCOUNT_NUMBER = "SQ-119572-1"


class WollplatzCrawler(Crawler):
    def __init__(self, url: str = URL):
        super().__init__(url)

    @staticmethod
    def get_table(soup_object):
        table_results = {}
        table = soup_object.find("div", id="pdetailTableSpecs").select_one("table").select("tr")
        for td in table:
            td_info = td.select("td")
            specification = td_info[0].text
            info = td_info[1].text
            table_results[specification] = info
        return table_results

    def main_crawler(self, products: List[Dict[str, str]]):
        products = wollplatz_product_url(products, self.url, ACCOUNT_NUMBER)
        for product in products:
            if product["href"] is not None:
                req = requests.get(product["href"])
                req.raise_for_status()
                soup = BeautifulSoup(req.text, "html.parser")
                product_title = soup.find("h1").text
                availability = soup.find("span", class_="stock-green")
                if availability is not None:
                    availability = availability.text
                else:
                    availability = "Nicht lieferbar"
                price = soup.find("div", class_="buy-price").select_one(".product-price-amount").text
                specifications = self.__class__.get_table(soup)
                brand = specifications.get("Marke")
                needle_size = specifications.get("Nadelstärke")
                compilation = specifications.get("Zusammenstellung")
                woll_ball = WollBall(brand, product_title, availability, float(price.replace(",", ".")),
                                     needle_size.split()[0], compilation, datetime.now().strftime("%d-%m-%YT%H:%M"))
                self._crawling_results.append(woll_ball)
            else:
                print(f"{product['title']} wurde nicht gefunden.")
        return self._crawling_results
