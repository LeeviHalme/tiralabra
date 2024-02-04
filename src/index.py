import click
from classes.shunting_yard import ShuntingYard

@click.command()
@click.argument("infix_expression", type=click.STRING, required=True)
@click.option("-verbose", is_flag=True, type=click.BOOL, \
              help="Verbose mode (prints out algorithm steps)")
# @click.option("-vars", help="Variables list")
def evaluate(infix_expression: str, verbose: bool) -> int:
    alg = ShuntingYard(verbose)

    # parse the expression
    postfix_expression = alg.parse(infix_expression)

    print("POSTFIX:", postfix_expression)

# on init, run the main command
if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    evaluate()
