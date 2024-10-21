from datetime import datetime

class Category():
    def __init__(self, id: int, name: str, desc: str, budget: float, created_at: datetime, user_id: int) -> None:
        self.id = id
        self.name = name
        self.desc = desc
        self.budget = budget
        self.created_at = created_at
        self.user_id = user_id

    @classmethod
    def create(cls, name, desc, budget, user_id):
        return cls(id=None, 
                   name=name, 
                   desc=desc, 
                   budget=budget,
                   created_at=None, 
                   user_id=user_id)
    
    def __repr__(self):
        return f'<Category id={self.id}, name={self.name}, desc={self.desc}, budget={self.budget}, created_at={self.created_at}, user_id={self.user_id}'

    def display(self):
        category = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n'\
              f'Category ID:                {self.id}\n'\
              f'Category name:              {self.name}\n'\
              f'Category description:       {self.desc}\n'\
              f'Category monthly budget:    {self.budget}\n'\
              f'Category created at:        {self.created_at}\n'\
              '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n'
        print(category)


def get_category():
    pass

def add_category():
    pass

def update_category():
    pass

def delete_category():
    pass