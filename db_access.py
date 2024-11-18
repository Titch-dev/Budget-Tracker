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

### USER
# create user
def create_user(user: User) -> None:
    conn, cur = db_connect()
    command = '''INSERT INTO user (email, password) 
                    VALUES (?, ?)'''
    cur.execute(command, (user.email, 
                          user.password))
    conn.commit()
    conn.close()
    print(f'user: {user.email}, has been created')

# update user
def update_user(user: User) -> None:
    conn, cur = db_connect()
    command = '''UPDATE user
                SET email = ?,
                    password = ?,
                    last_login = ?
                WHERE id = ?'''
    cur.execute(command, (user.email,
                          user.password,
                          user.last_login,
                          user.id))
    conn.commit()
    conn.close()
    print(f'user: {user.email}, has been updated')

# delete user
def delete_user(user_id: int) -> None:
    conn, cur = db_connect()
    command = '''DELETE FROM user WHERE id = ?'''
    cur.execute(command, (user_id,))
    conn.commit()
    conn.close()
    print(f'user: {user_id}, has been deleted')

# get user
def get_user_by_id(user_id: int) -> User:
    conn, cur = db_connect()
    command = '''SELECT * FROM user WHERE id = ?'''
    cur.execute(command, (user_id,))
    data = cur.fetchone()
    conn.close()
    try:
        user = User(id=data[0],
                    email=data[1],
                    password=data[2],
                    created_at=data[3],
                    last_login=data[4])
        return user
    except TypeError:
        return data


def get_user_by_email(email: str) -> User:
    conn, cur = db_connect()
    command = '''SELECT * FROM user WHERE email = ?'''
    cur.execute(command, (email,))
    data = cur.fetchone()
    conn.close()
    try:
        return User(id=data[0],
                    email=data[1],
                    password=data[2],
                    created_at=data[3],
                    last_login=data[4])
    except TypeError:
        return data

### CATEGORY
# create category
def create_category(category: Category) -> int:
    conn, cur = db_connect()
    command = '''INSERT INTO category(name, desc, budget, user_id)
                    VALUES(?, ?, ?, ?)'''
    cur.execute(command, (category.name,
                          category.desc,
                          category.budget,
                          category.user_id))
    conn.commit()
    print(f'category: {category.name}, has been created')
    category_id = cur.lastrowid
    conn.close()

    return category_id

# update category
def update_category(category: Category) -> None:
    conn, cur = db_connect()
    command = '''UPDATE
                    category
                SET
                    name = ?,
                    desc = ?,
                    budget = ?
                WHERE
                    id = ?'''
    cur.execute(command,(category.name,
                         category.desc,
                         category.budget,
                         category.id))
    conn.commit()
    conn.close()
    print(f'category: {category.name}, has been updated')

# delete Category
def delete_category(category_id: int) -> None:
    conn, cur = db_connect()
    command = '''DELETE FROM category WHERE id = ?'''
    cur.execute(command, (category_id,))
    conn.commit()
    conn.close()
    print(f'category: {category_id}, has been deleted')

# get all user's categories
def get_user_categories(user_id: int) -> list[Category]:
    conn, cur = db_connect()
    command = '''SELECT * FROM category WHERE user_id = ?'''
    cur.execute(command, (user_id,))
    data = cur.fetchall()
    conn.close()
    categories = []
    for entry in data:
        category = Category(id=entry[0],
                            name=entry[1],
                            desc=entry[2],
                            budget=entry[3],
                            created_at=entry[4],
                            user_id=entry[5])
        categories.append(category)

    return categories

# get category by ID
def get_category_by_id(cat_id:int) -> Category:
    conn, cur = db_connect()
    command = '''SELECT * FROM category WHERE id = ?'''
    cur.execute(command, (cat_id, ))
    data = cur.fetchone()
    conn.close()
    try:
        return Category(id=data[0],
                        name=data[1],
                        desc=data[2],
                        budget=data[3],
                        created_at=data[4],
                        user_id=data[5])
    except TypeError:
        return data

