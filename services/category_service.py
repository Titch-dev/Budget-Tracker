from models import Category

from db_access import db_connect


def map_category(row: tuple) -> Category:
    return Category(id=row[0],
                    name=row[1],
                    desc=row[2],
                    budget=row[3],
                    cat_type=row[4],
                    created_at=row[5],
                    user_id=row[6])


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
    return map_category(data) if data else None


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
    try:
        return [map_category(row) for row in data]
    except TypeError:
        return data


def update_category(category: Category) -> None:
    """Function to update a category entry

    Parameters:
        category: Category object
    """
    conn, cur = db_connect()
    command = '''UPDATE category SET budget = ? WHERE id = ?'''
    cur.execute(command,(category.budget, category.id))
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
    try:
        return [map_category(row) for row in data]
    except TypeError:
        return data
