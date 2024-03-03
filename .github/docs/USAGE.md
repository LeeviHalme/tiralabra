# Usage Guide

The project is a simple command-line calculator that can evaluate mathematical expressions in infix notation. The program will throw an error if the expression is not valid and why.

## Gotchas

- All the operators must be explicitly written within the expression. For example, `2(3 + 4)` is not a valid expression, but `2 * (3 + 4)` is.
- Negative numbers must be written without spaces. For example, `-3 * 2` is a valid expression, but `- 3 * 2` is not.

## Getting Started

Get started by downloading the latest [GitHub release](https://github.com/LeeviHalme/tiralabra/releases).

### Prerequisites

- [Python >=3.12](https://www.python.org/downloads/)
- [Poetry >=1.7](https://python-poetry.org/)

### 1. Install dependencies with Poetry:

```bash
poetry install
```

### 2. Run the program:

Start the CLI tool and enter your mathematical expressions in the prompt. Input must be in infix notation and can contain the following tokens:

- Positive and negative integers
- Parentheses: `()`
- Basic operators: `+`, `-`, `*`, `/`
- Powers: `^`
- Minmax: `min()`, `max()`
- Trigonometric functions: `sin()`, `cos()`
- Available constants: `pi`, `e`
- Available variables: `a-z`

```bash
poetry run poe cli
```

> Quit the program by typing `:q` in the prompt

> View the help page by typing `:h` in the prompt

## Running tests

Run the tests with pytest:

```bash
poetry run poe test
```

## Generating a coverage report

Generate a coverage report in the `htmlcov` directory with coverage:

```bash
poetry run poe coverage
```

## Linting the code

Lint the code with pylint:

```bash
poetry run poe lint
```
