import sqlite3

conn = sqlite3.connect("tutorial.db")
cur = conn.cursor()
# cur.execute("CREATE TABLE movie(title, year, score)")
cur.execute("insert into movie values ('stray', '2021', '8')")
# res2 = cur.execute("insert into movie values ('enigma', '2002', '8')")
cur.connection.commit()

res1 = cur.execute("select * from movie")
one = res1.fetchone()
# all_ = res1.fetchall()
z = 0
# cur.close()
cur.connection.close()
