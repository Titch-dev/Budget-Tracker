import sqlite3

conn = sqlite3.connect('budget_tracker.db')  # Production database
cur = conn.cursor()

CREATE_USER_TABLE = '''
CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    created_at TEXT DEFAULT (DATETIME('now')),
    last_login TEXT DEFAULT NULL
);
'''

INSERT_USER = '''
INSERT INTO user (email, password)
    VALUES(?, ?)
'''

INITIAL_USER = ('test@test.com', 'password')

CREATE_CATEGORY_TABLE = '''
CREATE TABLE IF NOT EXISTS category(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) UNIQUE NOT NULL,
    desc VARCHAR(500),
    budget FLOAT DEFAULT 0.00,
    created_at TEXT DEFAULT (DATETIME('now')),
    user_id INTEGER,
    CONSTRAINT fk_user
        FOREIGN KEY(user_id)
        REFERENCES user(id)
        ON DELETE CASCADE
);
'''

INSERT_CATEGORIES = '''
INSERT INTO category (name, desc, budget, user_id)
    VALUES(?, ?, ?, ?)
'''

INITIAL_CATEGORIES = [
    ("Salary", "Monthly salary payment", 0.00, 1),
    ("Rent", "Monthly rent payment.", 0.00, 1),
    ("Utilities", "Electricity, water, and gas bills.", 0.00, 1),
    ("Dining Out", "Eating out at restaurants and cafes.", 150.00, 1),
    ("Health & Fitness", "Gym membership and health-related expenses.", 0.00, 1),
    ("Goals", "Working towards financial goals.", 0.00, 1)
]

CREATE_GOAL_TABLE = '''
CREATE TABLE IF NOT EXISTS goal(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) UNIQUE NOT NULL,
    desc VARCHAR(500),
    target FLOAT DEFAULT 0.00,
    end_date TEXT,
    created_at TEXT DEFAULT (DATETIME('now')),
    user_id INTEGER NOT NULL,
    CONSTRAINT fk_user
        FOREIGN KEY(user_id)
        REFERENCES user(id)
        ON DELETE CASCADE
);
'''

INSERT_GOAL = '''
INSERT INTO goal(name, desc, target, end_date, user_id)
    VALUES (?, ?, ?, ?, ?)
'''

INITIAL_GOAL = ("Vacation Fund", "Saving for a vacation trip to Hawaii.", 5000.00, "2025-06-01 00:00:00", 1)


CREATE_EXPENSE_TABLE = '''
CREATE TABLE IF NOT EXISTS expense(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    amount FLOAT DEFAULT 0.00,
    effect_date TEXT NOT NULL,
    created_at TEXT DEFAULT (DATETIME('now')),
    user_id INTEGER NOT NULL,
    category_id INTEGER,
    goal_id INTEGER,
    CONSTRAINT fk_user
        FOREIGN KEY(user_id)
        REFERENCES user(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_category
        FOREIGN KEY(category_id)
        REFERENCES category(id),
    CONSTRAINT fk_goal
        FOREIGN KEY(goal_id)
        REFERENCES category(id)
        ON DELETE CASCADE
);
'''

INSERT_EXPENSES = '''
INSERT INTO expense (name, amount, effect_date, user_id, category_id, goal_id)
    VALUES (?, ?, ?, ?, ?, ?)'''

INITIAL_EXPENSES = [
    ("Rent", 1200.00, "2024-07-01 00:00:00", 1, 2, None),
    ("Electricity Bill", 60.00, "2024-07-03 00:00:00", 1, 3, None),
    ("Ask Italian", 40.00, "2024-07-05 00:00:00", 1, 4, None),
    ("Gas Bill", 30.00, "2024-07-06 00:00:00", 1, 3, None),
    ("Burger King", 15.00, "2024-07-20 00:00:00", 1, 4, None),
    ("Rent", 1200.00, "2024-08-01 00:00:00", 1, 2, None),
    ("Electricity Bill", 60.00, "2024-08-03 00:00:00", 1, 3, None),
    ("Gas Bill", 30.00, "2024-08-06 00:00:00", 1, 3, None),
    ("Vacation Saving", 20.00, "2024-08-25 00:00:00", 1, 6, 1),
    ("Rent", 1200.00, "2024-09-01 00:00:00", 1, 2, None),
    ("Electricity Bill", 60.00, "2024-09-03 00:00:00", 1, 3, None),
    ("Gas Bill", 30.00, "2024-09-06 00:00:00", 1, 3, None),
    ("Vacation Saving", 30.00, "2024-09-25 00:00:00", 1, 6, 1),
    ("Rent", 1200.00, "2024-10-01 00:00:00", 1, 2, None),
    ("Gym", 75.00, "2024-10-02 00:00:00", 1, 5, None),
    ("Electricity Bill", 60.00, "2024-10-03 00:00:00", 1, 3, None),
    ("Gas Bill", 30.00, "2024-10-06 00:00:00", 1, 3, None),
    ("Yo Sushi", 45.00, "2024-10-10 00:00:00", 1, 4, None),
    ("Vacation Saving", 30.00, "2024-10-25 00:00:00", 1, 6, 1)
]

CREATE_INCOME_TABLE = '''
CREATE TABLE IF NOT EXISTS income(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    amount FLOAT DEFAULT 0.00,
    effect_date TEXT NOT NULL,
    created_at TEXT DEFAULT (DATETIME('now')),
    user_id INTEGER NOT NULL,
    category_id INTEGER,
    CONSTRAINT fk_user
        FOREIGN KEY(user_id)
        REFERENCES user(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_category
        FOREIGN KEY(category_id)
        REFERENCES category(id)
);
'''

INSERT_INCOMES = '''
INSERT INTO income (name, amount, effect_date, user_id, category_id)
    VALUES(?, ?, ?, ?, ?)
'''

INITIAL_INCOME = [
    ("Work Salary", 2000.00, "2024-06-25 00:00:00", 1, 1),
    ("Work Salary", 2000.00, "2024-07-25 00:00:00", 1, 1),
    ("Work Salary", 2000.00, "2024-08-25 00:00:00", 1, 1),
    ("Work Salary", 2000.00, "2024-09-25 00:00:00", 1, 1),
    ("Work Salary", 2000.00, "2024-10-25 00:00:00", 1, 1),
]

try:
    cur.execute("DROP TABLE IF EXISTS user")
    cur.execute(CREATE_USER_TABLE)
    cur.execute("DROP TABLE IF EXISTS category")
    cur.execute(CREATE_CATEGORY_TABLE)
    cur.execute("DROP TABLE IF EXISTS goal")
    cur.execute(CREATE_GOAL_TABLE)
    cur.execute("DROP TABLE IF EXISTS expense")
    cur.execute(CREATE_EXPENSE_TABLE)
    cur.execute("DROP TABLE IF EXISTS income")
    cur.execute(CREATE_INCOME_TABLE)
    conn.commit()
except Exception as e:
    conn.rollback()
    print(e)

try:
    cur.execute(INSERT_USER, INITIAL_USER)
    cur.executemany(INSERT_CATEGORIES, INITIAL_CATEGORIES)
    cur.execute(INSERT_GOAL, INITIAL_GOAL)
    cur.executemany(INSERT_EXPENSES, INITIAL_EXPENSES)
    cur.executemany(INSERT_INCOMES, INITIAL_INCOME)
    conn.commit()
except Exception as e:
    conn.rollback()
    print(e)

conn.close()