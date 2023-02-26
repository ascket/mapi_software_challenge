from app.wollplatz.wollplatz_crawler import WollplatzCrawler
from app.general.get_file_path import get_path
import os
import app.general.general_commands as commands

available_crawlers = {"wollplatz": WollplatzCrawler()}
available_commands = {1: commands.SaveCsvCommand(), 2: commands.PrintResults(), 3: commands.QuitCommand()}

FILE_DIR = get_path(os.path.dirname(__file__), ["wollplatz"])

CSV_FILE_PATH = get_path(FILE_DIR, ["data_to_crawling.csv"])



if __name__ == "__main__":
    # crawler = available_crawlers["wollplatz"]
    # wp_main = WollplatzMain(crawler, CSV_FILE_PATH)
    # results = wp_main.get_crawling_results()
    # print(results)
    # CsvSaver().execute(results, FILE_DIR, "wollplatz")
    available_commands.get(2).execute("This is OK")
