from models.category import Category

from datetime import datetime

from db_access import get_user_categories, create_category, update_category, get_expenses_by_month, \
    get_user_categories_by_type, get_category_by_id, get_expenses_by_category, update_expense, delete_category

from general_utils import display_formatter

from templates import SELECT_CATEGORY, ADD_CATEGORY, CATEGORY_BUDGET


def select_user_category(user_id: int, cat_type: str) -> Category | None:

    categories = get_user_categories_by_type(user_id, cat_type)

    ref_dict = dict()

    for ref, category in enumerate(categories, start=1):
        category.display_short(ref)
        ref_dict[ref] = category

    option = len(categories)
    # need an option if the length of categories is zero display nothing
    choice = int(input(display_formatter(SELECT_CATEGORY, option + 1, cat_type, option + 2)))

    if choice in ref_dict:
        return ref_dict[choice]  # return the category
    elif choice == option + 1:
        new_category = add_category(user_id, cat_type)
        return new_category
    elif choice == option + 2:
        return None


def select_category(user_id: int, categories: list[Category]) -> Category | None:

    ref_dict = dict()

    for ref, category in enumerate(categories, start=1):
        category.display_short(ref)
        ref_dict[ref] = category

    option = len(categories) + 1

    category_choice = int(input(display_formatter(SELECT_CATEGORY, option)))

    if category_choice in ref_dict:
        return ref_dict[category_choice]
    elif category_choice == option:
        return add_category(user_id)
    else:
        return None


def add_category(user_id: int, cat_type: str) -> Category:
    """Function to take user input, instantiate Category object,
    and call db_access.create_category

    Parameters:
        user_id: Int,
        cat_type: Str

    Returns:
        A newly created Category object
    """
    print(ADD_CATEGORY)
    name = input('Enter a name for the category: ')
    # TODO: validate that name is unique
    desc = input('Enter a short description: ')
    budget = float(input('Enter a monthly budget for this category: '))
    new_category = Category.create(name=name,
                                   desc=desc,
                                   budget=budget,
                                   cat_type=cat_type,
                                   user_id=user_id)

    category_id = create_category(new_category)
    category = get_category_by_id(category_id)

    return category


def remove_delete_category(cat_id: int) -> None:
    expenses = get_expenses_by_category(cat_id)

    for expense in expenses:
        expense.cat_id = None
        update_expense(expense)

    # Delete category
    delete_category(cat_id)


def set_category_budget(category: Category):

    new_budget = float(input(f'Enter the monthly budget amount for {category.name}: '))

    category.budget = new_budget

    update_category(category)


def view_category_budget(user_id: int):
    categories = get_user_categories(user_id)

    ref_dict = dict()

    for ref, category in enumerate(categories, start=1):
        category.display_short(ref)
        ref_dict[ref] = category

    choice = int(input('Please select from the above categories to view this month\'s budget: '))

    category = ref_dict[choice]

    current_date = datetime.now()
    month = current_date.strftime('%B')
    search_date = current_date.strftime('%Y-%m')

    expenses = get_expenses_by_month(search_date, category.id)
    spent = 0

    for expense in expenses:
        date = datetime.fromisoformat(expense.effect_date)
        if date <= current_date:
            spent += expense.amount

    remaining = category.budget - spent

    print(display_formatter(CATEGORY_BUDGET,
                            category.name,
                            month,
                            spent,
                            remaining,
                            category.budget))
