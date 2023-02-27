from app.general.general_main import GeneralMain
from app.wollplatz.wollplatz_crawler import WollplatzCrawler

class WollplatzMain(GeneralMain):
    def __init__(self, path_to_products, wollplatz_crawler = WollplatzCrawler()):
        super().__init__(path_to_products, wollplatz_crawler)
