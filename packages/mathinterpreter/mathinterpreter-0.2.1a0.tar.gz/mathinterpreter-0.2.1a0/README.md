
![Static Badge](https://img.shields.io/badge/python-%3E%3D3.10-blue?style=flat&logo=python&logoColor=green&label=Python&color=green) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) ![Static Badge](https://img.shields.io/badge/unit_test-pytest-blue?style=flat&logo=pytest)

# Python - Math Interpreter

An interpreter, written from scratch in Python, that can evaluate simple math calculations, with a simple Read-Eval-Print-Loop (REPL) command line interface. This project is based on  [py-simple-math-interpreter](https://github.com/davidcallanan/py-simple-math-interpreter), by David Callanan and illustrates the use of software engineering techniques to evolve a prototype code into a professional software. 

Since our objective is to create an education/professional example we didn't change the original business logic, *i.e.*, we do not change the interpretor code. Besides the four basic operations ( addition, subtraction, multiplication, and division) we implemented the power operator `^` to calculate `a^b` and the modulo operator `%`.

## How to install and run the REPL


### Using pipx (recommended)

To use this project as a standalone command line tool install [pipx](https://pipx.pypa.io/stable/installation/) and run:

```bash
pipx install git+https://github.com/ScientificThought/py-math-interpreter
```

### Install using pip

If you want to install this package and use it as a library on another project you ccan use `pip` and a virtual environment manager.  There are many ways to do that but if you already know how to setup a virtual environment, probably you could proceed your way. 

In our development setup we use `venv`, which comes with python, on Ubuntu Linux. If you are new to software development, follow the steps we recommend below which is expect to work on any Linux Distribution.

Create a new directory and a new virtual environment for working with `mathinterpreter`:

```bash
mkdir mynewproject
cd mynewproject
python -m venv env
source env/bin/activate
```
Note that `mynewproject` could be any name of your choice and that instead of using `source` you could simply use the `.` command. After activating your new environment, install the package from source using pip:

```bash
python -m pip install git+https://github.com/ScientificThought/py-math-interpreter.git
```
At this point you can run the REPL, from the directory in which you installed the package by typing `mathinterpreter` in your terminal. This will open the REPL terminal of the interpreter and you can now use it for evaluating math expressions:
```
$ mathinterpreter
calc > 1+1        
2.0
calc > (3.0+2*2)/3
2.3333333333333335
calc > q
$ 
```
Just type `q` or `quit` followed by enter  in the REPL to return to your shell. That's it.

### How to use this package as Python module

You can import the module `mathinterpreter` from your python code and use the function `calc` to evaluate expressions, as in the following:
```python
from mathinterpreter import calc

value = calc('1 + 3*(5*2+1)/2')
print(value)
```
To using `mathinterpreter` as a library you will need to import the Lexer, the Parser, and the Interpreter classes. For understanding how the interpreter works we recommend you to look the files `mathinterpreter/__main__.py` and `mathinterpreter/calculate.py`, which implement the REPL.

## What we have done and what we are doing

### Current implementation includes:**

*Version*: 2024.05.07
- library `mathinterpreter` (Lexer, Parser, Interpreter, and a `calc()`, to simplify calculations);
- a simple command line interface, `mathinterpreter`, using a simple REPL;


### Project Software Stack

- pip: for package installation frontend;
- setuptools: for package installation backend;
- pytest: for unit tests;
- black: for automatic code formatting;
- GitHub Action Scripts: for CI Automation;

### Planned improvements
We track feature requests with issues. But we aim to implement:

- implement code coverage;
- expand the tests suit;
- improve the cli:
    - use `argparse` to improve the cli usage, allowing the user to call `mathinterpreter "1+1"`, for example.    
    - make the REPL more user friendly;

## Contributing

Please take a look on our [contributing guide](doc/guides/contributing.md).

## Who we are?

We are [Marco Barbosa](@aureliobarbosa) and [Henrique Guidi](@hsguidi), colleagues which got 
involved with computation while doing PhD in Physics at University of São Paulo. 

ScientificThoughts was created as an online place to develop interesting small projects to improving 
our software engineering techniques. Want to join us? Just contact us.