### GOAL
# create goal
def create_goal(goal: Goal) -> None:
    conn, cur = db_connect()
    command = '''INSERT INTO goal (name, desc, target, end_date, user_id)
                    VALUES(?, ?, ?, ?, ?)'''
    cur.execute(command, (goal.name,
                          goal.desc,
                          goal.target,
                          goal.end_date,
                          goal.user_id))
    conn.commit()
    print(f'goal: {goal.name}, has been created')
    goal_id = cur.lastrowid
    conn.close()

    return goal_id
# update goal
def update_goal(goal: Goal) -> None:
    conn, cur = db_connect()
    command = '''UPDATE 
                    goal
                SET
                    name = ?,
                    desc = ?,
                    target = ?,
                    end_date = ?
                WHERE
                    id = ?'''
    cur.execute(command, (goal.name,
                          goal.desc,
                          goal.target,
                          goal.end_date,
                          goal.id))
    conn.commit()
    conn.close()
    print(f'goal: {goal.name}, has been updated')

# delete goal
def delete_goal(goal_id: int) -> None:
    conn, cur = db_connect()
    command = '''DELETE FROM goal WHERE id = ?'''
    cur.execute(command, (goal_id, ))
    conn.commit()
    conn.close()
    print(f'goal: {goal_id}, has been deleted')

# get all user's goals
def get_user_goals(user_id: int) -> list[Goal]:
    conn, cur = db_connect()
    command = '''SELECT * FROM goal WHERE user_id = ?'''
    cur.execute(command, (user_id, ))
    data = cur.fetchall()
    conn.close()
    goals = []
    for row in data:
        goal = Goal(id=row[0],
                    name=row[1],
                    desc=row[2],
                    target=row[3],
                    end_date=row[4],
                    created_at=row[5],
                    user_id=row[6])
        goals.append(goal)

    return goals

# get goal by id
def get_goal_by_id(goal_id: int) -> Goal:
    conn, cur = db_connect()
    command = '''SELECT * FROM goal WHERE id = ?'''
    cur.execute(command, (goal_id,))
    data = cur.fetchone()
    conn.close()
    try:
        return Goal(id=data[0],
                    name=data[1],
                    desc=data[2],
                    target=data[3],
                    end_date=data[4],
                    created_at=data[5],
                    user_id=data[6])
    except TypeError:
        return data

### INCOME
# insert income
def create_income(income: Income, cat_id: int) -> None:
    conn, cur = db_connect()
    command = '''INSERT INTO income(name, amount, effect_date, user_id, category_id)
                    VALUES (?, ?, ?, ?, ?)'''
    cur.execute(command, (income.name,
                          income.amount,
                          income.effect_date,
                          income.user_id,
                          cat_id))
    conn.commit()
    conn.close()
    print(f'income: {income.name}, has been created')

# update income
def update_income(income: Income, cat_id: int) -> None:
    conn, cur = db_connect()
    command = f'''UPDATE 
                    income
                  SET 
                    name = ?,
                    amount = ?,
                    effect_date = ?,
                    category_id = ?
                  WHERE 
                    id = ?'''
    cur.execute(command, (income.name,
                          income.amount,
                          income.effect_date,
                          cat_id,
                          income.id))
    conn.commit()
    conn.close()
    print(f'income: {income.id}, has been updated')

# delete income
def delete_income(income_id: int) -> None:
    conn, cur = db_connect()
    command = '''DELETE FROM income WHERE id = ?'''
    cur.execute(command, (income_id, ))
    conn.commit()
    conn.close()
    print(f'income: {income_id}, has been dleeted')

