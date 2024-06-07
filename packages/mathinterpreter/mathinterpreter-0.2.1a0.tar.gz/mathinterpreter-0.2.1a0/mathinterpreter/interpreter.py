from mathinterpreter.nodes import *
from mathinterpreter.values import Number


class Interpreter:
    """
    mathinterpreter's interpreter class

    Example:

        lexer = Lexer('1+(4/3)')
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        if tree:
            interpreter = Interpreter()
            value = interpreter.visit(tree)
            print(value)
        else:
            print("Invalid expression.")


    """

    def __init__(self):
        pass

    def visit(self, node):
        method_name = f"visit_{type(node).__name__}"
        method = getattr(self, method_name)
        return method(node)

    def visit_NumberNode(self, node):
        return Number(node.value)

    def visit_AddNode(self, node):
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

    def visit_SubtractNode(self, node):
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

    def visit_MultiplyNode(self, node):
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

    def visit_DivideNode(self, node):
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except:
            raise Exception("Runtime math error")

    def visit_RemaindeNode(self, node):
        try:
            return Number(self.visit(node.node_a).value % self.visit(node.node_b).value)
        except:
            raise Exception("Runtime math error")

    def visit_PowerNode(self, node):
        return Number(self.visit(node.node_a).value ** self.visit(node.node_b).value)
