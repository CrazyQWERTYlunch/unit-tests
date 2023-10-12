import pytest
import task1


@pytest.mark.parametrize("result, number", [(True, -2),
                                            (False, -1),
                                            (True, 0),
                                            (False, 1),
                                            (True, 2)])
def test_is_even_number(result, number):
    assert task1.is_even_number(number) == result
