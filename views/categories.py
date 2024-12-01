from datetime import datetime

from models import Category

from services import (get_user_categories, create_category, update_category,
                      get_user_categories_by_type, get_category_by_id, delete_category,
                      update_income_category_to_null, get_expenses_by_month,
                      update_expenses_category_to_null)

from general_utils import display_template, date_formatter, pause_terminal, amount_validator

from templates import SELECT_CATEGORY, ADD_CATEGORY, CATEGORY_BUDGET


def is_category_name_taken(user_id: int, name: str) -> bool:
    """Returns True if name already taken, and False if not

    Parameters:
        user_id (int): The ID of the user to filter by
        name (str): The category name to check if already exists

    Returns:
        True | False: True if name exists and False if not"""
    categories = get_user_categories(user_id)
    try:
        for category in categories:
            if name.strip() == category.name:
                return True
        return False
    except TypeError:
        return False


def add_category(user_id: int, cat_type: str) -> Category | None:
    """Take user input, return a newly created category

    Parameters:
        user_id (int): The user's ID.
        cat_type (str): The type of category to select.

    Returns:
        Category: A newly created category
    """
    print(ADD_CATEGORY)

    # fullback mechanism: Get and validate a category name
    while True:
        name = input('Enter a name for the category: ').strip()
        if not name:
            print('Name cannot be empty.')
            continue
        if is_category_name_taken(user_id, name):
            print('Category name already taken.')
            continue
        break

    # Not a required field
    desc = input('Enter a short description for the category: ').strip()

    # Validate a budget
    if cat_type == 'income':
        budget = 0.00  # Budget not required for income category
    elif cat_type == 'expense':
        budget = amount_validator(prompt='monthly budget')

    # Create the new category
    new_category = Category.create(
        name=name,
        desc=desc,
        budget=budget,
        cat_type=cat_type,
        user_id=user_id)

    # Save and retrieve the category
    try:
        category_id = create_category(new_category)
        category = get_category_by_id(category_id)
        return category
    except Exception as e:
        print(f'An error has occurred while creating the category: {e}')
        return None


def select_user_category(user_id: int, cat_type: str) -> Category | None:
    """Take User input and return a Category.

    Parameters:
        user_id (int): The user's ID.
        cat_type (str): The type of category to select.

    Returns:
        Category | None: The selected category, a newly added one, or None.
    """
    categories = get_user_categories_by_type(user_id, cat_type)

    if not categories:
        print("No categories available.")
        choice = input("Would you like to add a new category? (y/n): ").strip().lower()
        if choice == 'y':
            return add_category(user_id, cat_type)
        return None

    ref_dict = {ref: category for ref, category in enumerate(categories, start=1)}

    # Display available categories
    for ref, category in ref_dict.items():
        category.display_short(ref)

    ADD_OPTION = len(categories) + 1

    try:
        choice = int(input(display_template(SELECT_CATEGORY, ADD_OPTION, cat_type)))
    except ValueError:
        return None

    if choice in ref_dict:
        return ref_dict[choice]  # return the category
    elif choice == ADD_OPTION:
        return add_category(user_id, cat_type)
    else:
        return None


def remove_delete_category(cat_id: int, cat_type: str) -> None:
    """Remove the category id from income and expense entries, then delete
    the category

    Parameters:
        cat_id (int): Category ID
        cat_type (str): The type of category to select
    """
    try:
        # Delete category id from income
        if cat_type == 'income':
            update_income_category_to_null(cat_id)

        # Delete category id from expenses
        elif cat_type == 'expense':
            update_expenses_category_to_null(cat_id)

        delete_category(cat_id)
    except Exception as e:
        print(f'An error had occurred while removing the category: {e}')


def set_category_budget(category: Category):
    """Take user input to set the budget property of a category entry

    Parameters:
        category (Category): The category selected for updating"""

    while True:
        try:
            new_budget = amount_validator('new budget')

            if new_budget < 0:
                print('The budget cannot be negative.')
                continue

            category.budget = new_budget
            update_category(category)
            break

        except ValueError:
            print('Please enter a valid number')
            continue


def view_category_budget(user_id: int):
    """Display the budget information for a selected category
    for a specific month

    Parameters:
        user_id (int): The ID of the user
    """

    # Prompt user to select a month
    print('Please choose the month you wish to see the budget for a category')
    search_date = date_formatter(full_date=False)  # Returns a 'YYYY-MM' formatted string

    # Retrieve the expenditures for the month
    expenses = get_expenses_by_month(user_id, search_date)
    if not expenses:
        print(f'No expenses found for {search_date}')
        return

    # Retrieve user expense categories
    categories = get_user_categories_by_type(user_id, 'expense')
    if not categories:
        print('No expense categories exist, please create add one first')
        return

    # Display categories and allow user to select one
    ref_dict = {ref: category for ref, category in enumerate(categories)}
    for ref, category in ref_dict.items():
        category.display_short(ref)

    while True:
        try:
            choice = int(input('Please select from the above categories to view budget: '))
            category = ref_dict.get(choice)
            if not category:
                print('Please enter a valid reference number')
                continue
            break
        except ValueError:
            print('Please enter a valid reference number')
            continue

    # cycle through expenditures
    spent = 0
    for expense in expenses:
        if expense.cat_id == category.id:
            spent += expense.amount

    # Determine the remaining budget
    if category.budget == 0:
        remaining = 'Budget not set'
    else:
        remaining = f'R{category.budget - spent:.2f}'

    # Display budget information
    month = datetime.strptime(search_date, '%Y-%m').strftime('%B')
    year = datetime.strptime(search_date, '%Y-%m').strftime('%Y')


    print(display_template(CATEGORY_BUDGET,
                           category.name,
                           month,
                           year,
                           spent,
                           remaining,
                           category.budget))
    pause_terminal()
