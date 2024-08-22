"""Own data types required for the application to work. Designed for ease of use with information"""

from typing import NamedTuple
from app.general.general_main import GeneralMain


class WollBall(NamedTuple):
    """
    Type for presenting information with scrolling results for the wollplatz-crawler
    """
    brand: str = None
    title: str = None
    availability: str = None
    price: float = None
    needle_size: str = None
    compilation: str = None
    date: str = None

    def __repr__(self):
        return f"Marke: {self.brand}, Bezeichnung: {self.title}, Verfügbarkeit: {self.availability}, Price (€): {self.price}, Nadelstärke (mm): {self.needle_size}, Zusammenstellung: {self.compilation}"


class CrawlerObject(NamedTuple):
    """
    Type to represent information about the crawler
    """
    crawler_name: str = None
    crawler_object: GeneralMain = None


class CommandObject(NamedTuple):
    """
    Type to represent command information
    """
    command_description: str = None
    command: object = None
