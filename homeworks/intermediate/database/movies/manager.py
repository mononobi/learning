import homeworks.intermediate.database.manager as db
import homeworks.intermediate.database.movies.queries as query


def create(name, year, score):
    db.insert(query.INSERT, name=name, year=year, score=score)


create('up', 2007, 8)
create('cars', 2008, 7)
create('django', 2009, 9)
