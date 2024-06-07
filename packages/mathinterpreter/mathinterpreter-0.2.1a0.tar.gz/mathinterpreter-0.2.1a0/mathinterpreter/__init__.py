from importlib.metadata import version

from mathinterpreter.calculate import calc
from mathinterpreter.interpreter import Interpreter
from mathinterpreter.lexer import Lexer
from mathinterpreter.parser import Parser

__version__ = version("mathinterpreter")
