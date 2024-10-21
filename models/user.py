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
        return cls(id=None, 
                   email=email, 
                   password=password, 
                   created_at=None, 
                   last_login=None)
    
    def __repr__(self):
        return f'<User id={self.id}, email={self.email}, password={self.password}, created_at={self.created_at}, last_login={self.last_login}>'
    
    def display(self):
        user = '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n'\
              f'User ID:         {self.id}\n'\
              f'User email:      {self.email}\n'\
              f'User password:   {self.password}\n'\
              f'User created:    {self.created_at}\n'\
              f'User last login: {self.last_login}\n'\
              '- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n'
        print(user)
    
    # TODO:
    #   - create a print method for object
    #   - 