from models.category import Category

from datetime import datetime

from db_access import get_user_categories, create_category, update_category, get_expenses_by_month

from general_utils import enumerate_object, display_formatter

from templates import SELECT_CATEGORY, ADD_CATEGORY, CATEGORY_BUDGET


def select_user_category(user_id: int):

    categories = get_user_categories(user_id)

    ref_dict = dict()

    for ref, category in enumerate(categories, start=1):
        category.display(ref) # adding 1 ensures that it'll be displayed
        ref_dict[ref] = category

    option = len(categories)
    # need an option if the length of categories is zero display nothing
    category_choice = int(input(display_formatter(SELECT_CATEGORY, option + 1, option + 2)))

    if category_choice in ref_dict:
        return ref_dict[category_choice].id  # return the category id
    elif category_choice == option + 1:
        new_category = add_category()
        return new_category.id
    elif category_choice == option + 2:
        return None


def add_category(user_id: int) -> Category:
    print(ADD_CATEGORY)
    name = input('Enter a name for the category: ')
    # TODO: validate that name is unique
    desc = input('Enter a short description: ')
    budget = float(input('Enter a monthly budget for this category: '))
    category = Category.create(name=name,
                               desc=desc,
                               budget=budget,
                               user_id=user_id)
    cat_id = create_category(category)


def set_category_budget(user_id: int):
    print('Select from the below categories to amend the budget')
    categories = get_user_categories(user_id)

    ref_dict = dict()

    for ref, category in enumerate(categories, start=1):
        category.display(ref)
        ref_dict[ref] = category

    category_choice = int(input('Please input the respective reference number to alter the budget for: '))

    category = ref_dict[category_choice]

    budget = float(input(f'Enter the monthly budget amount for {category.name}: '))

    category.budget = budget

    update_category(category)


def view_category_budget(user_id: int):
    categories = get_user_categories(user_id)

    ref_dict = dict()

    for ref, category in enumerate(categories, start=1):
        category.display(ref)
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


