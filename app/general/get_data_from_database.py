"""Get data from the database"""

from app.general.get_file_path import get_path
from pathlib import Path
import sqlite3, os


def get_data_from_db(db_name: str):
    ROOT_DIR = Path(__file__).parent.parent
    db_path = get_path(ROOT_DIR, [db_name, "results", f"{db_name}.db"])
    if not os.path.exists(db_path):
        return "Sie müssen zunächst die App starten, um gesamelte Daten in der Datenbank zu speichern."
    db = sqlite3.connect(db_path)
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM {db_name}")
    results = cursor.fetchall()
    cursor.close()
    return results
