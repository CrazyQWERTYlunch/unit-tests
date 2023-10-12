import pytest

import task2


@pytest.mark.parametrize("result, number", [(True, 25),
                                            (False, 10),
                                            (True, 50),
                                            (False, 101),
                                            (True, 100)])
def test_in_interval(result, number):
    assert task2.in_interval(number) == result
