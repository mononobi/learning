import sqlite3


_current_connection = None


def get_connection():
    global _current_connection
    if not _current_connection:
        result = sqlite3.connect("cinema.db")
        _current_connection = result
    return _current_connection


def get_cursor():
    return get_connection().cursor()


def execute(statement):
    return get_cursor().execute(statement)


def commit():
    get_connection().commit()


def rollback():
    get_connection().rollback()


def close():
    get_connection().close()
    global _current_connection
    _current_connection = None
