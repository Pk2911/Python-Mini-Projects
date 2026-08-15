import os


def clear_screen():
    """
    Clears the terminal screen.
    """

    os.system("cls" if os.name == "nt" else "clear")


def pause():
    """
    Pause until the user presses Enter.
    """

    input("\nPress Enter to continue...")


def print_header(title):
    """
    Prints a formatted section header.
    """

    print("\n" + "=" * 45)
    print(title.center(45))
    print("=" * 45)