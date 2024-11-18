from templates import ADD_EXPENSE
from models.expense import Expense
from models.category import Category

from views.categories import select_user_category
from views.goals import select_user_goal, select_user_goal

from db_access import get_user_categories, create_expense, get_user_expenses, get_expenses_by_category
from general_utils import display_formatter


def add_expense(user_id: int):
    print(ADD_EXPENSE)
    name = input('Enter an expense name: ')
    amount = float(input('Enter the expense amount: '))
    effect_date = input('Enter the date the expense will leave your account: ')
    expense = Expense.create(name=name,
                             amount=amount,
                             effect_date=effect_date,
                             user_id=user_id)
    category_id = select_user_category(user_id)
    goal_id = select_user_goal(user_id)

    create_expense(expense, category_id, goal_id)  # create new expense entry in db

def view_expenses(user_id: int):
    expenses = get_user_expenses(user_id)

    for expense in expenses:
        expense.display()

#     TODO: select singular entry to view, update or delete

def view_expenses_by_category(user_id):

    categories = get_user_categories(user_id)

    ref_dict = dict()

    for ref, category in enumerate(categories):
        category.display(ref + 1)  # adding 1 ensures that it'll be displayed
        ref_dict[ref + 1] = category

    category_id = int(input('Please enter the above reference for the category'))
    expenses = get_expenses_by_category(category_id)

    for expense in expenses:
        expense.display()
