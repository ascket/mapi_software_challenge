from app.general.general_main import GeneralMain
from app.wollplatz.wollplatz_crawler import WollplatzCrawler

class WollplatzMain(GeneralMain):
    def __init__(self, path_to_products, wollplatz_crawler = WollplatzCrawler()):
        super().__init__(path_to_products, wollplatz_crawler)














# products_to_crawling = [
#     {"brand_name": "DMC", "product_name": "Natura XL"},
#     {"brand_name": "Drops", "product_name": "Safran"},
#     {"brand_name": "Drops", "product_name": "Baby Merino Mix"},
#     {"brand_name": "Hahn", "product_name": "Alpacca Speciale"},
#     {"brand_name": "Stylecraft", "product_name": "Special double knit"},
#     {"brand_name": "Rico", "product_name": "Essentials Super"}
# ]


# FILE_DIR = os.path.dirname(__file__)
#
#
# def get_path(dir_name: str, fd_name: List):
#     return os.path.join(dir_name, *fd_name)
#
#
# CSV_FILE_PATH = get_path(FILE_DIR, ["data_to_crawling.csv"])
#
#
# def get_products_to_crawling(data_path: str):
#     pc = []
#     with open(data_path, newline='') as csvfile:
#         products = csv.reader(csvfile, delimiter=';')
#         header = next(products)
#         for product in products:
#             pc.append({"brand_name": product[0], "product_name": product[1]})
#     return pc
#
#
# def get_crawling_results(file_path: str):
#     data = get_products_to_crawling(file_path)
#     crawler = WollplatzCrawler()
#     results = crawler.main_crawler(data)
#     return results
#
#
# def save_crawling_results(saver_type: str, results: List):
#     if not os.path.exists(get_path(FILE_DIR, ["results"])):
#         os.makedirs(get_path(FILE_DIR, ["results"]))
#     if saver_type == "csv":
#         CsvSaver().save_csv(results, get_path(FILE_DIR, ["results", f'{datetime.now().strftime("%d_%m_%YT%H_%M")}_wollplatz.csv']))
#
# if __name__ == "__main__":
#     results = get_crawling_results(CSV_FILE_PATH)
#     print(results)
#     save_crawling_results("csv", results)
#     print("Save!")
#     #print(get_path(FILE_DIR, ["results", f'{datetime.now().strftime("%d_%m_%YT%H_%M")}_wollplatz.csv']))
