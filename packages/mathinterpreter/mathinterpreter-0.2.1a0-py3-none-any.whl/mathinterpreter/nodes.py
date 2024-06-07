from dataclasses import dataclass


@dataclass
class NumberNode:
    """
    Class for define number nodes.
    Number nodes have no children node.
    """

    value: any

    def __repr__(self):
        return f"{self.value}"


@dataclass
class AddNode:
    """
    Class for define Add nodes.
    Add nodes must have 2 children nodes.
    """

    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}+{self.node_b})"


@dataclass
class SubtractNode:
    """
    Class for define Subtract nodes.
    Subtract nodes must have 2 children nodes.
    """

    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}-{self.node_b})"


@dataclass
class MultiplyNode:
    """
    Class for define Multiply nodes.
    Multiply nodes must have 2 children nodes.
    """

    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}*{self.node_b})"


@dataclass
class DivideNode:
    """
    Class for define Divide nodes.
    Divide nodes must have 2 children nodes.
    """

    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}/{self.node_b})"


@dataclass
class RemaindeNode:
    """
    Class for define Divide nodes.
    Remainde nodes must have 2 children nodes.
    """

    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}%{self.node_b})"


@dataclass
class PowerNode:
    """
    class mathinterpreter.nodes.PowerNode()

    @dataclass for nodes evaluating the power operation.
    If syntactically correct, the resulting operation will be $a^b$,
    where $a$ is the basis and $b$ is the exponent.

    Properties:
    -----------
    node_a: the value of the basis.
    node_b: the value of the exponent
    """

    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}^{self.node_b})"


@dataclass
class PlusNode:
    """
    Class for define plus nodes.
    Plus nodes must have only one child node.
    """

    node: any

    def __repr__(self):
        return f"(+{self.node})"


@dataclass
class MinusNode:
    """
    Class for define minus nodes.
    Minus nodes must have only one child node.
    """

    node: any

    def __repr__(self):
        return f"(-{self.node})"
