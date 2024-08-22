import pytest
from app.general.own_data_types import *
from app.savers.save_to_database import DatabaseSaver, DatabaseConnector
from pathlib import Path
from tempfile import TemporaryDirectory


@pytest.fixture()
def wollball_values():
    return {
        "brand": "Example Brand",
        "title": "Example Product",
        "availability": "Available",
        "price": 2.99,
        "needle_size": "4",
        "compilation": "100% Acryl",
        "date": "27-02-2023T08:45"
    }


@pytest.fixture()
def crawler_object_values():
    return {
        "crawler_name": None,
        "crawler_object": None
    }


@pytest.fixture()
def command_object_values():
    return {
        "command_description": None,
        "command": None
    }


@pytest.fixture()
def one_wollball(wollball_values):
    return WollBall(**wollball_values)


@pytest.fixture()
def crawler_object(crawler_object_values):
    return CrawlerObject(**crawler_object_values)


@pytest.fixture()
def command_object(command_object_values):
    return CommandObject(**command_object_values)


@pytest.fixture(scope="session")
def db_session(tmp_path_factory):
    path = tmp_path_factory.mktemp("sub")
    db_path = path / "muster.db"
    connection = DatabaseConnector(db_path)
    yield connection
    del (connection)


@pytest.fixture()
def db_example_structure():
    return {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "brand": "TEXT NOT NULL",
        "title": "TEXT NOT NULL",
        "availability": "TEXT",
        "price": "REAL",
        "needle_size": "TEXT",
        "compilation": "TEXT",
        "date": "TEXT NOT NULL",
    }


@pytest.fixture()
def some_wollballs():
    return [
        WollBall(brand='DMC', title='DMC Natura XL 02 Black', availability='Nicht lieferbar', price=8.46,
                 needle_size='8', compilation='100% Baumwolle', date='27-02-2023T09:44'),
        WollBall(brand='Drops', title='Drops Safran 1 Light-pink', availability='Lieferbar', price=1.1, needle_size='3',
                 compilation='100% Baumwolle', date='27-02-2023T09:44'),
        WollBall(brand='Drops', title='Drops Baby Merino Mix 17 Beige', availability='Lieferbar', price=3.35,
                 needle_size='3', compilation='100% Merinowolle', date='27-02-2023T09:44'),
        WollBall(brand='Stylecraft', title='Stylecraft Special dk 1001 White', availability='Lieferbar', price=2.85,
                 needle_size='4', compilation='100% Acryl', date='27-02-2023T09:44')
    ]
