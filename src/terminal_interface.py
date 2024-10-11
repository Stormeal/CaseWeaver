from assets.art import logo


def initialize_tc_interface():
    print(logo)
    print(
        "Welcome to ScriptWeaver, I'm here to help you create Test Cases for your projects!\nYou have a few options to choose from:"
    )


def main_menu():
    int(
        input(
            "[1] Create a new Test Case | [2] Edit an existing Test Case | [3] Delete a Test Case | [4] Exit\n"
        )
    )


initialize_tc_interface()
