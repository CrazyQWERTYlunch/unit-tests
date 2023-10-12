import pytest

from Homework3.Task3.User import User
from Homework3.Task3.UserRepository import UserRepository


#
@pytest.mark.parametrize("user, result", [(User("Ваня", "zxc"), False),
                                          (User("Ваня2", "zxcv", True, True), True),
                                          (User("Ваня3", "zxc", True, False), False)])
def test_log_out_except_admin(user, result):
    ur1 = UserRepository()
    ur1.add_user(user)

    ur1.log_out_except_admin()

    assert user.is_authenticate == result
