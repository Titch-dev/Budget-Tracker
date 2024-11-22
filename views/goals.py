from datetime import datetime

from db_access import get_user_goals, create_goal, get_goal_by_id, get_expenses_by_goal
from models.expense import Expense

from templates import SELECT_GOAL, ADD_GOAL, GOAL_SUMMARY

from general_utils import display_formatter, date_formatter

from models.goal import Goal


def track_goals(expenses: list[Expense], goal: Goal) -> None:

    balance = 0.00

    for expense in expenses:
        balance += expense.amount
        expense.display_long()

    end_date = datetime.strptime(goal.end_date, "%Y-%m-%d")
    now = datetime.now()
    balance_left = goal.target - balance
    days_left = (end_date - now).days
    weeks_left = days_left / 7
    amount_per_week = round((balance_left / weeks_left), 2)

    input(display_formatter(GOAL_SUMMARY,
                            goal.name,
                            goal.desc,
                            balance,
                            goal.target,
                            balance_left,
                            goal.end_date,
                            days_left,
                            amount_per_week))

def add_goal(user_id: int) -> Goal:
    print(ADD_GOAL)

    name = input('Enter a name for the financial goal: ')
    desc = input('Enter a short description of the financial goal: ')
    target = float(input('Enter a target amount for the financial goal: '))
    print('Enter an end date for your financial goal ')
    end_date = date_formatter(full_date=True)

    new_goal = Goal.create(name=name,
                           desc=desc,
                           target=target,
                           end_date=end_date,
                           user_id=user_id)

    goal_id = create_goal(new_goal)
    goal = get_goal_by_id(goal_id)

    return goal


def select_user_goal(user_id: int) -> Goal | None:

    goals = get_user_goals(user_id)

    ref_dict = dict()

    for ref, goal in enumerate(goals, start=1):
        goal.display_short(ref)
        ref_dict[ref] = goal

    option = len(goals) + 1

    # need an option if the length of goals is zero display nothing
    try:
        goal_choice = int(input(display_formatter(SELECT_GOAL, option)))

        if goal_choice in ref_dict:  # Existing goal choice
            return ref_dict[goal_choice]

        elif goal_choice == option:  # Create new goal
            return add_goal(user_id)

        else:
            return None

    except ValueError:
        return None


def view_goals_progress(user_id: int):

    goal = select_user_goal(user_id)
    expenses = get_expenses_by_goal(goal.id)

    track_goals(expenses, goal)