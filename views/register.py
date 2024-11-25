import getpass

from models.user import User

from db_access import create_user, get_user_by_username
from templates import ADD_USER


def register() -> User:
    """Check username is unique, create and return new user

    Returns:
        User: The newly created user
    """
    # Fallback mechanism to ensure username is unique
    while True:
        print(ADD_USER)

        username = input('Please enter a username: ').strip()
        if not username:
            print('Username cannot be blank')
            continue

        if get_user_by_username(username):
            print('Username already exists')
            continue

        break

    # Fallback mechanism to ensure password is valid
    while True:
        password = getpass.getpass('Please enter your password: ')
        if len(password) < 6:
            print('The password must be at least 6 characters long')
            continue

        confirm_password = getpass.getpass('Please confirm your password: ')
        if password != confirm_password:
            print('The passwords don\'t match up')
            continue

        break

    # Create and return new user
    new_user = User.create(username=username, password=password)
    create_user(new_user)
    print("User registered successfully!")
    return get_user_by_username(username)
