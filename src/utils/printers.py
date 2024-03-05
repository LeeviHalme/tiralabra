from collections import namedtuple

def print_logo() -> None:
    print(r"""
   _____      _            _   _  __ _         _____      _            _       _             
  / ____|    (_)          | | (_)/ _(_)       / ____|    | |          | |     | |            
 | (___   ___ _  ___ _ __ | |_ _| |_ _  ___  | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
  \___ \ / __| |/ _ \ '_ \| __| |  _| |/ __| | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
  ____) | (__| |  __/ | | | |_| | | | | (__  | |___| (_| | | (__| |_| | | (_| | || (_) | |   
 |_____/ \___|_|\___|_| |_|\__|_|_| |_|\___|  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
""")

def print_help_page() -> None:
    Line = namedtuple("Line", ["header", "text"])
    lines = [
        Line("Verbose mode:", "Start the program with the --v flag to enable verbose mode."),
        Line("Commands:", "Type :q to quit the program."),
        Line("", "Type :h to see this help page."),
        Line("Usage:", "Type an expression to evaluate it."),
        Line("", "Example: 2 + 2"),
        Line("", "Assign variables to values. Available variables: a-z"),
        Line("", "Example: x = 2"),
        Line("", "Use variables in expressions."),
        Line("", "Example: x + 2"),
        Line("", "Use functions in expressions. Available functions: sin, cos, min, max."),
        Line("", "Example: sin(x) + 2")
    ]

    print()

    for line in lines:
        print(f"{line.header:20}", line.text)

    print()
