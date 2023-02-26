import csv, os
from typing import List, Dict
from app.general.get_file_path import get_path
from datetime import datetime


class CsvSaver:
    def __init__(self):
        self.path_file_to_save = None

    def save_to_file(self, data_to_save: List[object], file_dir: str, crawler_name: str):
        if not os.path.exists(get_path(file_dir, ["results"])):
            os.makedirs(get_path(file_dir, ["results"]))
        header = data_to_save[0]._asdict().keys()
        format_path_to_save = f'{datetime.now().strftime("%d_%m_%YT%H_%M")}_{crawler_name}.csv'
        self.path_file_to_save = get_path(file_dir, ["results", format_path_to_save])
        with open(self.path_file_to_save, "w", newline="") as csvfile:
            result_writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            result_writer.writerow(header)
            for data in data_to_save:
                result_writer.writerow(data._asdict().values())


    def get_path_file_to_save(self):
        return self.path_file_to_save
