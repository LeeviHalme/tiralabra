# Requirements Specification

**Study Programme:** Tietojenkäsittelytieteen kandidiohjelma, TKTK <br />
**Topic:** Scientific Calculator <br /> **Programming language:** Python <br />
**Scope:** A scientific calculator that can evaluate mathematical expressions written in infix notation. <br />
**Peer Reviews:** I am able to review projects written in Python or Java.

All the project documentation will be written in English.

## Problem Statement

The calculator will be able to evaluate mathematical expressions written in [infix notation](https://en.wikipedia.org/wiki/Infix_notation). The calculator will support the following operators: `+`, `-`, `*`, `/`, `^`, `(`, `)`. It will also have support for variables, one-parameter functions (`sqrt`, `sin`) and two-parameter functions (`min`, `max`)

It is considered hard to evaluate mathematical expressions written in infix notation because of the operator precedence and the need to use parentheses to override the precedence. That is why we first need to convert the expression to [Reverse Polish notation (RPN)](https://en.wikipedia.org/wiki/Reverse_Polish_notation) using the [Shunting-yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm). After the expression is in RPN or postfix notation, we can evaluate the expression easily using a stack and applying the calculations to the top two elements.

## Used Algorithms and Data Structures

The calculator will use the [Shunting-yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm) to convert the infix notation to [Reverse Polish notation (RPN)](https://en.wikipedia.org/wiki/Reverse_Polish_notation) and then evaluate the expression and return the result.

The calculator will use a custom Stack data structure built with Python's built-in `deque`.

## Time Complexity Analysis

Stack is a data structure that has O(1) time complexity for adding and removing elements, while the shunting-yard algorithm has O(n) time complexity. The time will depend on the length of the expression, thus the calculator time complexity will be **O(n)**.

## Sources

- [Wikipedia: Infix notation](https://en.wikipedia.org/wiki/Infix_notation)
- [Wikipedia: Shunting-yard algorithm](https://en.wikipedia.org/wiki/Shunting-yard_algorithm)
- [Wikipedia: Reverse Polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)
