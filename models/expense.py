from datetime import datetime

class Expense():
    def __init__(self, id: int, name: str, amount: float, effect_date: datetime, created_at: datetime, user_id: int, category_name: str, goal_name: str) -> None:
        self.id = id
        self.name = name
        self.amount = amount
        self.effect_date = effect_date
        self.created_at = created_at
        self.user_id = user_id
        self.category_name = category_name
        self.goal_name = goal_name

    @classmethod
    def create(cls, name, amount, effect_date, user_id):
        return cls(id=None, 
                   name=name, 
                   amount=amount, 
                   effect_date=effect_date, 
                   created_at=None, 
                   user_id=user_id, 
                   category_name=None,
                   goal_name=None)
    
    def __repr__(self):
        return f'<Expense id={self.id}, name={self.name}, amount={self.amount}, effect_date={self.effect_date}, created_at={self.created_at}, user_id={self.user_id}, category_name={self.category_name}, goal_name={self.goal_name}>'
    
    def display(self):
        expense = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n'\
              f'Expense ID:          {self.id}\n'\
              f'Expense name:        {self.name}\n'\
              f'Expense amount:      {self.amount}\n'\
              f'Expense effect date: {self.effect_date}\n'\
              f'Expense category:    {self.category_name}\n'\
              f'Expense goal:        {self.goal_name}\n'\
              '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n'
        print(expense)

def get_expense():
    pass

def add_expense():
    pass

def update_expense():
    pass

def delete_expense():
    pass