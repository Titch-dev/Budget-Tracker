from datetime import datetime


class Goal:
    def __init__(self, id: int, name: str, desc: str, target: float, end_date: datetime, created_at: datetime, user_id: int) -> None:
        self.id = id
        self.name = name
        self.desc = desc
        self.target = target
        self.end_date = end_date
        self.created_at = created_at
        self.user_id = user_id

    @classmethod
    def create(cls, name, desc, target, end_date, user_id):
        return cls(id=None, 
                   name=name, 
                   desc=desc, 
                   target=target, 
                   end_date=end_date, 
                   created_at=None, 
                   user_id=user_id)
    
    def __repr__(self):
        return (f'<Goal id={self.id}, name={self.name}, desc={self.desc}, target={self.target}, '
                f'end_date={self.end_date}, created_at={self.created_at}, user_id={self.user_id}')

    def display_short(self, reference=None):
        goal = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n'
        if reference:
            goal += f'                                                           ref # {reference} \n'
        goal += f'Goal name:          {self.name}\n'\
                f'Goal description:   {self.desc}\n'\
                f'Goal target:        {self.target}\n'\
                '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n'
        print(goal)

    def display_long(self):
        goal = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n'\
                f'Goal ID:            {self.id}\n' \
                f'Goal name:          {self.name}\n' \
                f'Goal description:   {self.desc}\n' \
                f'Goal target:        {self.target}\n' \
                f'Goal end date:      {self.end_date}\n' \
                f'Goal created:       {self.created_at}\n' \
                '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n'
        print(goal)
