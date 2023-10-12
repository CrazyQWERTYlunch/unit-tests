from User import User


class UserRepository:
    data = list()

    def add_user(self, new_user):

        if new_user not in self.data:
            self.data.append(new_user)
        else:
            print("Такой пользователь уже имеется")

    def find_by_name(self, name):
        for user in self.data:
            if user.name == name:
                return True
        return False

    def log_out_except_admin(self):
        for user in self.data:
            if not user.is_admin:
                user.is_authenticate = False

