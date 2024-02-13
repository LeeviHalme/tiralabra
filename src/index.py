import click
from classes.shunting_yard import ShuntingYard
from classes.tokenizer import Tokenizer

@click.command()
@click.argument("infix_expression", type=click.STRING, required=True)
@click.option("--v", is_flag=True, type=click.BOOL, \
              help="Verbose mode (prints out algorithm steps)")
# @click.option("-vars", help="Variables list")
def evaluate(infix_expression: str, v: bool) -> int:
    # create a list of tokens from the expression
    tkn = Tokenizer()
    alg = ShuntingYard(verbose=v)

    # parse the expression
    token_list = tkn.tokenize(infix_expression)
    postfix_expression = alg.parse(token_list)

    print(f"{"Input:":25} {infix_expression}")
    print(f"{"Parsed Tokens:":25}", token_list)
    print(f"{"Converted Postfix (RPN):":25}", postfix_expression)
    print(f"{"Evaluated RNP (result):":25}", None, "(not implemented yet)")

# on init, run the main command
if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    evaluate()
