from datetime import datetime

from general_utils import display_template, date_formatter, amount_validator, pause_terminal

from templates import INCOME_ADD, INCOME_OPTION, CATEGORY_OPTION, INCOME_VIEW, INCOME_SUMMARY, SELECT_INCOME, \
    ERROR_MESSAGE
from models.income import Income

from views.categories import select_user_category, get_user_categories, set_category_budget, remove_delete_category

from db_access import create_income, get_user_income, get_income_by_category, delete_income, get_income_by_month, \
    get_user_categories_by_type, update_income


def add_income(user_id: int):
    """Take user input, create a new income entry, optionally link to a category

    Parameters:
        user_id (int): The ID of the user creating the income
    """
    print(INCOME_ADD)

    # Get income details
    name = input('Enter an income name: ').strip()
    amount = amount_validator(prompt='income')
    print('Enter the date this income will take effect')
    effect_date = date_formatter(full_date=True)

    # Create an income object without linking to a category
    income = Income.create(name, amount, effect_date, user_id)

    # Link category to income (if not none)
    category = select_user_category(user_id, cat_type='income')
    income.cat_id = category.id if category else None

    # Save income to the database
    create_income(income)


def track_incomes(incomes: list[Income], month: str = None):
    """Summarise and display income totals by category for a given list of incomes.

    Parameters:
        incomes (list[Income]): List of incomes to track.
        month (str): Optional month to include in the summary display.
    """
    if not incomes:
        print("No incomes to track")
        pause_terminal()
        return

    total = 0
    categories = dict()

    for income in incomes:
        total += income.amount
        if income.cat_name in categories.keys():
            categories[income.cat_name] += income.amount
        else:
            categories[income.cat_name] = income.amount

    # Display summary
    print(display_template(INCOME_SUMMARY, month or 'All Time', total))

    # print categorised income
    for name, amount in categories.items():
        print(f'      {name}:{' '*(20 - len(name))}R{amount}')
    print('-' * 72)

    pause_terminal()


def view_incomes(user_id: int) -> None:
    """View, update, or delete user incomes. Allows filtering by all-time or a specific month.

    Parameters:
        user_id (int): ID of the user viewing expenses.
    """
    while True:
        view_choice = input(INCOME_VIEW).strip()

        # Retrieve incomes based on user choice
        if view_choice == '1':  # get all incomes
            incomes = get_user_income(user_id)
            if not incomes:
                print(display_template(ERROR_MESSAGE, 'No incomes found'))
                return
            track_incomes(incomes)
            break
        elif view_choice == '2':  # get incomes by month
            search_month = date_formatter(full_date=False)
            month_name = datetime.strptime(search_month, '%Y-%m').strftime("%B")

            incomes = get_income_by_month(user_id, search_month)
            if not incomes:
                print(display_template(ERROR_MESSAGE, f'No incomes found for {month_name}'))
                continue
            track_incomes(incomes, month_name)
            break
        else:  # Exit or invalid option
            print('Exiting income viewer...')
            return

    # Display and interact with individual incomes
    ref_dict = {ref: income for ref, income in enumerate(incomes, start=1)}
    for ref, income in ref_dict.items():
        income.display_short(ref)

    while True:
        try:
            income_choice = int(input(SELECT_INCOME))
            selected_income = ref_dict.get(income_choice)
            if not selected_income:
                print('Not a valid selection')
                continue
            break
        except ValueError:
            print('Exiting income viewer...')
            return

    # Display detailed expense view and update/delete options
    selected_income.display_long()
    income_option = input(INCOME_OPTION)

    if income_option == "1":  # Update expense amount
        new_amount = amount_validator(prompt='new')
        selected_income.amount = new_amount
        update_income(selected_income)
    elif income_option == "2":  # Delete expense
        confirm = input('Are you sure you wish to delete this expense (y/n)?: ').strip().lower()
        if confirm == 'y':
            delete_income(selected_income.id)
        else:
            print('Income deletion canceled')
    else:
        print('Exiting income viewer...')


def view_incomes_by_category(user_id: int):
    """View incomes filtered by category and allow actions on categories.

    Parameters:
        user_id (int): ID of the user whose expenses are being managed.
    """
    # Retrieve and display income categories
    categories = get_user_categories_by_type(user_id, 'income')
    if not categories:
        print('No income categories found.')
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

    # Retrieve and display incomes for the selected category
    incomes = get_income_by_category(category.id)
    if not incomes:
        print(f'You don\'t have any incomes for {category.name} category!')
    else:
        for income in incomes:
            income.display_short()

    # Options for the selected category
    category_choice = input(display_template(CATEGORY_OPTION, category.name)).strip()

    if category_choice == '1':  # Change Category budget
        set_category_budget(category)
    elif category_choice == '2':  # Delete Category
        remove_delete_category(category.id, category.cat_type)