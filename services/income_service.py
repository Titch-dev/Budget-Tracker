import sqlite3

from models import Income

from db_access import db_connect


def map_income(row: tuple) -> Income:
    return Income(id=row[0],
                  name=row[1],
                  amount=row[2],
                  effect_date=row[3],
                  created_at=row[4],
                  user_id=row[5],
                  cat_id=row[6],
                  cat_name=row[7])


def get_income_by_id(income_id: int) -> Income | None:
    """Function to get an Income by the id

    Parameters:
        income_id: int

    Returns:
        An Income object
    """
    conn, cur = db_connect()
    command = '''SELECT
                    i.id, i.name, i.amount, i.effect_date, i.created_at,
                    i.user_id, i.category_id, c.name as category_name 
                 FROM income i
                 LEFT JOIN category c ON i.category_id = c.id
                 WHERE i.id = ?'''
    cur.execute(command, (income_id,))
    data = cur.fetchone()
    conn.close()
    return map_income(data) if data else None


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
                    i.id, i.name, i.amount, i.effect_date, i.created_at,
                    i.user_id, i.category_id, c.name as category_name 
                 FROM income i
                 INNER JOIN category c ON i.category_id = c.id
                 WHERE i.user_id in (?)'''
    cur.execute(command, (user_id, ))
    data = cur.fetchall()
    conn.close()
    try:
        return [map_income(row) for row in data]
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
                    i.id, i.name, i.amount, i.effect_date, i.created_at,
                    i.user_id, i.category_id, c.name as category_name
                 FROM income i
                 INNER JOIN category c
                 ON i.category_id = c.id
                 WHERE c.id = ?'''
    cur.execute(command, (cat_id, ))
    data = cur.fetchall()
    conn.close()
    try:
        return [map_income(row) for row in data]
    except TypeError:
        return data


def update_income(income: Income) -> None:
    """Function to update an Income entry

    Parameters:
        income: Income
    """
    conn, cur = db_connect()
    command = f'''UPDATE income SET amount = ? WHERE id = ?'''
    cur.execute(command, (income.amount, income.id))
    conn.commit()
    conn.close()
    print(f'income: {income.id}, has been updated')


def update_income_category_to_null(cat_id: int):
    conn, cur = db_connect()
    try:
        command = '''UPDATE income SET category_id = NULL WHERE category_id = ?'''
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
                    i.id, i.name, i.amount, i.effect_date, i.created_at,
                    i.user_id, i.category_id, c.name as category_name
                FROM income i
                INNER JOIN category c ON i.category_id = c.id
                WHERE i.effect_date LIKE ?
                AND i.user_id = ?'''
    cur.execute(command, (month + '%', user_id))
    data = cur.fetchall()
    conn.close()
    try:
        return [map_income(row) for row in data]
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
    command = '''SELECT SUM(amount)
                FROM income
                WHERE user_id = ?
                AND effect_date < DATE('now')'''
    cur.execute(command, (user_id, ))
    result = cur.fetchone()
    conn.close()
    return result[0]
