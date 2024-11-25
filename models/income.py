from datetime import datetime


class Income:
    def __init__(self, id: int, name: str, amount: float, effect_date: datetime,
                 created_at: datetime, user_id: int, cat_id: int, cat_name: str) -> None:
        self.id = id
        self.name = name
        self.amount = amount
        self.effect_date = effect_date
        self.created_at = created_at
        self.user_id = user_id
        self.cat_id = cat_id
        self.cat_name = cat_name

    @classmethod
    def create(cls, name, amount, effect_date, user_id):
        return cls(id=None, 
                   name=name, 
                   amount=amount, 
                   effect_date=effect_date, 
                   created_at=None, 
                   user_id=user_id,
                   cat_id=None,
                   cat_name=None)
    
    def __repr__(self):
        return (f'<Income id={self.id}, name={self.name}, amount={self.amount}, '
                f'effect_date={self.effect_date}, created_at={self.created_at}, '
                f'user_id={self.user_id}, cat_id={self.cat_id}, cat_name={self.cat_name}>')

    def display_short(self, reference=None):
        income = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n'
        if reference:
            income += f'                                                       reference # {reference} \n'
        income += f'Income name:        {self.name}\n'\
                  f'Income amount:      {self.amount}\n'\
                  f'Income effect date: {self.effect_date}\n'\
                  f'Income category:    {self.cat_name}\n'\
                  '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n'
        print(income)

    def display_long(self):
        income = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n'\
                  f'Income ID:          {self.id}\n'\
                  f'Income name:        {self.name}\n'\
                  f'Income amount:      {self.amount}\n'\
                  f'Income effect date: {self.effect_date}\n'\
                  f'Income category:    {self.cat_name}\n'\
                  f'Income created:     {self.created_at}\n'\
                  '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n'
        print(income)
