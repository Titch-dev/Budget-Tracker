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


##### USER #####
def get_user_by_username(username: str) -> User | None:
    """Get a user entry by username or return None

    Parameters:
        username (str): The username of the user to filter by.

    Returns:
        User | None:
    """
    conn, cur = db_connect()
    command = '''SELECT * FROM user WHERE username = ?'''
    cur.execute(command, (username,))
    data = cur.fetchone()
    conn.close()
    try:
        return User(id=data[0],
                    username=data[1],
                    password=data[2],
                    created_at=data[3],
                    last_login=data[4])
    except TypeError:
        return data


def create_user(user: User) -> None:
    """Function to create a user entry

    Parameters:
        user: User object
    """
    conn, cur = db_connect()
    command = '''INSERT INTO user (username, password) 
                    VALUES (?, ?)'''
    cur.execute(command, (user.username,
                          user.password))
    conn.commit()
    conn.close()
    print(f'User: {user.username}, has been created')


##### CATEGORY #####
def get_category_by_id(cat_id: int) -> Category:
    """Function to get a Category by id

    Parameters:
        cat_id: Int

    Returns:
        A Category object
    """
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
                        cat_type=data[4],
                        created_at=data[5],
                        user_id=data[6])
    except TypeError:
        return data


def create_category(category: Category) -> int:
    """Function to create a category entry

    Parameters:
        category: Category

    Returns:
        category_id: Int
    """
    conn, cur = db_connect()
    command = '''INSERT INTO category(name, desc, budget, cat_type, user_id)
                    VALUES(?, ?, ?, ?, ?)'''
    cur.execute(command, (category.name,
                          category.desc,
                          category.budget,
                          category.cat_type,
                          category.user_id))
    conn.commit()
    print(f'category: {category.name}, has been created')
    category_id = cur.lastrowid
    conn.close()

    return category_id


def get_user_categories(user_id: int) -> list[Category] | None:
    """Function to get a list of categories

    Parameters:
        user_id: Int

    Returns:
        list of Category objects
    """
    conn, cur = db_connect()
    command = '''SELECT * FROM category WHERE user_id = ?'''
    cur.execute(command, (user_id,))
    data = cur.fetchall()
    conn.close()
    categories = []
    try:
        for row in data:
            category = Category(id=row[0],
                                name=row[1],
                                desc=row[2],
                                budget=row[3],
                                cat_type=row[4],
                                created_at=row[5],
                                user_id=row[6])
            categories.append(category)

        return categories
    except TypeError:
        return data


def update_category(category: Category) -> None:
    """Function to update a category entry

    Parameters:
        category: Category object
    """
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


def delete_category(category_id: int) -> None:
    """Function to delete a category entry

    Parameters:
        category_id: Int
    """
    conn, cur = db_connect()
    command = '''DELETE FROM category WHERE id = ?'''
    cur.execute(command, (category_id,))
    conn.commit()
    conn.close()
    print(f'category: {category_id}, has been deleted')


def get_user_categories_by_type(user_id: int, cat_type: str) -> list[Category] | None:
    """Function to get a list of categories by category type

    Parameters:
        user_id: Int
        cat_type: Int

    Returns:
        list of Category objects
    """
    conn, cur = db_connect()
    command = '''SELECT * FROM category WHERE user_id = ? AND cat_type = ?'''
    cur.execute(command, (user_id, cat_type, ))
    data = cur.fetchall()
    conn.close()
    categories = list()
    try:
        for row in data:
            category = Category(id=row[0],
                                name=row[1],
                                desc=row[2],
                                budget=row[3],
                                cat_type=row[4],
                                created_at=row[5],
                                user_id=row[6])
            categories.append(category)

        return categories
    except TypeError:
        return data


##### GOAL #####
def get_goal_by_id(goal_id: int) -> Goal | None:
    """Function to get a Goal by the id

    Parameters:
        goal_id: Int

    Returns:
        A Goal object
    """
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


def create_goal(goal: Goal) -> int:
    """Function to create a Goal and return the id

    Parameters:
        goal (Goal):

    Returns:
        An Integer - Goal id
    """
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


