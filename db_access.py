import sqlite3


def db_connect():
    conn = sqlite3.connect('budget_tracker.db')
    cur = conn.cursor()
    return conn, cur
