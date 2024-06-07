import pytest

from mathinterpreter import calc


class TestCalculate:

    def test_numbers(self):
        value = calc("51.2")
        assert value == "51.2"

    def test_expression(self):
        value = float(calc("0 + 10/3"))
        pytest.approx(value, 3.33, 2)
