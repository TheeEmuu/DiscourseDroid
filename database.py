import sqlite3
from sqlite3.dbapi2 import IntegrityError

from discord.ext.commands.errors import MissingRequiredArgument

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

    sql = "INSERT INTO " + type + "(name) VALUES(\'" + name + "\')"
    try:
        conn.execute(sql)
    except IntegrityError:
        return name + " is already in " + type
    except MissingRequiredArgument:
        return "Missing one of the arguments"
    except:
        return "Failed for some reason"

    conn.commit()

    return name + " was added to " + type

def removeData(type, name):
    conn = _connect()

    sql = "DELETE FROM " + type + " WHERE name=\"" + name + "\"" 

    conn.execute(sql)

    conn.commit()

    return "No, Fuck you"
