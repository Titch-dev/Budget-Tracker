from datetime import datetime

class Income():
    def __init__(self, id: int, name: str, amount: float, effect_date: datetime, created_at: datetime, user_id: int, category_name: str) -> None:
        self.id = id
        self.name = name
        self.amount = amount
        self.effect_date = effect_date
        self.created_at = created_at
        self.user_id = user_id
        self.category_name = category_name

    @classmethod
    def create(cls, name, amount, effect_date, user_id, category_name):
        return cls(id=None, 
                   name=name, 
                   amount=amount, 
                   effect_date=effect_date, 
                   created_at=None, 
                   user_id=user_id, 
                   category_name=category_name)
    
    def __repr__(self):
        return f'<Income id={self.id}, name={self.name}, amount={self.amount}, effect_date={self.effect_date}, created_at={self.created_at}, user_id={self.user_id}, category_name={self.category_name}>'
    
    def display(self):
        income = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n'\
              f'Income ID:          {self.id}\n'\
              f'Income name:        {self.name}\n'\
              f'Income amount:      {self.amount}\n'\
              f'Income effect date: {self.effect_date}\n'\
              f'Income category:    {self.category_name}\n'\
              f'Income created:     {self.created_at}\n'\
              '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n'
        print(income)

def get_income():
    pass

def get_all_incomes():
    pass

def add_income():
    pass

def update_income():
    pass

def delete_income():
    pass