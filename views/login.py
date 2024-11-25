import getpass

from models.user import User

from db_access import get_user_by_username


def login() -> User | None:
    """Takes user input and returns a user object

    Returns:
        User | None: matched user returned, or None
    """
    username = input('Enter Username: ').strip()
    password = getpass.getpass('Enter Password: ').strip()

    try:
        user = get_user_by_username(username)
        if password == user.password:
            return user
        else:
            print('Password does not match')
    except TypeError:
        print('User does not exist')
