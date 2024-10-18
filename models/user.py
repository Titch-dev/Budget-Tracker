from datetime import datetime

class User():
    def __init__(self, id: int, email: str, password: str, created_at: datetime, last_login: datetime) -> None:
        self.id = id,
        self.email = email
        self.password = password
        self.created_at = created_at
        self.last_login = last_login
    
    @classmethod
    def create(cls, email, password):
        return cls(None, email, password, None, None)
    
    def json(self):
        return dict(id = self.id,
                    email = self.email,
                    password = self.password,
                    created_at = self.created_at,
                    last_login = self.last_login)