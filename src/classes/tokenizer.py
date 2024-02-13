# This class is responsible for tokenizing the input expression
# into a list of tokens to be used by the Shunting Yard algorithm.
#
# Methods:
# - tokenize: returns a list of tokens from the input expression
class Tokenizer:
    def __init__(self):
        self.operators = set(["+", "-", "*", "/", "^", "(", ")"])

    def tokenize(self, expression: str) -> list:
        tokens = []
        negative = False
        num_start = None  # to keep track of the start index of a number

        for i, char in enumerate(expression):
            # check if previous and next index can be accessed
            is_in_middle = 0 < i < (len(expression) - 1)

            # if current character is a digit
            if char.isdigit():
                if num_start is None:
                     # set the start index of the number
                    num_start = i
                else:
                    continue

            # if current character is an operator
            if char in self.operators:
                first_match = i == 0 and expression[i + 1].isdigit()

                # the number ends if it has started
                if num_start is not None:
                    number = expression[num_start:i].strip()
                    tokens.append(f"-{number}" if negative else number)
                    negative = False
                    num_start = None

                # if current character is a negative sign
                if char == "-":
                    # if the negative sign is a unary negation (previous char is
                    # a space (or left parenthesis) and next char is a digit
                    # OR first to match)
                    if first_match or (is_in_middle and \
                      (expression[i - 1] == "" or expression[i - 1] == "(") and \
                      expression[i + 1].isdigit()):
                        negative = True
                        continue
                # if current character is a plus sign
                elif char == "+":
                    # if the plus sign is used to implicitly denote a positive
                    # number (previous char is a space (or left parenthesis) and
                    # next char is a digit)
                    if first_match or (is_in_middle and \
                      (expression[i - 1] == "" or expression[i - 1] == "(") and \
                      expression[i + 1].isdigit()):
                        negative = False
                        continue

                # otherwise, add the operator to tokens
                tokens.append(char)

        # if the expression ends with a number, add it to tokens
        if num_start is not None:
            tokens.append(expression[num_start:].strip())

        return tokens
