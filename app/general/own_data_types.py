from typing import NamedTuple
from app.general.general_main import GeneralMain


class WollBall(NamedTuple):
    brand: str = None
    title: str = None
    availability: str = None
    price: float = None
    needle_size: str = None
    compilation: str = None
    date: str = None

    def __repr__(self):
        return f"Marke: {self.brand}, Bezeichnung: {self.title}, Verfügbarkeit: {self.availability}, Price: {self.price}€, Nadelstärke: {self.needle_size} mm, Zusammenstellung: {self.compilation}"


class CrawlerObject(NamedTuple):
    crawler_name: str = None
    crawler_object: GeneralMain = None


class CommandObject(NamedTuple):
    command_description: str = None
    command: object = None
