from templates import ADD_INCOME
from models.income import Income

from views.categories import select_user_category, get_user_categories

from db_access import create_income, get_user_income, get_income_by_category

def add_income(user_id: int):
    print(ADD_INCOME)
    name = input('Enter an income name: ')
    amount = float(input('Enter the income amount: '))
    effect_date = input('Enter the date this income will take effect: ')
    income = Income.create(name=name,
                           amount=amount,
                           effect_date=effect_date,
                           user_id=user_id)
    category_id = select_user_category(user_id)
    create_income(income, category_id)

def view_incomes(user_id: int):
    incomes = get_user_income(user_id)

    for income in incomes:
        income.display()

#     TODO: select singular entry to view, update or delete

def view_incomes_by_category(user_id: int):
    categories = get_user_categories(user_id)

    ref_dict = dict()

    for ref, category in enumerate(categories):
        category.display(ref + 1)  # adding 1 ensures that it'll be displayed
        ref_dict[ref + 1] = category

    category_id = int(input('Please enter the above reference for the category: '))

    incomes = get_income_by_category(category_id)

    for income in incomes:
        income.display()