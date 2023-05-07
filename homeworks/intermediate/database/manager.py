import homeworks.intermediate.database.database as db


def insert(statement, **kwargs):
    result = db.execute(statement.format(**kwargs))
    db.commit()
    return result


def update(statement, **kwargs):
    result = db.execute(statement.format(**kwargs))
    db.commit()
    return result


def delete(statement, **kwargs):
    result = db.execute(statement.format(**kwargs))
    db.commit()
    return result


def select_all(statement, **kwargs):
    return db.execute(statement.format(**kwargs)).fetchall()


def select_one(statement, **kwargs):
    return db.execute(statement.format(**kwargs)).fetchone()
