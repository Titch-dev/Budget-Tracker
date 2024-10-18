from datetime import datetime

class Income():
    def __init__(self, id: int, name: str, amount: float, effect_date: datetime, created_at: datetime, user_id: int, category_id: int) -> None:
        self.id = id
        self.name = name
        self.amount = amount
        self.effect_date = effect_date
        self.created_at = created_at
        self.user_id = user_id
        self.category_id = category_id

    @classmethod
    def create(cls, name, amount, effect_date, user_id, category_id):
        return cls(None, name, amount, effect_date, None, user_id, category_id)
    
    def json(self):
        return dict(id = self.id,
                    name = self.name,
                    amount = self.amount,
                    effect_date = self.effect_date,
                    created_at = self.created_at,
                    user_id = self.user_id,
                    category_id = self.category_id)