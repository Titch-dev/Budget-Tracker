from datetime import datetime

from models import Goal, Expense

from services import get_goal_by_id, get_user_goals, create_goal, get_expenses_by_goal

from general_utils import display_template, date_formatter, amount_validator, pause_terminal

from templates import SELECT_GOAL, ADD_GOAL, GOAL_SUMMARY, GOAL_LIST


def is_goal_name_taken(user_id: int, name: str) -> bool:
    """Returns True if name already taken, and False if not

    Parameters:
        user_id (int): The ID of the user to filter by
        name (str): The goal name to check if already exists

    Returns:
        True | False: True if name exists and False if not
    """
    try:
        goals = get_user_goals(user_id)
        for goal in goals:
            if name.strip() == goal.name:
                return True
        return False
    except TypeError:
        return False


def track_goals(expenses: list[Expense], goal: Goal) -> None:
    """Track progress towards a financial goal.

    Parameters:
        expenses (list[Expense]): A list of expenses associated with the goal.
        goal (Goal): The financial goal being tracked.
    """

    balance = sum(expense.amount for expense in expenses)

    # Display all expenses associated with the goal
    if expenses:
        print(f"\nExpenses contributing to the goal {goal.name}:")
        for expense in expenses:
            expense.display_short()
    else:
        print("No expenses recorded for this goal.")

    # Calculate progress and time remaining
    balance_left = goal.target - balance
    end_date = datetime.strptime(goal.end_date, "%Y-%m-%d")
    now = datetime.now()
    days_left = (end_date - now).days
    weeks_left = days_left / 7
    amount_per_week = round((balance_left / weeks_left), 2) if balance_left > 0 else 'Goal Reached!'

    # Provide feedback based on the progress
    if balance_left <= 0:
        status_message = f"Goal achieved! You’ve exceeded your target by R{-balance_left:.2f}."
    elif days_left < 0:
        status_message = f"The goal deadline has passed. You are short by R{balance_left:.2f}."
    else:
        status_message = (
            f"You need to save R{amount_per_week:.2f} per week to meet your goal on time."
        )

    # Display goal summary
    print(display_template(GOAL_SUMMARY,
                           goal.name,
                           goal.desc,
                           balance,
                           goal.target,
                           balance_left,
                           goal.end_date,
                           days_left if days_left >= 0 else 'Deadline passed',
                           status_message))
    pause_terminal()


def add_goal(user_id: int) -> Goal | None:
    """Take user input, return a newly created category

    Parameters:
        user_id (int): The ID of the user to create a goal.

    Returns:
        Goal: A newly created goal
    """
    print(ADD_GOAL)

    # fullback mechanism: Get and validate a category name
    while True:
        name = input('Enter a name for the financial goal: ').strip()
        if not name:
            print('Name cannot be empty.')
            continue
        if is_goal_name_taken(user_id, name):
            print('Goal name already taken.')
            continue
        break

    # Not a required field
    desc = input('Enter a short description of the financial goal: ').strip()

    # Validate a target
    target = amount_validator('target')

    # Get a valid date string
    print('Enter an end date for your financial goal')
    end_date = date_formatter(full_date=True)

    # Create the new goal
    new_goal = Goal.create(
        name=name,
        desc=desc,
        target=target,
        end_date=end_date,
        user_id=user_id)

    # Save and retrieve the category
    try:
        goal_id = create_goal(new_goal)
        goal = get_goal_by_id(goal_id)
        return goal
    except Exception as e:
        print(f'An error has occurred while creating the goal: {e}')
        return None


def select_user_goal(user_id: int) -> Goal | None:
    """Take user input and return a Goal

    Parameters:
        user_id (int): The ID of user to creating the goal

    Returns:
        Goal | None: The selected goal, a newly added one, or None
    """
    goals = get_user_goals(user_id)

    if not goals:
        print("No goals available")
        choice = input('Would you like to add a goal? (y/n): ').strip().lower()
        if choice == 'y':
            return add_goal(user_id)
        else:
            return None

    ref_dict = {ref: goal for ref, goal in enumerate(goals, start=1)}

    # Display available goals
    for ref, goal in ref_dict.items():
        goal.display_short(ref)

    ADD_OPTION = len(goals) + 1

    try:
        goal_choice = int(input(display_template(SELECT_GOAL, ADD_OPTION)).strip())
    except ValueError:
        return None

    if goal_choice in ref_dict:  # Existing goal choice
        return ref_dict.get(goal_choice)
    elif goal_choice == ADD_OPTION:  # Create new goal
        return add_goal(user_id)
    else:
        return None


def view_goals_progress(user_id: int) -> None:
    """Summarise and display a user selected goal

    Parameters:
        user_id (int): The ID of the user to get user goals
    """
    # User selects goal
    print(GOAL_LIST)
    goal = select_user_goal(user_id)
    if not goal:
        print('Exiting goals progress...')
        return

    # Get all expenses associated with the goal
    expenses = get_expenses_by_goal(goal.id)
    if not expenses:
        goal.display_long()
        print(f'No expenses associated with goal {goal.name}')
        print('Consider adding new expenses and linking this goal to them \n')
        pause_terminal()
        return

    track_goals(expenses, goal)
