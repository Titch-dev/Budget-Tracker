import sqlite3

from models import Expense

from db_access import db_connect


def map_expense(row: tuple) -> Expense:
    return Expense(id=row[0],
                   name=row[1],
                   amount=row[2],
                   effect_date=row[3],
                   created_at=row[4],
                   user_id=row[5],
                   cat_id=row[6],
                   cat_name=row[7],
                   goal_id=row[8],
                   goal_name=row[9])


def get_expense_by_id(expense_id: int) -> Expense | None:
    """Function to get an Expense object by the id

    Parameters:
        expense_id: Int

    Returns:
        An Expense object
    """
    conn, cur = db_connect()
    command = '''SELECT
                    e.id, e.name, e.amount, e.effect_date, e.created_at,
                    e.user_id, e.category_id, c.name as category_name,
                    e.goal_id, g.name as goal_name
                FROM expense e
                LEFT JOIN category c ON e.category_id = c.id
                LEFT JOIN goal g ON e.goal_id = g.id
                WHERE e.id = ?'''
    cur.execute(command, (expense_id, ))
    data = cur.fetchone()
    conn.close()
    return map_expense(data) if data else None


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
                    e.id, e.name, e.amount, e.effect_date, e.created_at,
                    e.user_id, e.category_id, c.name as category_name,
                    e.goal_id, g.name as goal_name
                FROM expense e 
                LEFT JOIN category c ON e.category_id = c.id
                LEFT JOIN goal g ON e.goal_id = g.id
                WHERE e.user_id in (?)'''
    cur.execute(command, (user_id, ))
    data = cur.fetchall()
    conn.close()
    try:
        return [map_expense(row) for row in data]
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
                    e.id, e.name, e.amount, e.effect_date, e.created_at,
                    e.user_id, e.category_id, c.name as category_name,
                    e.goal_id, g.name as goal_name
                 FROM expense e
                 LEFT JOIN category c ON e.category_id = c.id
                 LEFT JOIN goal g ON e.goal_id = g.id
                 WHERE e.category_id = ?'''
    cur.execute(command, (cat_id, ))
    data = cur.fetchall()
    conn.close()
    try:
        return [map_expense(row) for row in data]
    except TypeError:
        return data


def update_expense(expense: Expense) -> None:
    """Function to update an Expense entry

    Parameters:
        expense: Expense
    """
    conn, cur = db_connect()
    command = '''UPDATE expense SET amount = ? WHERE id = ?'''
    cur.execute(command, (expense.amount, expense.id))
    conn.commit()
    conn.close()
    print(f'expense: {expense.id}, has been updated')


def update_expenses_category_to_null(cat_id) -> None:
    conn, cur = db_connect()
    try:
        command = '''UPDATE expense SET category_id = NULL WHERE category_id = ?'''
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
                    e.id, e.name, e.amount, e.effect_date, e.created_at,
                    e.user_id, e.category_id, c.name as category_name,
                    e.goal_id, g.name as goal_name
                 FROM expense e
                 LEFT JOIN category c ON e.category_id = c.id
                 LEFT JOIN goal g ON e.goal_id = g.id
                 WHERE e.effect_date LIKE ?
                 AND e.user_id = ?'''
    cur.execute(command, (month + '%', user_id))
    data = cur.fetchall()
    conn.close()
    try:
        return [map_expense(row) for row in data]
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
                    e.id, e.name, e.amount, e.effect_date, e.created_at,
                    e.user_id, e.category_id, c.name as category_name,
                    e.goal_id, g.name as goal_name
                 FROM expense e
                 LEFT JOIN category c ON e.category_id = c.id
                 LEFT JOIN goal g ON e.goal_id = g.id
                 WHERE e.goal_id = ?'''
    cur.execute(command, (goal_id, ))
    data = cur.fetchall()
    conn.close()
    try:
        return [map_expense(row) for row in data]
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
    command = '''SELECT SUM(amount) 
                FROM expense
                WHERE user_id = ?
                AND effect_date < DATE('now')'''
    cur.execute(command, (user_id, ))
    result = cur.fetchone()
    conn.close()
    return result[0]
