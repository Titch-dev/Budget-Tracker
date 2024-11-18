from db_access import get_user_goals, create_goal, get_goal_by_id

from templates import SELECT_GOAL, ADD_GOAL

from general_utils import display_formatter

from models.goal import Goal


def set_goals():
    pass

def select_user_goal(user_id: int) -> int|None:

    goals = get_user_goals(user_id)

    ref_dict = dict()

    for ref, goal in enumerate(goals, start=1):
        goal.display(ref)
        ref_dict[ref] = goal

    option = len(goals)

    # need an option if the length of goals is zero display nothing
    goal_choice = int(input(display_formatter(SELECT_GOAL, option + 1, option + 2)))

    if goal_choice in ref_dict:  # Existing goal choice
        return ref_dict[goal_choice].id
    elif goal_choice == option + 1:  # Create new goal
        return add_goal(user_id)
    elif goal_choice == option + 2:  # Cancel
        return None


def add_goal(user_id: int):
    print(ADD_GOAL)

    name = input('Enter a name for the financial goal: ')
    desc = input('Enter a short description of the financial goal: ')
    target = float(input('Enter a target amount for the financial goal: '))
    end_date = input('Enter an end date for your financial goal: ')

    goal = Goal.create(name=name,
                       desc=desc,
                       target=target,
                       end_date=end_date,
                       user_id=user_id)

    goal_id = create_goal(goal)

    return goal_id

def view_goals_progress(user_id: int):

    goal_id = select_user_goal(user_id)

    goal = get_goal_by_id(goal_id)

    goal.display()