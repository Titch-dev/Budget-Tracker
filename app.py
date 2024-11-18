# Views
from views.login import login
from views.register import register
from views.expenses import add_expense, view_expenses, view_expenses_by_category
from views.incomes import add_income, view_incomes, view_incomes_by_category
from views.categories import set_category_budget, view_category_budget
from views.goals import add_goal, view_goals_progress

# Utilities
from general_utils import display_formatter

# templates
from templates import WELCOME_MENU, DASHBOARD_MENU, LOGOUT_MESSAGE, ERROR_MESSAGE


### Application start ###
def app_logic():

    user = None

    while not user:
        menu_choice = input(WELCOME_MENU)

        if menu_choice == '1':  # Login
            user = login()
        elif menu_choice == '2':  # Register
            user = register()
        else:
            print(display_formatter(ERROR_MESSAGE, 'Please enter a valid option...'))

    while user:
        menu_choice = input(DASHBOARD_MENU)

        if menu_choice == '1':  # Add expense
            add_expense(user.id)
        elif menu_choice == '2':  # View expenses
            view_expenses(user.id)
        elif menu_choice == '3':  # View expenses by category
            view_expenses_by_category(user.id)
        elif menu_choice == '4':  # Add income
            add_income(user.id)
        elif menu_choice == '5':  # View income
            view_incomes(user.id)
        elif menu_choice == '6':  # View income by category
            view_incomes_by_category(user.id)
        elif menu_choice == '7':  # Set budget for a category
            set_category_budget(user.id)
        elif menu_choice == '8':  # View budget for a category
            view_category_budget(user.id)
        elif menu_choice == '9':  # Set financial goals
            add_goal(user.id)
        elif menu_choice == '10':  # View progress to financial goals
            view_goals_progress(user.id)
        elif menu_choice == '11':  # Quit
            print(display_formatter(LOGOUT_MESSAGE, user.email))
            user = None
        else:
            print(display_formatter(ERROR_MESSAGE, 'Please enter a valid option...'))