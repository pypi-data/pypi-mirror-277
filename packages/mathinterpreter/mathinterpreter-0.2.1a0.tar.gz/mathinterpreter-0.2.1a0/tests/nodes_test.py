import pytest

from mathinterpreter.nodes import *


@pytest.mark.parametrize(
    "a,b,result",
    [
        (0, 0, "(0^0)"),
        (1, 1, "(1^1)"),
        (7, 2, "(7^2)"),
        (6.2, 2.0, "(6.2^2.0)"),
    ],
)
def test_PowerNode_constructor(a, b, result):
    node = PowerNode(a, b)
    assert node.__repr__() == result
