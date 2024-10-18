import sqlite3

def db_connect():
    conn = sqlite3.connect('budget_tracker.db')
    cur = conn.cursor()
    return conn, cur

### USER
# create user
def create_user(user: dict) -> None:
    conn, cur = db_connect()
    command = '''INSERT INTO user (email, password) 
                    VALUES (?, ?)'''
    cur.execute(command, (user.email, user.password))
    conn.commit()
    conn.close()
    print(f'user: {user.email}, has been created')

# update user
def update_user(user: dict) -> None:
    conn, cur = db_connect()
    command = '''INSERT OR REPLACE INTO user (id, email, password, last_login)
                    VALUES(?, ?, ?, ?)'''
    cur.execute(command, (user.id,
                          user.email,
                          user.password,
                          user.last_login))
    conn.commit()
    conn.close()
    print(f'user: {user.email}, has been updated')

# delete user
def delete_user(user_id: int) -> None:
    conn, cur = db_connect()
    command = '''DELETE FROM user WHERE id = ?'''
    cur.execute(command, (user_id))
    conn.commit()
    conn.close()
    print(f'user: {user_id}, has been deleted')

# get user
def get_user_by_id(user_id: int) -> tuple:
    conn, cur = db_connect()
    command = '''SELECT * FROM user WHERE id = ?'''
    cur.execute(command, (user_id))
    data = cur.fetchone()
    conn.close()
    print(data)
    return data

def get_user_by_email(email: str) -> tuple:
    conn, cur = db_connect()
    command = '''SELECT * FROM user WHERE email = ?'''
    cur.execute(command, (email))
    data = cur.fetchone()
    conn.close()
    print(data)
    return data

### CATEGORY
# create category
def create_category(category: dict) -> None:
    conn, cur = db_connect()
    command = '''INSERT INTO category(name, desc, budget, user_id)
                    VALUES(?, ?, ?, ?)'''
    cur.execute(command, (category.name,
                          category.desc,
                          category.budget,
                          category.user_id))
    conn.commit()
    conn.close()
    print(f'category: {category.name}, has been created')

# update category
def update_category(category: dict) -> None:
    conn, cur = db_connect()
    command = '''INSERT OR REPLACE INTO category(id, name, desc, budget)
                    VALUES(?, ?, ?, ?)'''
    cur.execute(command,(category.id,
                         category.name,
                         category.desc,
                         category.budget))
    conn.commit()
    conn.close()
    print(f'category: {category.id}, has been updated')

# delete Category
def delete_category(category_id: int) -> None:
    conn, cur = db_connect()
    command = '''DELETE FROM category WHERE id = ?'''
    cur.execute(command,(category_id))
    conn.commit()
    conn.close()
    print(f'category: {category_id}, has been deleted')

# get all user's categories
def get_user_categories(user_id: int) -> list[tuple]:
    conn, cur = db_connect()
    command = '''SELECT * FROM category WHERE user_id = ?'''
    cur.execute(command, (user_id))
    data = cur.fetchall()
    conn.close()
    return data

# get category by ID
def get_category_by_id(cat_id:int) -> tuple:
    conn, cur = db_connect()
    command = '''SELECT * FROM category WHERE id = ?'''
    cur.execute(command, (cat_id))
    data = cur.fetchone()
    conn.close()
    return data

### GOAL
# create goal
def create_goal(goal: dict) -> None:
    conn, cur = db_connect()
    command = '''INSERT INTO goal (name, desc, target, end_date, user_id)
                    VALUES(?, ?, ?, ?, ?)'''
    cur.execute(command, (goal.name,
                          goal.desc,
                          goal.target,
                          goal.end_date,
                          goal.user_id))
    conn.commit()
    conn.close()
    print(f'goal: {goal.name}, has been created')

# update goal
def update_goal(goal: dict) -> None:
    conn, cur = db_connect()
    command = '''INSERT OR REPLACE INTO goal (id, name, desc, target, end_date)
                    VALUES (?, ?, ?, ?, ?)'''
    cur.execute(command, (goal.id,
                          goal.name,
                          goal.desc,
                          goal.target,
                          goal.end_date))
    conn.commit()
    conn.close()
    print(f'goal: {goal.name}, has been updated')

