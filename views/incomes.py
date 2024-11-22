from datetime import datetime

from general_utils import display_formatter, date_formatter

from templates import INCOME_ADD, INCOME_SELECT, INCOME_OPTION, CATEGORY_OPTION, INCOME_VIEW, INCOME_SUMMARY
from models.income import Income

from views.categories import select_user_category, get_user_categories, set_category_budget, remove_delete_category

from db_access import create_income, get_user_income, get_income_by_category, delete_income, get_income_by_month, \
    get_user_categories_by_type


def add_income(user_id: int):
    print(INCOME_ADD)
    name = input('Enter an income name: ')
    amount = float(input('Enter the income amount: '))
    print('Enter the date this income will take effect:')
    effect_date = date_formatter(full_date=True)
    income = Income.create(name=name,
                           amount=amount,
                           effect_date=effect_date,
                           user_id=user_id)
    category_id = select_user_category(user_id, cat_type='income')
    income.cat_id = category_id
    create_income(income)


def track_incomes(incomes: list[Income], month: str = None):

    total = 0
    categories = dict()

    for income in incomes:
        total += income.amount
        if income.cat_name in categories.keys():
            categories[income.cat_name] += income.amount
        else:
            categories[income.cat_name] = income.amount

    print(INCOME_SUMMARY)
    print(f'Total amount:   R{total}\n')
    if month:
        print(f'Month: {month}')

    print('Categories:\n')

    for name, amount in categories.items():
        print(f'    {name}:     R{amount}')

    print('-' * 72)

    stall = input('Press any key to continue: ')


def view_incomes(user_id: int) -> None:

    incomes = None
    while not incomes:

        view_choice = input(INCOME_VIEW)
        if view_choice == '1':  # get all incomes
            incomes = get_user_income(user_id)
            track_incomes(incomes)
        elif view_choice == '2':  # get incomes by month
            search_month = date_formatter(full_date=False)
            month_abbr = datetime.strptime(search_month, '%Y-%m').strftime("%b")

            incomes = get_income_by_month(search_month)

            track_incomes(incomes, month_abbr)
        else:
            return None

    ref_dict = dict()

    for ref, income in enumerate(incomes, start=1):
        income.display_short(ref)
        ref_dict[ref] = income

    try:
        income_ref = int(input(INCOME_SELECT))
    except ValueError:
        return None

    if income_ref in ref_dict:
        income = ref_dict[income_ref]
        income.display_long()

        income_choice = input(INCOME_OPTION)

        if income_choice == "1":
            delete_income(income.id)


def view_incomes_by_category(user_id: int):
    categories = get_user_categories_by_type(user_id, 'income')

    ref_dict = dict()

    for ref, category in enumerate(categories, start=1):
        category.display_short(ref)
        ref_dict[ref] = category

    ref_choice = int(input('Please enter the above reference for the category: '))

    category = ref_dict[ref_choice]

    incomes = get_income_by_category(category.id)

    if len(incomes) == 0:
        print(f'You don\'t have any incomes for {category.name} category!')
    else:
        for income in incomes:
            income.display_short()

    category_choice = input(display_formatter(CATEGORY_OPTION, category.name))

    if category_choice == '1':  # Change Category budget
        set_category_budget(category)
    elif category_choice == '2':  # Delete Category
        remove_delete_category(category.id)