def get_user_goals(user_id: int) -> list[Goal] | None:
    """Function to get list of user Goal objects

    Parameters:
        user_id: Int

    Returns:
        A list of Goal objects
    """
    conn, cur = db_connect()
    command = '''SELECT * FROM goal WHERE user_id = ?'''
    cur.execute(command, (user_id, ))
    data = cur.fetchall()
    conn.close()
    goals = []
    try:
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
    except TypeError:
        return data



##### INCOME #####
def get_income_by_id(income_id: int) -> Income | None:
    """Function to get an Income by the id

    Parameters:
        income_id: int

    Returns:
        An Income object
    """
    conn, cur = db_connect()
    command = '''SELECT
                    i.id,
                    i.name,
                    i.amount,
                    i.effect_date,
                    i.created_at,
                    i.user_id,
                    i.category_id,
                    c.name as category_name 
                 FROM
                    income i
                 LEFT JOIN
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
                      cat_id=data[6],
                      cat_name=data[7])
    except TypeError:
        return data


def create_income(income: Income) -> int:
    """Function to create an Income entry and return the id

    Parameters:
        income: Income

    Returns:
        An Integer - Income id
    """
    conn, cur = db_connect()
    command = '''INSERT INTO income(name, amount, effect_date, user_id, category_id)
                    VALUES (?, ?, ?, ?, ?)'''
    cur.execute(command, (income.name,
                          income.amount,
                          income.effect_date,
                          income.user_id,
                          income.cat_id))
    conn.commit()
    print(f'income: {income.name}, has been created')
    income_id = cur.lastrowid
    conn.close()

    return income_id


def get_user_income(user_id: int) -> list[Income] | None:
    """Function to get a list of Income objects

    Parameters:
        user_id: Int

    Returns:
        An list of Income objects
    """
    conn, cur = db_connect()
    command = '''SELECT
                    i.id,
                    i.name,
                    i.amount,
                    i.effect_date,
                    i.created_at,
                    i.user_id,
                    i.category_id,
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
                            cat_id=row[6],
                            cat_name=row[7])
            incomes.append(income)

        return incomes
    except TypeError:
        return data


def get_income_by_category(cat_id: int) -> list[Income] | None:
    """Function to get a list of Income objects by category

    Parameters:
        cat_id: Int

    Returns:
        A list of Income objects
    """
    conn, cur = db_connect()
    command = '''SELECT
                    i.id,
                    i.name,
                    i.amount,
                    i.effect_date,
                    i.created_at,
                    i.user_id,
                    i.category_id,
                    c.name as category_name
                 FROM
                    income i
                 INNER JOIN
                    category c
                 ON
                    i.category_id = c.id
                 WHERE
                    c.id = ?'''
    cur.execute(command, (cat_id, ))
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
                            cat_id=row[6],
                            cat_name=row[7])
            incomes.append(income)

        return incomes

    except TypeError:
        return data


def update_income(income: Income) -> None:
    """Function to update an Income entry

    Parameters:
        income: Income
    """
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
                          income.cat_id,
                          income.id))
    conn.commit()
    conn.close()
    print(f'income: {income.id}, has been updated')


