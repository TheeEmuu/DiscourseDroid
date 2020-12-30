import sqlite3

def _connect():
    conn = sqlite3.connect('pieces.db')
    return conn

def get(toGet: str) -> str:
    conn = _connect()

    sql = "SELECT name FROM " + toGet + " ORDER BY RANDOM() LIMIT 1"
    cursor = conn.execute(sql)
    for row in cursor:
        return str(row[0])

def addData(type, name):
    conn = _connect()

    sql = "INSERT INTO " + type + "VALUES(" + name + ")"
    conn.execute(sql)

    conn.commit()