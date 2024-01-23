import click
from classes.stack import Stack

@click.command()
@click.argument("infix_expression", type=click.STRING, required=True)
# @click.option("--vars", help="Variables list")
def evaluate(infix_expression: str) -> int:
    stack = Stack()

    stack.push("+1")
    stack.push("+2")
    stack.push("+3")
    print(stack.peek())
    stack.pop()
    print(stack.peek())

    click.echo(infix_expression)
    click.echo(0)

# on init, run the main command
if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    evaluate()
