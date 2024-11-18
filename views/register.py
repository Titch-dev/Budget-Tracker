from models.user import User

from db_access import create_user, get_user_by_email

from general_utils import display_formatter

from templates import ERROR_MESSAGE


def register() -> User:

    user_email = input('Please enter your email: ')
    # TODO: email validation
    exists = get_user_by_email(user_email)

    if exists:
        print(display_formatter(ERROR_MESSAGE, 'Email already exists'))
    else:
        user_password = input('Please enter your password: ')
        new_user = User.create(user_email, user_password)
        create_user(new_user)
        return get_user_by_email(user_email)

