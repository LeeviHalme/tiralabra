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
    print()

    print(f"{"Verbose mode:":20}", "Start the program with the" \
          " -v flag to enable verbose mode.")

    print()

    print(f"{"Commands:":20}", "Type :q to quit the program.")
    print(f"{"":20}", "Type :h to see this help page.")

    print()

    print(f"{"Usage:":20}", "Type an expression to evaluate it. ")
    print(f"{"":25}", "Example: 2 + 2")
    print(f"{"":20}", "Assign variables to values.")
    print(f"{"":25}", "Example: x = 2")
    print(f"{"":20}", "Use variables in expressions.")
    print(f"{"":25}", "Example: x + 2")
    print(f"{"":20}", "Use functions in expressions. Available " \
          "functions: sin, cos, min, max.")
    print(f"{"":25}", "Example: sin(x) + 2")

    print()
