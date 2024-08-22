"""It saves information with crawling results in the database"""

import sqlite3, os
from typing import List, Dict, Tuple
from app.general.get_file_path import get_path

DB_EXAMPLE_STRUCTURE = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "brand": "TEXT NOT NULL",
    "title": "TEXT NOT NULL",
    "availability": "TEXT",
    "price": "REAL",
    "needle_size": "TEXT",
    "compilation": "TEXT",
    "date": "TEXT NOT NULL",
}


class DatabaseConnector:
    def __init__(self, database_name: str):
        self.connector = sqlite3.connect(database_name)

    def __del__(self):
        self.connector.close()

    def _execute(self, sql_command: str, values: Tuple[object] = None):
        with self.connector:
            cursor = self.connector.cursor()
            cursor.execute(sql_command, values or ())
            return cursor

    def create_table(self, table_name: str, columns: Dict[str, str]):
        placeholders = ", ".join(f"{col_name} {col_value}" for col_name, col_value in columns.items())
        self._execute(
            f"""CREATE TABLE IF NOT EXISTS {table_name} ({placeholders})"""
        )

    def add_to_table(self, table_name: str, columns: Dict[str, object]):
        placeholders = ", ".join("?" * len(columns))
        col_names = ", ".join(columns.keys())
        col_values = tuple(columns.values())

        self._execute(
            f"""INSERT INTO {table_name} ({col_names}) VALUES ({placeholders});""", col_values
        )


class DatabaseSaver:
    def __init__(self):
        self.path_file_to_save = None

    def save_to_database(self, data_to_save: List[object], file_dir: str, crawler_name: str,
                         db_structure: Dict[str, str] = DB_EXAMPLE_STRUCTURE):
        if not os.path.exists(get_path(file_dir, ["results"])):
            os.makedirs(get_path(file_dir, ["results"]))
        header = data_to_save[0]._asdict().keys()
        format_path_to_save = f'{crawler_name}.db'
        self.path_file_to_save = get_path(file_dir, ["results", format_path_to_save])
        db = DatabaseConnector(self.path_file_to_save)
        db.create_table(crawler_name, db_structure)

        for data in data_to_save:
            db.add_to_table(crawler_name, data._asdict())

    def get_path_file_to_save(self):
        return self.path_file_to_save
