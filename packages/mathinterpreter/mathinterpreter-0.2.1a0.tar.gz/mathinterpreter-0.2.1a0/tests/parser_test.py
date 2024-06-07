import pytest

from mathinterpreter.nodes import *
from mathinterpreter.parser import Parser
from mathinterpreter.tokens import Token, TokenType


class TestParser:

    def test_empty(self):
        tokens = []
        node = Parser(tokens).parse()
        assert node == None

    def test_numbers(self):
        tokens = [Token(TokenType.NUMBER, 51.2)]
        node = Parser(tokens).parse()
        assert node == NumberNode(51.2)

    @pytest.mark.parametrize(
        "token_operation,num_a,num_b,Node",
        [
            (TokenType.PLUS, 27, 14, AddNode),
            (TokenType.MINUS, 27, 14, SubtractNode),
            (TokenType.DIVIDE, 27, 14, DivideNode),
            (TokenType.MULTIPLY, 27, 14, MultiplyNode),
            (TokenType.POWER, 3, 2, PowerNode),
            (TokenType.REMAINDE, 3, 2, RemaindeNode),
        ],
    )
    def test_single_operations_new(self, token_operation, num_a, num_b, Node):
        tokens = [
            Token(TokenType.NUMBER, num_a),
            Token(token_operation),
            Token(TokenType.NUMBER, num_b),
        ]

        node = Parser(tokens).parse()
        assert node == Node(NumberNode(num_a), NumberNode(num_b))

    def test_full_expression(self):
        tokens = [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.PLUS),
            Token(TokenType.LPAREN),
            Token(TokenType.NUMBER, 43),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 36),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 48),
            Token(TokenType.RPAREN),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 51),
        ]

        node = Parser(tokens).parse()
        assert node == AddNode(
            NumberNode(27),
            MultiplyNode(
                SubtractNode(
                    DivideNode(NumberNode(43), NumberNode(36)), NumberNode(48)
                ),
                NumberNode(51),
            ),
        )
