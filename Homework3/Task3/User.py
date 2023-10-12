class User:
    def __init__(self, name: str, password: str, is_authenticate: bool = False, is_admin: bool = False):
        self.name = name
        self.password = password
        self.is_authenticate = is_authenticate
        self.is_admin = is_admin

    def __repr__(self):
        return f'{self.name}: {self.password}, {self.is_admin}, {self.is_authenticate}'

    def authenticate(self, name, password) -> bool:
        if self.name == name and self.password == password:
            self.is_authenticate = True



