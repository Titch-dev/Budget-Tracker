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
        return cls(None, name, desc, budget, None, user_id)
    
    def json(self):
        return dict(id = self.id, 
                    name = self.name, 
                    desc = self.desc, 
                    budget = self.budget, 
                    created_at = self.created_at, 
                    user_id = self.user_id)
    