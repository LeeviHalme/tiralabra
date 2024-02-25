import click
from classes.shunting_yard import ShuntingYard
from classes.tokenizer import Tokenizer
from classes.rpn_evaluator import RPNEvaluator

@click.command()
@click.argument("infix_expression", type=click.STRING, required=False)
@click.option("--v", is_flag=True, type=click.BOOL, \
              help="Verbose mode (prints out algorithm steps)")
@click.option("--exp", type=click.STRING, help="Expression to evaluate")
# @click.option("-vars", help="Variables list")
def evaluate(infix_expression: str, v: bool, exp: str) -> int:
    # create a list of tokens from the expression
    tkn = Tokenizer()
    alg = ShuntingYard(verbose=v)
    rpn = RPNEvaluator(verbose=v)

    if not infix_expression and not exp:
        raise click.BadParameter("No expression provided")

    print(r"""
   _____      _            _   _  __ _         _____      _            _       _             
  / ____|    (_)          | | (_)/ _(_)       / ____|    | |          | |     | |            
 | (___   ___ _  ___ _ __ | |_ _| |_ _  ___  | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
  \___ \ / __| |/ _ \ '_ \| __| |  _| |/ __| | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
  ____) | (__| |  __/ | | | |_| | | | | (__  | |___| (_| | | (__| |_| | | (_| | || (_) | |   
 |_____/ \___|_|\___|_| |_|\__|_|_| |_|\___|  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
""")
    print(f"{"Input:":25} {infix_expression}")
    # parse the expression
    token_list = tkn.tokenize(infix_expression or exp)
    print(f"{"Parsed Tokens:":25}", token_list)
    postfix_expression = alg.parse(token_list)
    print(f"{"Converted Postfix (RPN):":25}", postfix_expression)
    print()
    result = rpn.evaluate(postfix_expression)
    print(f"{"Evaluated RNP (result):":25}", f"{result:g}")

# on init, run the main command
if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    evaluate()
