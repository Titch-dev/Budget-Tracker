from datetime import datetime

from models.finance import Finance


class Expense(Finance):
    def __init__(self, id: int, name: str, amount: float, effect_date: datetime,
                 created_at: datetime, user_id: int, cat_id: int, cat_name: str,
                 goal_id: int = None, goal_name: str = None) -> None:
        super().__init__(id, name, amount, effect_date, created_at, user_id, cat_id, cat_name)
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
        base_repr = super().__repr__()
        return f'{base_repr[:-2]} goal_id={self.goal_id}, goal_name={self.goal_name}'

    def display_short(self, reference=None):
        super().display_short(reference)
        if self.goal_name:
            print(f'{self.__class__.__name__} goal:        {self.goal_name}')

    def display_long(self):
        super().display_long()
        if self.goal_name:
            print(f'{self.__class__.__name__} goal:        {self.goal_name}')
