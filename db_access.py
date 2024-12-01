import sqlite3

from models.income import Income
from models.expense import Expense
from models.goal import Goal
from models.category import Category
from models.user import User


def db_connect():
    conn = sqlite3.connect('budget_tracker.db')
    cur = conn.cursor()
    return conn, cur
