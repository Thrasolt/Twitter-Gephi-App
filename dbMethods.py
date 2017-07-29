import sqlite3

# Connection Seupt
conn = sqlite3.connect('gephi.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS GephiNodes(id INTEGER, label TEXT, fan_count INTEGER, category TEXT )')
    c.execute('CREATE TABLE IF NOT EXISTS GephiEdges(source INTEGER, target INTEGER, type TEXT, id INTEGER, weight INTEGER)')

def dynamic_data_entry_Nodes(id, label, fan_count, category):
    c.execute("INSERT INTO GephiNodes (id, label, fan_count, category) VALUES (?, ?, ?, ?)",
          (id, label, fan_count, category))
    conn.commit()

def dynamic_data_entry_Edges(source, target, type, id, weight):
    c.execute("INSERT INTO GephiEdges (source, target, type, id, weight) VALUES (?, ?, ?, ?, ?)",
          (source, target, type, id, weight))
    conn.commit()

def read_from_db_GephiNodes(**kwargs):
    if "id" in kwargs:
        id = (kwargs["id"], )
        c.execute("SELECT * FROM GephiNodes WHERE id=?", id)
        data = c.fetchall()
        return data
    if "label" in kwargs:
        label = (kwargs["label"], )
        c.execute("SELECT * FROM GephiNodes WHERE label=?", label)
        data = c.fetchall()
        return data
    c.execute("SELECT * FROM GephiNodes")
    data = c.fetchall()
    return data


def read_from_db_GephiEdges(**kwargs):
    if "id" in kwargs:
        id = (kwargs["id"], )
        c.execute("SELECT * FROM GephiEdges WHERE id=?", id)
        data = c.fetchall()
        return data
    if "source" in kwargs:
        source = (kwargs["source"], )
        c.execute("SELECT * FROM GephiEdges WHERE source=?", source)
        data = c.fetchall()
        return data
    if "target" in kwargs:
        target = (kwargs["target"], )
        c.execute("SELECT * FROM GephiEdges WHERE target=?", target)
        data = c.fetchall()
        return data
    c.execute("SELECT * FROM GephiEdges")
    data = c.fetchall()
    return data

def close_connection():
    c.close()
    conn.close()
