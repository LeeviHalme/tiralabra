# Custom data structure to store tokens and variables
#
# Methods:
# - is_variable_assignment: returns True if the token list contains a variable assignment
# - __str__: returns prettified string representation of the token list
class TokenList:
    def __init__(self, tokens: list, variables: dict) -> None:
        self.tokens = tokens
        self.variables = variables

    def is_variable_assignment(self) -> bool:
        return len(self.variables.keys()) > 0

    def __str__(self) -> str:
        variables = ", ".join(
            [f"{k}: {v.tokens}" for k, v in self.variables.items()]
        )
        return f"\n Tokens: [{", ".join(self.tokens)}] \n Variables: {variables}"
