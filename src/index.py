from ui import start_cli

# on init, run the main command
if __name__ == "__main__":
    try:
        # pylint: disable=no-value-for-parameter
        start_cli()
    except KeyboardInterrupt:
        print("Bye!")
