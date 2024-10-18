from datetime import datetime

class Goal():
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
        return cls(None, name, desc, target, end_date, None, user_id)
    
    def json(self):
        return dict(id = self.id,
                    name = self.name,
                    desc = self.desc,
                    target = self.target,
                    end_date = self.end_date,
                    created_at = self.created_at,
                    user_id = self.user_id)