# get all user's income
def get_user_income(user_id: int) -> list[Income]:
    conn, cur = db_connect()
    command = '''SELECT
                    i.id,
                    i.name,
                    i.amount,
                    i.effect_date,
                    i.created_at,
                    i.user_id,
                    c.name as category_name 
                 FROM
                    income i
                 INNER JOIN
                    category c
                 ON
                    i.category_id = c.id
                 WHERE 
                    i.user_id in (?)'''
    cur.execute(command, (user_id, ))
    data = cur.fetchall()
    conn.close()
    incomes = []
    try:
        for row in data:
            income = Income(id=row[0],
                            name=row[1],
                            amount=row[2],
                            effect_date=row[3],
                            created_at=row[4],
                            user_id=row[5],
                            category_name=row[6])
            incomes.append(income)

        return incomes
    except TypeError:
        return data
# get income by id
def get_income_by_id(income_id: int) -> Income:
    conn, cur = db_connect()
    command = '''SELECT
                    i.id,
                    i.name,
                    i.amount,
                    i.effect_date,
                    i.created_at,
                    i.user_id,
                    c.name as category_name 
                 FROM
                    income i
                 INNER JOIN
                    category c
                 ON
                    i.category_id = c.id
                 WHERE 
                    i.id = ?'''
    cur.execute(command,(income_id,))
    data = cur.fetchone()
    conn.close()
    try:
        return Income(id=data[0],
                      name=data[1],
                      amount=data[2],
                      effect_date=data[3],
                      created_at=data[4],
                      user_id=data[5],
                      category_name=data[6])
    except TypeError:
        return data

# get incomes by category
def get_income_by_category(category_id: int) -> list[Income]:
    conn, cur = db_connect()
    command = '''SELECT
                    i.id,
                    i.name,
                    i.amount,
                    i.effect_date,
                    i.created_at,
                    i.user_id,
                    c.name as category_name
                 FROM
                    income i
                 INNER JOIN
                    category c
                 ON
                    i.category_id = c.id
                 WHERE
                    c.id = ?'''
    cur.execute(command, (category_id, ))
    data = cur.fetchall()
    conn.close()
    incomes = []
    try:
        for row in data:
            income = Income(id=row[0],
                            name=row[1],
                            amount=row[2],
                            effect_date=row[3],
                            created_at=row[4],
                            user_id=row[5],
                            category_name=row[6])
            incomes.append(income)

        return incomes
    except TypeError:
        return data

### EXPENSE
# create expense
def create_expense(expense: Expense, category_id: int=None, goal_id: int=None) -> None:
    conn, cur = db_connect()
    command = '''INSERT INTO expense(name, amount, effect_date, user_id, category_id, goal_id)
                    VALUES(?, ?, ?, ?, ?, ?)'''
    cur.execute(command, (expense.name,
                          expense.amount,
                          expense.effect_date,
                          expense.user_id,
                          category_id,
                          goal_id))
    conn.commit()
    conn.close()
    print(f'expense: {expense.name}, has been created')

# update expense
def update_expense(expense: Expense, category_id, goal_id) -> None:
    conn, cur = db_connect()
    command = '''UPDATE 
                    expense
                 SET
                    name = ?,
                    amount = ?,
                    effect_date = ?,
                    category_id = ?,
                    goal_id = ?
                 WHERE
                    id = ?'''
    cur.execute(command, (expense.name,
                          expense.amount,
                          expense.effect_date,
                          category_id,
                          goal_id,
                          expense.id))
    conn.commit()
    conn.close()
    print(f'expense: {expense.id}, has been updated')

# delete expense
def delete_expense(expense_id: int) -> None:
    conn, cur = db_connect()
    command = '''DELETE FROM expense WHERE id = ?'''
    cur.execute(command, (expense_id, ))
    conn.commit()
    conn.close()
    print(f'expense: {expense_id}, has been deleted')

