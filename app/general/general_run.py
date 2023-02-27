from app.wollplatz.wollplatz_main import WollplatzMain
from app.general.own_data_types import CommandObject, CrawlerObject
from app.general.general_crawler import Crawler
from app.general.get_file_path import get_path
import os
import app.general.general_commands as commands
from pathlib import Path
from typing import Dict

ROOT_DIR = Path(__file__).parent.parent


def file_dir_path(crawler_name: str):
    list_ = [crawler_name]
    return get_path(ROOT_DIR, list_)


def path_crawling_products(crawler_name: str):
    return get_path(file_dir_path(crawler_name), ["data_to_crawling.csv"])


available_crawlers = {
    "1": CrawlerObject("wollplatz", WollplatzMain(path_crawling_products("wollplatz")))
}
available_commands = {
    "A": CommandObject("Ergebnisse anzeigen", commands.PrintResults()),
    "B": CommandObject("Ergebnisse als .csv speichern", commands.SaveCsvCommand()),
    "D": CommandObject("Ergebnisse in Database speichern", commands.SaveDatabaseCommand()),
    "C": CommandObject("Anderen Crawler auswählen", None),
    "Q": CommandObject("Exit", commands.QuitCommand())
}


class MainDialog:
    def main_dialog(self):
        while True:
            print(f"Verfügbare Crawlers:\n{self.get_crawlers_number(available_crawlers)}")
            crawler_number = input("Geben Sie Ihr Crawler Nummer oder 'Q' zum Beenden: ")
            if crawler_number not in list(available_crawlers.keys()) and crawler_number.lower() != "q":
                print(f"Wir haben keinen Crawler mit der Nummer {crawler_number}.\n{15 * '-'}")
            elif crawler_number.lower() == "q":
                ac = available_commands["Q"].command
                ac.execute()
            else:
                selected_crawler = available_crawlers[crawler_number]
                print(
                    f"Sie haben {selected_crawler.crawler_name} gewählt. Wir fangen an, Informationen zu sammeln...")
                wp_main = selected_crawler.crawler_object
                results = wp_main.get_crawling_results()
                if len(results) == 0:
                    print(
                        f"\nWir haben nichts gefunden. Ändern Sie Ihre Suchbegriffe oder probieren Sie einen anderen Crawler.\n{15 * '-'}")
                    continue
                print(f"Wir haben {len(results)} Ergebnisse gefunden.")
                # print(results)
                while True:
                    print("Was wollen Sie als Nächstes tun: ")
                    for key, value in available_commands.items():
                        print(f"{3 * ' '}{key}: {value.command_description}")
                    command_list = list(available_commands.keys())
                    command_result = input(f"Wählen Sie {', '.join(command_list[:-1]) + ' oder ' + command_list[-1]}: ")
                    if command_result.upper() not in command_list and command_result.upper() != "Q":
                        print(f"Wir haben '{command_result}' nicht.\n{15 * '-'}")
                    elif command_result.upper() == "C":
                        break
                    else:
                        ac = available_commands[command_result.upper()].command
                        ac.execute(
                            results, file_dir_path(selected_crawler.crawler_name),
                            selected_crawler.crawler_name)
                        print(ac)

    def get_crawlers_number(self, available_crawlers: Dict[str, CrawlerObject]):
        result = ""
        for key, value in available_crawlers.items():
            result += f"{3 * ' '}{key}: {value.crawler_name}\n"
        return result
