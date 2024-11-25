from datetime import datetime


class Category:
    def __init__(self, id: int, name: str, desc: str, budget: float,
                 cat_type: str, created_at: datetime, user_id: int) -> None:
        self.id = id
        self.name = name
        self.desc = desc
        self.budget = budget
        self.cat_type = cat_type
        self.created_at = created_at
        self.user_id = user_id

    @classmethod
    def create(cls, name, desc, budget, cat_type, user_id):
        return cls(id=None, 
                   name=name, 
                   desc=desc, 
                   budget=budget,
                   cat_type=cat_type,
                   created_at=None, 
                   user_id=user_id)
    
    def __repr__(self):
        return f'<Category id={self.id}, name={self.name}, desc={self.desc}, budget={self.budget}, created_at={self.created_at}, user_id={self.user_id}>'

    def display_short(self, reference=None):
        category = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n'
        if reference:
            category += f'                                                           ref # {reference}\n'
        category += (f'Category name:   {self.name}\n'
                     f'Monthly Budget:  {'Not set' if self.budget == 0.00 else f'{self.budget}'}\n'
                     f'- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        print(category)

    def display_long(self):
        category = ('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n'
                    f'Category name:     {self.name}\n'
                    f'Category type:     {self.cat_type}\n'
                    f'Description:       '
                    f'     {self.desc}\n'
                    f'Monthly budget:    {'Not set' if self.budget == 0.00 else f'{self.budget}'}n'
                    '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ')
        print(category)