# delete goal
def delete_goal(goal_id: int) -> None:
    conn, cur = db_connect()
    command = '''DELETE FROM goal WHERE id = ?'''
    cur.execute(command, (goal_id))
    conn.commit()
    conn.close()
    print(f'goal: {goal_id}, has been deleted')

# get all user's goals
def get_user_goals(user_id: int) -> list[tuple]:
    conn, cur = db_connect()
    command = '''SELECT * FROM goal WHERE user_id = ?'''
    cur.execute(command, (user_id))
    data = cur.fetchall()
    conn.close()
    return data

# get goal by id
def get_goal_by_id(goal_id: int) -> tuple:
    conn, cur = db_connect()
    command = '''SELECT * FROM goal WHERE id = ?'''
    cur.execute(command, (goal_id))
    data = cur.fetchone()
    conn.close()
    return data

### INCOME
# create income
def create_income(income: dict) -> None:
    conn, cur = db_connect()
    command = '''INSERT INTO income(name, amount, effect_date, user_id, category_id)
                    VALUES (?, ?, ?, ?, ?)'''
    cur.execute(command, (income.name,
                          income.amount,
                          income.effect_date,
                          income.user_id,
                          income.category_id))
    conn.commit()
    conn.close()
    print(f'income: {income.name}, has been created')

# update income
def update_income(income: dict) -> None:
    conn, cur = db_connect()
    command = '''INSERT OR REPLACE INTO income(id, name, amount, effect_date, category_id)
                    VALUES(?, ?, ?, ?, ?)'''
    cur.execute(command, (income.id,
                          income.name,
                          income.amount,
                          income.effect_date,
                          income.category_id))
    conn.commit()
    conn.close()
    print(f'income: {income.id}, has been updated')
# delete income
def delete_income(income_id: int) -> None:
    conn, cur = db_connect()
    command = '''DELETE FROM income WHERE id = ?'''
    cur.execute(command, (income_id))
    conn.commit()
    conn.close()
    print(f'income: {income_id}, has been dleeted')

# get all user's income
def get_user_income(user_id: int) -> list[tuple]:
    conn, cur = db_connect()
    command = '''SELECT * FROM income WHERE user_id = ?'''
    cur.execute(command, (user_id))
    data = cur.fetchall()
    conn.close()
    return data

# get income by id
def get_income_by_id(income_id: int) -> tuple:
    conn, cur = db_connect()
    command = '''SELECT * FROM income WHERE id = ?'''
    cur.execute(command,(income_id))
    data = cur.fetchone()
    conn.close()
    return data

### EXPENSE
# create expense
def create_expense(expense: dict) -> None:
    conn, cur = db_connect()
    command = '''INSERT INTO expense(name, amount, effect_date, user_id, category_id, goal_id)
                    VALUES(?, ?, ?, ?, ?, ?)'''
    cur.execute(command, (expense.name,
                          expense.amount,
                          expense.effect_date,
                          expense.user_id,
                          expense.category_id,
                          expense.goal_id))
    conn.commit()
    conn.close()
    print(f'expense: {expense.id}, has been created')

# update expense
def update_expense(expense: dict) -> None:
    conn, cur = db_connect()
    command = '''INSERT OR REPLACE INTO expense(id, name, amount, effect_date, category_id, goal_id)'''
    cur.execute(command, (expense.id,
                          expense.name,
                          expense.amount,
                          expense.effect_date,
                          expense.category_id,
                          expense.goal_id))
    conn.commit()
    conn.close()
    print(f'expense: {expense.id}, has been updated')

# delete expense
def delete_expense(expense_id: int) -> None:
    conn, cur = db_connect()
    command = '''DELETE FROM expense WHERE id = ?'''
    cur.execute(command, (expense_id))
    conn.commit()
    conn.close()
    print(f'expense: {expense_id}, has been deleted')

# get all user's expenses
def get_user_expenses(user_id: int) -> list[tuple]:
    conn, cur = db_connect()
    command = '''SELECT * FROM expense WHERE user_id = ?'''
    cur.execute(command, (user_id))
    data = cur.fetchall()
    conn.close()
    return data

# get expense by id
def get_expense_by_id(expense_id: int) -> tuple:
    conn, cur = db_connect()
    command = '''SELECT * FROM expense WHERE id = ?'''
    cur.execute(command, (expense_id))
    data = cur.fetchone()
    conn.close()
    return data
