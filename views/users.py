import getpass

from datetime import datetime

from models import User

from services import (get_user_by_username, create_user, get_sum_of_user_incomes,
                      get_sum_of_user_expenses_to_date)

from general_utils import display_template

from templates import ADD_USER, DASHBOARD_MENU


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
    except AttributeError:
        print('User does not exist')


def register() -> User:
    """Check username is unique, create and return new user

    Returns:
        User: The newly created user
    """
    # Fallback mechanism to ensure password is valid
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


def dashboard_menu(user_id: int, username: str) -> None:
    """Display a summary of user's budgets

    Parameters:
        user_id (int): The ID of useer to filter by
        username (str): The username to display
    """
    # Get current day ("DD MMM YYYY")
    now = datetime.now().strftime('%d %b %Y')

    # Obtain the total income and expense to get balance
    sum_income = get_sum_of_user_incomes(user_id) or 0.00  # 0.00 if returns None
    sum_expense = get_sum_of_user_expenses_to_date(user_id) or 0.00  # 0.00 if returns None
    balance = sum_income - sum_expense

    # display the dashboard template with user details
    print(display_template(DASHBOARD_MENU,
                           username,
                           balance,
                           now))
