from os import system, name
import click
from classes.shunting_yard import ShuntingYard
from classes.tokenizer import Tokenizer
from classes.rpn_evaluator import RPNEvaluator
from classes.exceptions import MalformedExpressionException
from utils.printers import print_logo, print_help_page

# global data structures
assigned_variables = {}
BLUE = "\033[94m"
ENDC = "\033[0m"

# clear the console
def clear_console() -> None:
    if name == "nt":
        system("cls")
    else:
        system("clear")

# print a summary of the expression and its result
def print_summary(exp: str, token_list: list, postfix_expression: list, result: int) -> None:
    # pylint: disable=inconsistent-quotes
    line_length = max(len(exp),len(str(token_list)),
                          len(str(postfix_expression)), len(str(result))
                      ) + 25
    print("-" * line_length)
    print(f"{'Input:':25} {exp}")
    print(f"{'Tokenizer Result:':25}", token_list)
    print(f"{'Converted Postfix (RPN):':25}", postfix_expression)
    print("-" * line_length)
    print(f"{'Evaluated RNP (result):':25}", result)

# evaluate a line of input
def evaluate_line(exp: str, verbose: bool) -> int:
    # initialize service classes
    tkn = Tokenizer()
    alg = ShuntingYard(verbose)
    rpn = RPNEvaluator(verbose)

    # parse the expression
    token_list = tkn.tokenize(exp)

    # assign variables to local scope
    if token_list.is_variable_assignment():
        for variable in token_list.variables.keys():
            # evaluate the expression
            postfix_expression = alg.parse(token_list.variables[variable])
            result = rpn.evaluate(postfix_expression, assigned_variables)

            # store the result
            assigned_variables[variable] = result
            print(f"{BLUE}{variable}: {result:g}{ENDC}")
        return

    # evaluate the expression
    postfix_expression = alg.parse(token_list)
    result = rpn.evaluate(postfix_expression, assigned_variables)

    if verbose:
        print_summary(exp, token_list, postfix_expression, result)

    print(f"{BLUE}= {result:g}{ENDC}")

@click.command()
@click.option("--v", is_flag=True, type=click.BOOL, help="Verbose mode (prints algorithm steps)")
def start_cli(v: bool) -> int: # pylint: disable=too-many-statements
    print_logo()
    print("Type your expression below. Type :h to see the help page and :q to quit.")
    print()

    # main input loop
    while True:
        exp = input("▶ ")

        # user issued quit command
        if exp == ":q":
            print(f"{BLUE}Bye!{ENDC}")
            break

        # user issued help command
        if exp == ":h":
            print_help_page()
            continue

        if exp == ":c":
            clear_console()
            continue

        try:
            # otherwise, treat as expression
            evaluate_line(exp, v)
        except MalformedExpressionException as e:
            print(f"MalformedExpressionException: {e}")
