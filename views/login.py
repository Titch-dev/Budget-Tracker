from models.user import User

from db_access import get_user_by_email


def login() -> User:
    user_email = input('Email: ')
    password = input('Password: ')

    try:
        user = get_user_by_email(user_email)
        if password == user.password:
            return user
        else:
            print('Password does not match')
    except TypeError:
        print('User does not exist')