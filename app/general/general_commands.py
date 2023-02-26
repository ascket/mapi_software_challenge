import sys
from app.savers.save_to_csv import CsvSaver
from abc import ABC, abstractmethod


class CommandInterface(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class SaveCsvCommand(CommandInterface):
    def __init__(self):
        self.path = None

    def execute(self, data, file_dir, crawler_name, **kwargs):
        saver = CsvSaver()
        saver.save_to_file(data, file_dir, crawler_name)
        self.path = saver.get_path_file_to_save()

    def __repr__(self):
        return f"Ergebnisse wurden in {self.path} gespeichert!\n{15 * '-'}"


class QuitCommand(CommandInterface):
    def execute(self, *args, **kwargs):
        print("Tschüss")
        sys.exit()

    def __repr__(self):
        return "Tschüss"


class PrintResults(CommandInterface):
    def execute(self, results, *_, **kwargs):
        print(results)

    def __repr__(self):
        return f"Ergebnisse wurden angezeigt!\n{15 * '-'}"
