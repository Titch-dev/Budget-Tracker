from models import User

from db_access import db_connect


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
