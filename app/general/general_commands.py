"""Commands used in the user interface"""

import sys
from app.savers.save_to_csv import CsvSaver
from app.savers.save_to_database import DatabaseSaver
from abc import ABC, abstractmethod
from typing import List

SEPARATOR_LENGTH = 15


class CommandInterface(ABC):
    """
    Common command interface
    """

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class SaveCsvCommand(CommandInterface):
    """
    Command for saving results to a .csv-file
    """

    def __init__(self):
        self.path = None

    def execute(self, data: List[object], file_dir: str, crawler_name: str, **kwargs):
        """
        It runs a save command.

        Args:
            data: Data to save
            file_dir: Path to crawler directory
            crawler_name: Crawler name
            **kwargs: Optional variables

        Returns:
            None
        """
        saver = CsvSaver()
        saver.save_to_file(data, file_dir, crawler_name)
        self.path = saver.get_path_file_to_save()

    def __repr__(self):
        return f"Ergebnisse wurden in {self.path} gespeichert!\n{SEPARATOR_LENGTH * '-'}"


class SaveDatabaseCommand(CommandInterface):
    """
    Command for saving results to a database
    """

    def __init__(self):
        self.path = None

    def execute(self, data, file_dir, crawler_name, **kwargs):
        """
        It runs a save command.

        Args:
            data: Data to save
            file_dir: Path to crawler directory
            crawler_name: Crawler name
            **kwargs: Optional variables

        Returns:
            None
        """
        saver = DatabaseSaver()
        saver.save_to_database(data, file_dir, crawler_name)
        self.path = saver.get_path_file_to_save()

    def __repr__(self):
        return f"Ergebnisse wurden in {self.path} gespeichert!\n{SEPARATOR_LENGTH * '-'}"


class QuitCommand(CommandInterface):
    """
    Command for the exit from the user interface
    """

    def execute(self, *args, **kwargs):
        print("Tschüss")
        sys.exit()

    def __repr__(self):
        return "Tschüss"


class PrintResults(CommandInterface):
    """
    Command for printing the results of crowling
    """

    def execute(self, results, *_, **kwargs):
        print(f"{SEPARATOR_LENGTH * '-'}")
        for result in results:
            print(result)

    def __repr__(self):
        return f"Ergebnisse wurden angezeigt!\n{SEPARATOR_LENGTH * '-'}"
