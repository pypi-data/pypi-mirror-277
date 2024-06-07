import pytest

from mathinterpreter.interpreter import Interpreter
from mathinterpreter.nodes import *
from mathinterpreter.values import Number


class TestInterpreter:

    def test_numbers(self):
        value = Interpreter().visit(NumberNode(51.2))
        assert value == Number(51.2)

    def test_single_operations(self):
        result = Interpreter().visit(AddNode(NumberNode(27), NumberNode(14)))
        assert result.value == 41

        result = Interpreter().visit(SubtractNode(NumberNode(27), NumberNode(14)))
        assert result.value == 13

        result = Interpreter().visit(MultiplyNode(NumberNode(27), NumberNode(14)))
        assert result.value == 378

        result = Interpreter().visit(PowerNode(NumberNode(2), NumberNode(2)))
        assert result.value == 4

        result = Interpreter().visit(DivideNode(NumberNode(27), NumberNode(14)))
        pytest.approx(result.value, 1.92857, 5)

        result = Interpreter().visit(RemaindeNode(NumberNode(32), NumberNode(10)))
        assert result.value == 2

        result = Interpreter().visit(RemaindeNode(NumberNode(5.3), NumberNode(2.1)))
        pytest.approx(result.value, 1.0999, 5)

        with pytest.raises(Exception):
            Interpreter().visit(DivideNode(NumberNode(27), NumberNode(0)))

    def test_full_expression(self):
        tree = AddNode(
            NumberNode(27),
            MultiplyNode(
                SubtractNode(
                    DivideNode(NumberNode(43), NumberNode(36)), NumberNode(48)
                ),
                NumberNode(51),
            ),
        )

        result = Interpreter().visit(tree)
        pytest.approx(result.value, -2360.08, 2)
