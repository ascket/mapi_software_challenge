import re
from abc import ABC, abstractmethod
from typing import List, Dict


class Crawler(ABC):
    def __init__(self, url: str):
        self.url = url
        self._crawling_results = []

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        if not self.__class__.check_valid_url(value):
            raise ValueError("Url must be correct.")
        self._url = value

    @staticmethod
    def check_valid_url(url_str: str):
        url_regex = re.compile(
            r'^(?:http|https)://'
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
            r'(?::\d+)?'
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        if url_str is None or not re.search(url_regex, url_str):
            return False
        return True

    @abstractmethod
    def main_crawler(self, products: List[Dict[str, str]]):
        pass
