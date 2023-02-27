"""General crawler interface. Contains logic common to most crawlers and can be used to create different crawlers"""

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
            raise ValueError("Invalid URL format")
        self._url = value

    @staticmethod
    def check_valid_url(url_str: str) -> bool:
        """
        Checks the validity of the URL

        Args:
            url_str: URL to check as a string

        Returns:
            Bool
        """
        url_regex = re.compile(
            r'^((?:http|https)://)|(www.)'
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
