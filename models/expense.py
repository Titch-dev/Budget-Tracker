from datetime import datetime


class Expense:
    def __init__(self, id: int, name: str, amount: float, effect_date: datetime,
                 created_at: datetime, user_id: int, cat_id: int, cat_name: str,
                 goal_id: int, goal_name: str) -> None:
        self.id = id
        self.name = name
        self.amount = amount
        self.effect_date = effect_date
        self.created_at = created_at
        self.user_id = user_id
        self.cat_id = cat_id
        self.cat_name = cat_name
        self.goal_id = goal_id
        self.goal_name = goal_name

    @classmethod
    def create(cls, name, amount, effect_date, user_id):
        return cls(id=None, 
                   name=name, 
                   amount=amount, 
                   effect_date=effect_date, 
                   created_at=None, 
                   user_id=user_id,
                   cat_id=None,
                   cat_name=None,
                   goal_id=None,
                   goal_name=None)
    
    def __repr__(self):
        return (f'<Expense id={self.id}, name={self.name}, amount={self.amount}, '
                f'effect_date={self.effect_date}, created_at={self.created_at}, '
                f'user_id={self.user_id}, cat_id={self.cat_id}, category_name={self.cat_name}, '
                f'goal_id={self.goal_id}, goal_name={self.goal_name}>')

    def display_short(self, reference=None):
        expense = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n'
        if reference:
            expense += f'                                                           ref # {reference} \n'
        expense += f'Expense name:        {self.name}\n'\
                   f'Expense amount:      R{self.amount}\n'\
                   f'Expense effect date: {self.effect_date}\n'
        if self.cat_name:
            expense += f'Expense category:    {self.cat_name}\n'
        if self.goal_name:
            expense += f'Expense goal:        {self.goal_name}\n'
        print(expense)

    def display_long(self):
        expense = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n'\
              f'Expense ID:          {self.id}\n'\
              f'Expense name:        {self.name}\n'\
              f'Expense amount:      R{self.amount}\n'\
              f'Expense effect date: {self.effect_date}\n'\
              f'Expense category:    {self.cat_name}\n'\
              f'Expense goal:        {self.goal_name}\n'
        print(expense)
