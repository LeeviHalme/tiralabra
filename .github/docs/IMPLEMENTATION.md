# Implementation

This document will describe the app structure, implementation of the shunting-yard algorithm, infix vs postfix notation, postfix evaluation and custom data structures.

## Structure

The app is a CLI (command line interface) tool that takes a mathematical expression written in natural notation as input and outputs the result of the expression. Internally, it uses the shunting-yard algorithm to convert the expression to postfix notation and then evaluates the postfix expression using a custom parser to get the result.

You can see all the available commands by running:

```bash
poetry run poe cli --help
```

## Shunting-yard algorithm

The shunting-yard algorithm is a method for parsing mathematical expressions written in infix notation. It was invented and published by Edsger Dijkstra in 1961 and named after its operation resembles a railroad shunting yard. The algorithm can be explained in the following steps:

1. Read the input: `3 + 4`
2. Push `3` to the output queue
3. Check the operator `+` and compare it to the operator stack
4. Push the operator `+` to the operator stack
5. Push `4` to the output queue
6. Pop the operators from the operator stack to the output queue
7. Output queue: `3 4 +`

Now the infix notation `(3 + 4)` is converted to postfix notation `(3 4 +)` and can be evaluated.

### Operator precedence

In step 3, the algorithm checks the precedence of the operators. If the operator on the top of the stack has higher precedence than the operator that is being read, the operator on the top of the stack is popped to the output queue before the new operator is pushed to the stack. This is done until the operator on the top of the stack has lower precedence than the new operator.

The algorithm is implemented in the `classes/shunting_yard.py` file.

[YouTube: "Comp Sci in 5: Shunting Yard Algorithm"](https://www.youtube.com/watch?v=Wz85Hiwi5MY)

## Infix vs Postfix notation

Infix and Postfix are mathematical notations, that offer different ways of writing expressions. In Infix, operators are between operands. This is also sometimes called the conventional mathematical order or the natural notation.

Using Postfix, or Reverse Polish Notation, the operators are after operands. The advantage of postfix notation is that it removes the need for parenthesis and is easier to calculate.

## Postfix evaluation

[YouTube: "Comp Sci in 5: Post Fix Stack Evaluator"](https://www.youtube.com/watch?v=bebqXO8H4eA)

## Custom data structures

The app uses two custom data structures: `Stack` and `Queue` that can be found in `classes/stack.py` and `classes/queue.py` respectively. Both are implemented using Python's built-in `queue` structure.

## Sources

- [Wikipedia: Shunting-yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm)
- [Github: codecocodes/swift-algorithm-club, Shunting Yard](https://aquarchitect.github.io/swift-algorithm-club/Shunting%20Yard/)
- [Wikipedia: Stack (abstract data type)](<https://en.wikipedia.org/wiki/Stack_(abstract_data_type)>)
- [Wikipedia: Queue (abstract data type)](<https://en.wikipedia.org/wiki/Queue_(abstract_data_type)>)
- [Wikipedia: Infix notation](https://en.wikipedia.org/wiki/Infix_notation)
- [Wikipedia: Reverse Polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)
