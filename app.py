# Utilities
from utilities.user_utils import login, register
from utilities.general_utils import display_formatter

# templates
from templates.templates import WELCOME_MENU, DASHBOARD_MENU, LOGOUT_MESSAGE, ERROR_MESSAGE



### Application start ###
user = None

while not user:
    menu_choice = input(WELCOME_MENU)

    if menu_choice == '1':  # Login
        user = login()
    elif menu_choice == '2':  # Register
        register()
    else:
        print(display_formatter(ERROR_MESSAGE, 'Please enter a valid option...'))

while user:
    menu_choice = input(DASHBOARD_MENU)

    if menu_choice == '1':  # Add expense
        pass
    elif menu_choice == '2':  # View expenses
        pass
    elif menu_choice == '3':  # View expenses by category 
        pass
    elif menu_choice == '4':  # Add income
        pass
    elif menu_choice == '5':  # View income
        pass
    elif menu_choice == '6':  # View income by category
        pass
    elif menu_choice == '7':  # Set budget for a category
        pass
    elif menu_choice == '8':  # View budget for a category
        pass
    elif menu_choice == '9':  # Set financial goals
        pass
    elif menu_choice == '10':  # View progress to financial goals
        pass
    elif menu_choice == '11':  # Quit
        print(display_formatter(LOGOUT_MESSAGE, user['email']))
        user = None
    else:
        print(display_formatter(ERROR_MESSAGE, 'Please enter a valid option...'))