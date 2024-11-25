from datetime import datetime


class User:
    def __init__(self, id: int, username: str, password: str, created_at: datetime, last_login: datetime):
        self.id = id
        self.username = username
        self.password = password
        self.created_at = created_at
        self.last_login = last_login
    
    @classmethod
    def create(cls, username, password):
        return cls(id=None, 
                   username=username,
                   password=password, 
                   created_at=None, 
                   last_login=None)
    
    def __repr__(self):
        return (f'<User id={self.id}, username={self.username}, password={self.password}, '
                f'created_at={self.created_at}, last_login={self.last_login}>')
    
    def display(self):
        user = ('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n'
                f'User ID:         {self.id}\n'
                f'User username:   {self.username}\n'
                f'User password:   {self.password}\n'
                f'User created:    {self.created_at}\n'
                f'User last login: {self.last_login}\n'
                '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n')
        print(user)