def update_income_category_to_null(cat_id: int):
    conn, cur = db_connect()
    try:
        command = '''UPDATE
                            income
                        SET
                            category_id = NULL
                        WHERE
                            category_id = ?'''
        cur.execute(command, (cat_id,))
        conn.commit()
        rows_affected = cur.rowcount
        print(f"{rows_affected} income entries updated.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()


def delete_income(income_id: int) -> None:
    """Function to delete an Income entry

    Parameters:
        income_id: Int
    """
    conn, cur = db_connect()
    command = '''DELETE FROM income WHERE id = ?'''
    cur.execute(command, (income_id, ))
    conn.commit()
    conn.close()
    print(f'income: {income_id}, has been deleted')


def get_income_by_month(user_id: int, month: str) -> list[Income] | None:
    """Get a list of Income objects by filtered by month and user

    Parameters:
        user_id (int): The ID of the user to filter by
        month (str): Date string to filter by - format 'YY-MM'

    Returns:
        List[Income]: A list of Income objects for a given month
    """
    conn, cur = db_connect()
    command = '''SELECT
                        i.id,
                        i.name,
                        i.amount,
                        i.effect_date,
                        i.created_at,
                        i.user_id,
                        i.category_id,
                        c.name as category_name
                     FROM
                        income i
                     INNER JOIN
                        category c
                     ON
                        i.category_id = c.id
                     WHERE
                        i.effect_date LIKE ?
                     AND
                        i.user_id = ?'''
    cur.execute(command, (month + '%', user_id))
    data = cur.fetchall()
    conn.close()
    incomes = list()
    try:
        for row in data:
            income = Income(id=row[0],
                            name=row[1],
                            amount=row[2],
                            effect_date=row[3],
                            created_at=row[4],
                            user_id=row[5],
                            cat_id=row[6],
                            cat_name=row[7])
            incomes.append(income)

        return incomes

    except TypeError:
        return data


def get_sum_of_user_incomes(user_id: int) -> int:
    """Get the aggregated sum of all incomes filtered by user_id

    Parameters:
        user_id (int): The ID of the user to filter by

    Returns:
        int: The aggregated sum of all incomes
    """
    conn, cur = db_connect()
    command = '''SELECT
                    SUM(amount)
                FROM 
                    income
                WHERE
                    user_id = ?
                AND
                    effect_date < DATE('now')'''
    cur.execute(command, (user_id, ))
    result = cur.fetchone()
    conn.close()
    return result[0]


##### EXPENSE #####
def get_expense_by_id(expense_id: int) -> Expense | None:
    """Function to get an Expense object by the id

    Parameters:
        expense_id: Int

    Returns:
        An Expense object
    """
    conn, cur = db_connect()
    command = '''SELECT
                    e.id,
                    e.name,
                    e.amount,
                    e.effect_date,
                    e.created_at,
                    e.user_id,
                    e.category_id,
                    c.name as category_name,
                    e.goal_id,
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
                       cat_id=data[6],
                       cat_name=data[7],
                       goal_id=data[8],
                       goal_name=data[9])
    except TypeError:
        return data


def create_expense(expense: Expense) -> int:
    """Function to create an Expense entry and return the id

    Parameters:
        expense: Expense

    Returns:
        An Integer - Expense id
    """
    conn, cur = db_connect()
    command = '''INSERT INTO expense(name, amount, effect_date, user_id, category_id, goal_id)
                    VALUES(?, ?, ?, ?, ?, ?)'''
    cur.execute(command, (expense.name,
                          expense.amount,
                          expense.effect_date,
                          expense.user_id,
                          expense.cat_id,
                          expense.goal_id))
    conn.commit()
    print(f'expense: {expense.name}, has been created')
    expense_id = cur.lastrowid
    conn.close()
    return expense_id


def get_user_expenses(user_id: int) -> list[Expense] | None:
    """Function to get a list of user's Expense objects

    Parameters:
        user_id: int

    Returns:
        A list of Expense objects
    """
    conn, cur = db_connect()
    command = '''SELECT 
                    e.id,
                    e.name,
                    e.amount,
                    e.effect_date,
                    e.created_at,
                    e.user_id,
                    e.category_id,
                    c.name as category_name,
                    e.goal_id,
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
    expenses = list()
    try:
        for row in data:
            expense = Expense(id=row[0],
                              name=row[1],
                              amount=row[2],
                              effect_date=row[3],
                              created_at=row[4],
                              user_id=row[5],
                              cat_id=row[6],
                              cat_name=row[7],
                              goal_id=row[8],
                              goal_name=row[9])
            expenses.append(expense)
        return expenses
    except TypeError:
        return data


def get_expenses_by_category(cat_id: int) -> list[Expense]:
    """Function to get a list of Expense objects by category id

    Parameters:
        cat_id: Int

    Returns:
        A list of Expense objects
    """
    conn, cur = db_connect()
    command = '''SELECT
                    e.id,
                    e.name,
                    e.amount,
                    e.effect_date,
                    e.created_at,
                    e.user_id,
                    e.category_id,
                    c.name as category_name,
                    e.goal_id,
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
    cur.execute(command, (cat_id, ))
    data = cur.fetchall()
    conn.close()
    expenses = list()
    try:
        for row in data:
            expense = Expense(id=row[0],
                              name=row[1],
                              amount=row[2],
                              effect_date=row[3],
                              created_at=row[4],
                              user_id=row[5],
                              cat_id=row[6],
                              cat_name=row[7],
                              goal_id=row[8],
                              goal_name=row[9])
            expenses.append(expense)
        return expenses
    except TypeError:
        return data


def update_expense(expense: Expense) -> None:
    """Function to update an Expense entry

    Parameters:
        expense: Expense
    """
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
                          expense.cat_id,
                          expense.goal_id,
                          expense.id))
    conn.commit()
    conn.close()
    print(f'expense: {expense.id}, has been updated')


def update_expenses_category_to_null(cat_id) -> None:
    conn, cur = db_connect()
    try:
        command = '''UPDATE 
                        expense
                    SET
                        category_id = null
                    WHERE
                        category_id = ?'''
        cur.execute(command, (cat_id,))
        conn.commit()
        rows_affected = cur.rowcount
        print(f'{rows_affected} expense entries updated')
    except sqlite3.Error as e:
        print(f'An error has occurred: {e}')
    finally:
        conn.close()


def delete_expense(expense_id: int) -> None:
    """Function to delete an Expense entry

    Parameters:
        expense_id: Int
    """
    conn, cur = db_connect()
    command = '''DELETE FROM expense WHERE id = ?'''
    cur.execute(command, (expense_id, ))
    conn.commit()
    conn.close()
    print(f'expense: {expense_id}, has been deleted')


def get_expenses_by_month(user_id: int, month: str) -> list[Expense] | None:
    """Get a list of Expense objects by user id and month

    Parameters:
        user_id (int): The ID of the user to filter by
        month (str): Date string to filter by - format 'YY-MM'

    Returns:
        List[Expense]: A list of Expense objects for a given month
    """
    conn, cur = db_connect()
    command = '''SELECT
                    e.id,
                    e.name,
                    e.amount,
                    e.effect_date,
                    e.created_at,
                    e.user_id,
                    e.category_id,
                    c.name as category_name,
                    e.goal_id,
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
                    e.user_id = ?'''
    cur.execute(command, (month + '%', user_id))
    data = cur.fetchall()
    conn.close()
    expenses = list()
    try:
        for row in data:
            expense = Expense(id=row[0],
                              name=row[1],
                              amount=row[2],
                              effect_date=row[3],
                              created_at=row[4],
                              user_id=row[5],
                              cat_id=row[6],
                              cat_name=row[7],
                              goal_id=row[8],
                              goal_name=row[9])
            expenses.append(expense)
        return expenses
    except TypeError:
        return data


def get_expenses_by_goal(goal_id: int) -> list[Expense]:
    """Function to get a list of Expense objects by goal id

    Parameters:
        goal_id: Int

    Returns:
        A list of Expense objects
    """
    conn, cur = db_connect()
    command = '''SELECT
                    e.id,
                    e.name,
                    e.amount,
                    e.effect_date,
                    e.created_at,
                    e.user_id,
                    e.category_id,
                    c.name as category_name,
                    e.goal_id,
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
                    e.goal_id = ?'''
    cur.execute(command, (goal_id, ))
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
                              cat_id=row[6],
                              cat_name=row[7],
                              goal_id=row[8],
                              goal_name=row[9])
            expenses.append(expense)
        return expenses
    except TypeError:
        return data


def get_sum_of_user_expenses_to_date(user_id: int) -> int:
    """Get the aggregated sum of all expenses filtered by user_id

    Parameters:
        user_id (int): The ID of the user to filter by

    Returns:
        int: The aggregated sum of all expenses
    """
    conn, cur = db_connect()
    command = '''SELECT
                    SUM(amount)
                FROM 
                    expense
                WHERE
                    user_id = ?
                AND
                    effect_date < DATE('now')'''
    cur.execute(command, (user_id, ))
    result = cur.fetchone()
    conn.close()
    return result[0]
