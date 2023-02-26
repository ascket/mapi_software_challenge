import sqlite3
from typing import List, Dict, Tuple


class DatabaseConnector:
    def __init__(self, database_name: str):
        self.connector = sqlite3.connect(database_name)


    def __del__(self):
        self.connector.close()


    def _execute(self, sql_command: str, values: Tuple[object] = None):
        with self.connector:
            cursor = self.connector.cursor()
            cursor.execute(sql_command, value or ())
            return cursor


    def create_table(self, table_name: str, columns: Dict[str, str]):
        """CREATE TABLE IF NOT EXISTS table_name (id INTEGER PRIMARY KEY AUTOINCREMENT)"""
        placeholders = ", ".join(f"{col_name} {col_value}" for col_name, col_value in columns.items())
        self._execute(
            f"""CREATE TABLE IF NOT EXISTS {table_name} ({placeholders})"""
        )


    def add_to_table(self, table_name: str, columns: Dict[str, object]):
        """INSERT INTO TABLE table_name (name, lastname) VALUES (?, ?)"""
        placeholders = ", ".join("?" * len(columns))
        col_names = ", ".join(columns.keys())
        col_values = tuple(columns.values())

        self._execute(
            f"""INSERT INTO {table_name} ({col_names}) VALUES ({placeholders});""", col_values
        )