# get all user's expenses
def get_user_expenses(user_id: int) -> list[Expense]:
    conn, cur = db_connect()
    command = '''SELECT 
                    e.id,
                    e.name,
                    e.amount,
                    e.effect_date,
                    e.created_at,
                    e.user_id,
                    c.name as category_name,
                    g.name as goal_name
                FROM 
                    expense e 
                LEFT JOIN
                    category c
                ON 
                    e.category_id = c.id
                LEFT JOIN
                    goal g
                ON
                    e.goal_id = g.id
                WHERE 
                    e.user_id in (?)'''
    cur.execute(command, (user_id, ))
    data = cur.fetchall()
    conn.close()
    expenses = []
    try:
        for row in data:
            expense = Expense(id=row[0],
                              name=row[1],
                              amount=row[2],
                              effect_date=row[3],
                              created_at=row[4],
                              user_id=row[5],
                              category_name=row[6],
                              goal_name=row[7])
            expenses.append(expense)
        return expenses
    except TypeError:
        return data

# get expense by id
def get_expense_by_id(expense_id: int) -> Expense:
    conn, cur = db_connect()
    command = '''SELECT
                    e.id,
                    e.name,
                    e.amount,
                    e.effect_date,
                    e.created_at,
                    e.user_id,
                    c.name as category_name,
                    g.name as goal_name
                FROM 
                    expense e
                LEFT JOIN
                    category c
                ON
                    e.category_id = c.id
                LEFT JOIN
                    goal g
                ON
                    e.goal_id = g.id
                WHERE 
                    e.id = ?'''
    cur.execute(command, (expense_id, ))
    data = cur.fetchone()
    conn.close()
    try:
        return Expense(id=data[0],
                       name=data[1],
                       amount=data[2],
                       effect_date=data[3],
                       created_at=data[4],
                       user_id=data[5],
                       category_name=data[6],
                       goal_name=data[7])
    except TypeError:
        return data

# get expenses by category
def get_expenses_by_category(category_id: int):
    conn, cur = db_connect()
    command = '''SELECT
                    e.id,
                    e.name,
                    e.amount,
                    e.effect_date,
                    e.created_at,
                    e.user_id,
                    c.name as category_name,
                    g.name as goal_name
                 FROM
                    expense e
                 LEFT JOIN
                    category c
                 ON
                    e.category_id = c.id
                 LEFT JOIN
                    goal g
                 ON
                    e.goal_id = g.id
                 WHERE
                    e.category_id = ?'''
    cur.execute(command, (category_id, ))
    data = cur.fetchall()
    conn.close()
    expenses = []
    try:
        for row in data:
            expense = Expense(id=row[0],
                              name=row[1],
                              amount=row[2],
                              effect_date=row[3],
                              created_at=row[4],
                              user_id=row[5],
                              category_name=row[6],
                              goal_name=row[7])
            expenses.append(expense)
        return expenses
    except TypeError:
        return data


# get expenses by current month
def get_expenses_by_month(current_month: str, category_id: int):
    conn, cur = db_connect()
    command = '''SELECT
                    e.id,
                    e.name,
                    e.amount,
                    e.effect_date,
                    e.created_at,
                    e.user_id,
                    c.name as category_name,
                    g.name as goal_name
                 FROM
                    expense e
                 LEFT JOIN
                    category c
                 ON
                    e.category_id = c.id
                 LEFT JOIN
                    goal g
                 ON
                    e.goal_id = g.id
                 WHERE
                    e.effect_date LIKE ?
                 AND
                    e.category_id = ?'''
    cur.execute(command, (current_month + '%', category_id, ))
    data = cur.fetchall()
    conn.close()
    expenses = []
    try:
        for row in data:
            expense = Expense(id=row[0],
                              name=row[1],
                              amount=row[2],
                              effect_date=row[3],
                              created_at=row[4],
                              user_id=row[5],
                              category_name=row[6],
                              goal_name=row[7])
            expenses.append(expense)
        return expenses
    except TypeError:
        return data
