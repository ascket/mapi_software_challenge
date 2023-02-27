import sqlite3
import pytest
from app.general.own_data_types import *
from app.savers.save_to_database import DatabaseSaver
from tempfile import TemporaryDirectory
from pathlib import Path
from app.general.general_run import MainDialog
from app.general.general_crawler import Crawler


class TestOwnDataTypes:
    def test_wallball(self, one_wollball, wollball_values):
        for attr_name in wollball_values:
            assert getattr(one_wollball, attr_name) == wollball_values.get(attr_name)

    def test_wallbal_repr(self, one_wollball):
        assert one_wollball.__repr__() == "Marke: Example Brand, Bezeichnung: Example Product, Verfügbarkeit: Available, Price: 2.99€, Nadelstärke: 4 mm, Zusammenstellung: 100% Acryl"

    def test_crawler_object(self, crawler_object, crawler_object_values):
        for attr_names in crawler_object_values:
            assert getattr(crawler_object, attr_names) == crawler_object_values.get(attr_names)

    def test_command_object(self, command_object, command_object_values):
        for attr_names in command_object_values:
            assert getattr(command_object, attr_names) == command_object_values.get(attr_names)


class TestDatabase:
    def test_empty_db(self, db_session):
        cursor = db_session.connector.cursor()
        cursor_execute = cursor.execute("SELECT name FROM sqlite_master")
        count = 0
        for table in cursor_execute:
            count += 1
        assert count == 0

    def test_create_table(self, db_session, db_example_structure):
        db_session.create_table("muster_table", db_example_structure)
        cursor = db_session.connector.cursor()
        cursor_execute = cursor.execute("SELECT name FROM sqlite_master")
        count = 0
        for table in cursor_execute:
            count += 1
        cursor.execute("SELECT * FROM muster_table")
        names = [description[0] for description in cursor.description]
        assert count == 2
        assert names == list(db_example_structure.keys())

    def test_add_to_table(self, db_session, wollball_values):
        db_session.add_to_table("muster_table", wollball_values)
        cursor = db_session.connector.cursor()
        cursor_execute = cursor.execute("SELECT * FROM muster_table")
        result = cursor_execute.fetchall()
        assert len(result) == 1

    def test_database_saver(self, some_wollballs, db_example_structure, tmp_path_factory):
        path = tmp_path_factory.mktemp("sub")
        saver = DatabaseSaver()
        saver.save_to_database(some_wollballs, path, "muster", db_example_structure)
        db = sqlite3.connect(saver.path_file_to_save)
        cursor = db.cursor()
        cursor_execute = cursor.execute("SELECT * FROM muster")
        result = cursor_execute.fetchall()
        assert len(result) == len(some_wollballs)


class TestCrawler:
    @pytest.mark.parametrize(
        "valid_url",
        ["https://muster.com", "http://muster.com", "www.muster.com"]
    )
    def test_valid_url(self, valid_url):
        Crawler.__abstractmethods__ = set()
        cr = Crawler(valid_url)
        assert cr.url == valid_url

    @pytest.mark.parametrize(
        "invalid_url",
        ["https//muster.com", "http:/muster.com", "ww.muster.com", "muster.com", "htpp://muster.com"]
    )
    def test_invalid_url(self, invalid_url):
        Crawler.__abstractmethods__ = set()
        with pytest.raises(ValueError) as err:
            cr = Crawler(invalid_url)
        assert str(err.value) == "Invalid URL format"
