from datetime import datetime


class Finance:
    def __init__(self, id: int, name: str, amount: float, effect_date: datetime,
                 created_at: datetime, user_id: int, cat_id: int, cat_name: str):
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
        return (f'<{self.__class__.__name__} id={self.id}, name={self.name}, amount={self.amount}, '
                f'effect_date={self.effect_date}, created_at={self.created_at}, '
                f'user_id={self.user_id}, cat_id={self.cat_id}, cat_name={self.cat_name}>')

    def display_short(self, reference=None):
        details = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n'
        if reference:
            details += f'                                                           ref # {reference} \n'
        details += f'{self.__class__.__name__} name:        {self.name}\n'\
                   f'{self.__class__.__name__} amount:      {self.amount}\n'\
                   f'{self.__class__.__name__} effect date: {self.effect_date}\n'\
                   f'{self.__class__.__name__} category:    {self.cat_name}'''
        print(details)

    def display_long(self):
        details = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n'\
                  f'{self.__class__.__name__} ID:          {self.id}\n'\
                  f'{self.__class__.__name__} name:        {self.name}\n'\
                  f'{self.__class__.__name__} amount:      {self.amount}\n'\
                  f'{self.__class__.__name__} effect date: {self.effect_date}\n'\
                  f'{self.__class__.__name__} category:    {self.cat_name}\n'\
                  f'{self.__class__.__name__} created:     {self.created_at}\n'
        print(details)
