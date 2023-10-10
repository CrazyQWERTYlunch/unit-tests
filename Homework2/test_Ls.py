from Vehicle import Vehicle
# from Homework2.Vehicle import Vehicle - не работающий вариант

class TestClass:

    def test_check_class_father(self, proto_car):
        assert isinstance(proto_car, Vehicle)

    def test_check_wheels_car(self, proto_car):
        assert proto_car.get_num_wheels() == 4

    def test_check_wheels_motorcycle(self, proto_motorcycle):
        assert proto_motorcycle.get_num_wheels() == 2

    def test_check_drive_car(self, proto_car):
        proto_car.test_drive()
        assert proto_car.get_speed() == 60
    def test_check_drive_motorcycle(self, proto_motorcycle):
        proto_motorcycle.test_drive()
        assert proto_motorcycle.get_speed() == 75

    def test_check_park_car(self, proto_car):
        proto_car.park()
        assert proto_car.get_speed() == 0

    def test_check_park_motorcycle(self, proto_motorcycle):
        proto_motorcycle.park()
        assert proto_motorcycle.get_speed() == 0
