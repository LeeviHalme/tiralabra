import click
from classes.shunting_yard import ShuntingYard
from classes.tokenizer import Tokenizer
from classes.rpn_evaluator import RPNEvaluator
from classes.exceptions import MalformedExpressionException
from utils.printers import print_logo, print_help_page

# global data structures
assigned_variables = {}

# evaluate a line of input
def evaluate_line(exp: str, verbose: bool) -> int:
    # initialize service classes
    tkn = Tokenizer()
    alg = ShuntingYard(verbose)
    rpn = RPNEvaluator(verbose)

    # parse the expression
    token_list = tkn.tokenize(exp)

    if token_list.is_variable_assignment():
        pass

    postfix_expression = alg.parse(token_list)
    result = rpn.evaluate(postfix_expression)

    if verbose:
        print(f"{"Input:":25} {exp}")
        print(f"{"Parsed Tokens:":25}", token_list)
        print(f"{"Converted Postfix (RPN):":25}", postfix_expression)
        print()
        print(f"{"Evaluated RNP (result):":25}", f"{result:g}")

    print(f"= {result:g}")

@click.command()
@click.option("--v", is_flag=True, type=click.BOOL, \
              help="Verbose mode (prints out algorithm steps)")
def start_cli(v: bool) -> int:
    print_logo()
    print("Type your expression below. Type :h to see the help page " \
           "and :q to quit.")
    print()

    # main input loop
    while True:
        exp = input("> ")

        # user issued quit command
        if exp == ":q":
            print("Bye!")
            break

        # user issued help command
        if exp == ":h":
            print_help_page()
            continue

        try:
            # otherwise, treat as expression
            evaluate_line(exp, v)
        except MalformedExpressionException as e:
            print(f"{type(e).__name__}: {e}")
