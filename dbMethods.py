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

def read_from_db_GephiNodes():
    c.execute("SELECT * FROM GephiNodes")

def read_from_db_GephiNodes():
    c.execute("SELECT * FROM GephiEdges")

def close_connection():
    c.close()
    conn.close()
