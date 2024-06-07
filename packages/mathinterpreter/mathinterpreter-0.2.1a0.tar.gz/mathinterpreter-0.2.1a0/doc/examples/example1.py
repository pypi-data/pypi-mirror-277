from mathinterpreter.interpreter import Interpreter
from mathinterpreter.lexer import Lexer
from mathinterpreter.parser_ import Parser

text = "1 + 3*(5*2+1)/2"
tokens = Lexer(text).generate_tokens()
tree = Parser(tokens).parse()

interpreter = Interpreter()
value = interpreter.visit(tree)
print(value)
