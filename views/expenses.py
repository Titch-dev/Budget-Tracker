from datetime import datetime

from templates import ADD_EXPENSE, SELECT_EXPENSE, EXPENSE_OPTION, CATEGORY_OPTION, EXPENSE_VIEW, \
    EXPENSE_SUMMARY
from models.expense import Expense
from models.category import Category

from views.categories import select_user_category, select_category, remove_delete_category, \
    set_category_budget
from views.goals import select_user_goal, select_user_goal

from db_access import get_user_categories, create_expense, get_user_expenses, get_expenses_by_category, update_expense, \
    delete_expense, get_user_categories_by_type, get_expenses_by_month
from general_utils import display_formatter, date_formatter


def add_expense(user_id: int):
    print(ADD_EXPENSE)
    name = input('Enter an expense name: ')
    amount = float(input('Enter the expense amount: '))
    print('Enter the date the expense will leave your account: ')
    effect_date = date_formatter(full_date=True)
    expense = Expense.create(name, amount, effect_date, user_id)


    category = select_user_category(user_id, cat_type='expense')
    if category:
        expense.cat_id = category.id
    else:
        expense.cat_id = None

    goal = select_user_goal(user_id)
    if goal:
        expense.goal_id = goal.id
    else:
        expense.goal_id = None

    create_expense(expense)  # create new expense entry in db


def track_expenses(expenses: list[Expense], month: str = ''):
    total = 0
    categories = dict()

    for expense in expenses:
        total += expense.amount
        if expense.cat_name in categories.keys():
            categories[expense.cat_name] += expense.amount
        else:
            categories[expense.cat_name] = expense.amount

    print(display_formatter(EXPENSE_SUMMARY, month, total))
    for name, amount in categories.items():
        print(f'      {name}:{' '*(20 - len(name))}R{amount}')

    print('-' * 72)
    stall = input(' Enter any key to continue: ')


def view_expenses(user_id: int) -> None:
    expenses = None

    while not expenses:

        view_choice = input(EXPENSE_VIEW)

        if view_choice == '1':  # get all expenses
            expenses = get_user_expenses(user_id)
            track_expenses(expenses)

        elif view_choice == '2':  # get expenses by month
            search_month = date_formatter(full_date=False)
            month_abbr = datetime.strptime(search_month, '%Y-%m').strftime("%b")

            expenses = get_expenses_by_month(search_month)

            track_expenses(expenses, month_abbr)

        else:
            return None

    ref_dict = dict()

    for ref, expense in enumerate(expenses, start=1):
        expense.display_short(ref)
        ref_dict[ref] = expense

    try:
        expense_choice = int(input(SELECT_EXPENSE))
    except ValueError:
        return None

    if expense_choice in ref_dict:
        expense = ref_dict[expense_choice]
        expense.display_long()

        expense_option = input(EXPENSE_OPTION)

        if expense_option == "1":  # Update expense amount
            new_amount = float(input('Enter new amount: '))
            expense.amount = new_amount
            update_expense(expense)
        elif expense_option == "2":  # Delete expense
            delete_expense(expense.id)


def view_expenses_by_category(user_id):

    categories = get_user_categories_by_type(user_id, "expense")

    ref_dict = dict()

    for ref, category in enumerate(categories, start=1):
        category.display_short(ref)
        ref_dict[ref] = category

    ref_choice = int(input('Please enter the above reference for the category: '))

    category = ref_dict[ref_choice]

    expenses = get_expenses_by_category(category.id)
    if len(expenses) == 0:
        print(f'You don\'t have any expenses for {category.name} category!')
    for expense in expenses:
        expense.display_short()

    category_choice = input(display_formatter(CATEGORY_OPTION, category.name))

    if category_choice == '1':  # Change Category budget
        set_category_budget(category)
    elif category_choice == '2':  # Delete Category
        remove_delete_category(category.id)
