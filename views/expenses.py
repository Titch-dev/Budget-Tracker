from datetime import datetime

from templates import ADD_EXPENSE, SELECT_EXPENSE, EXPENSE_OPTION, CATEGORY_OPTION, EXPENSE_VIEW, \
    EXPENSE_SUMMARY, ERROR_MESSAGE, EXPENSE_LIST, EXPENSE_CATEGORY

from models.expense import Expense

from views.categories import select_user_category, remove_delete_category, set_category_budget
from views.goals import select_user_goal

from db_access import create_expense, get_user_expenses, get_expenses_by_category, update_expense, \
    delete_expense, get_user_categories_by_type, get_expenses_by_month

from general_utils import display_template, date_formatter, amount_validator, pause_terminal


def add_expense(user_id: int):
    """Take user input, create a new expense entry, optionally link to category or goal.

    Parameters:
        user_id (int): The ID of the user creating the expense
    """
    print(ADD_EXPENSE)

    # Get expense details
    name = input('Enter an expense name: ').strip()
    amount = amount_validator(prompt='expense')
    print('Enter the date the expense will leave your account')
    effect_date = date_formatter(full_date=True)

    # Create expense object without category or goal
    expense = Expense.create(name, amount, effect_date, user_id)

    # Link category to expense (if not none)
    category = select_user_category(user_id, cat_type='expense')
    expense.cat_id = category.id if category else None

    # Link goal to expense (if not none)
    goal = select_user_goal(user_id)
    expense.goal_id = goal.id if goal else None

    # Save expense to the database
    create_expense(expense)


def track_expenses(expenses: list[Expense], month: str = None):
    """Summarise and display expense totals by category for a given list of expenses.

    Parameters:
        expenses (list[Expense]): List of expenses to track.
        month (str): Optional month to include in the summary display.
    """
    if not expenses:
        print('No expenses to track.')
        pause_terminal()
        return

    total = 0
    categories = dict()

    for expense in expenses:
        total += expense.amount
        if expense.cat_name in categories.keys():
            categories[expense.cat_name] += expense.amount
        else:
            categories[expense.cat_name] = expense.amount

    # Display summary
    print(display_template(EXPENSE_SUMMARY, month or "All Time", total))

    # Print categorised expenses
    for name, amount in categories.items():
        print(f'      {name}:{' '*(20 - len(name))}R{amount}')
    print('-' * 72)

    pause_terminal()


def view_expenses(user_id: int) -> None:
    """View, update, or delete user expenses. Allows filtering by all-time or a specific month.

    Parameters:
        user_id (int): ID of the user viewing expenses.
    """

    while True:
        view_choice = input(EXPENSE_VIEW).strip()

        # Retrieve expenses based on user choice
        if view_choice == '1':  # get all expenses
            expenses = get_user_expenses(user_id)
            if not expenses:
                print("No expenses found")
                return
            track_expenses(expenses)  # Display expense totals by category
            break

        elif view_choice == '2':  # get expenses by month
            search_month = date_formatter(full_date=False)
            month_name = datetime.strptime(search_month, '%Y-%m').strftime("%B")
            expenses = get_expenses_by_month(user_id, search_month)
            if not expenses:
                print(display_template(ERROR_MESSAGE, f'No expenses found for {month_name}'))
                continue
            track_expenses(expenses, month_name)  # Display expense totals by category
            break

        else:  # Exit or invalid option
            print('Exiting expense viewer...')
            return

    # Display and interact with individual expenses
    print(EXPENSE_LIST)
    ref_dict = {ref: expense for ref, expense in enumerate(expenses, start=1)}
    for ref, expense in ref_dict.items():
        expense.display_short(ref)

    while True:
        try:
            expense_choice = int(input(SELECT_EXPENSE))
            selected_expense = ref_dict.get(expense_choice)
            if not selected_expense:
                print('Not a valid selection')
                continue
            break
        except ValueError:
            print('Exiting expense viewer...')
            return

    # Display detailed expense view and update/delete options
    selected_expense.display_long()
    expense_option = input(EXPENSE_OPTION).strip()

    if expense_option == "1":  # Update expense amount
        new_amount = amount_validator(prompt='new')
        selected_expense.amount = new_amount
        update_expense(selected_expense)
    elif expense_option == "2":  # Delete expense
        confirm = input('Are you sure you wish to delete this expense (y/n)?: ').strip().lower()
        if confirm == 'y':
            delete_expense(selected_expense.id)
        else:
            print('Expense deletion canceled')
    else:
        print('Exiting expense viewer...')


def view_expenses_by_category(user_id):
    """View expenses filtered by category and allow actions on categories.

    Parameters:
        user_id (int): ID of the user whose expenses are being managed.
    """
    # Retrieve and display users expense categories
    print(EXPENSE_CATEGORY)
    categories = get_user_categories_by_type(user_id, "expense")
    if not categories:
        print('No expense categories found.')
        return

    ref_dict = {ref: category for ref, category in enumerate(categories, start=1)}
    for ref, category in ref_dict.items():
        category.display_short(ref)

    # Select a category
    while True:
        try:
            ref_choice = int(input('Please enter the above \'ref\' for the category: ').strip())
            category = ref_dict.get(ref_choice)
            if not category:
                print('Please enter a valid \'ref\' number.')
                continue
            break
        except ValueError:
            print('Invalid input. Enter a \'ref\' number')

    # Retrieve and display expenses for the selected category
    expenses = get_expenses_by_category(category.id)
    if not expenses:
        print(f'You don\'t have any expenses for {category.name} category')
    else:
        for expense in expenses:
            expense.display_short()

    # Options for the selected category
    category_choice = input(display_template(CATEGORY_OPTION, category.name)).strip()

    if category_choice == '1':  # Change Category budget
        set_category_budget(category)
    elif category_choice == '2':  # Delete Category
        confirm = (input(f'Are you sure you want to delete the category {category.name} (y/n)?: ').strip().lower())
        if confirm == 'y':
            remove_delete_category(category.id, category.cat_type)
        else:
            print('Category deletion canceled.')
            return
