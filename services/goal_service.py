from models import Goal

from db_access import db_connect


def map_goal(row: tuple) -> Goal:
    return Goal(id=row[0],
                name=row[1],
                desc=row[2],
                target=row[3],
                end_date=row[4],
                created_at=row[5],
                user_id=row[6])


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
    return map_goal(data) if data else None


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
    try:
        return [map_goal(row) for row in data]
    except TypeError:
        return data
