import os
import keyboard
import pandas as pd

if os.name == "nt":
    import msvcrt

from assets.art import logo
from helper.helper import (
    clear_screen,
    convert_dict_to_dataframe,
    create_csv_file,
    csv_progress_bar,
)
from test_case_view import ds_test_case, tc_handle_user_input

menu_index: int = 0
tc_menu_index: int = 0


def initialize_tc_interface():
    clear_screen(1, menu_index, tc_menu_index, logo)
    print(
        "Welcome to ScriptWeaver, I'm here to help you create Test Cases for your projects!\nYou have a few options to choose from:"
    )
    menu()


def get_keypress():
    if os.name == "nt":
        key = msvcrt.getch()
        return key.decode("utf-8") if isinstance(key, bytes) else key


def menu():
    global menu_index
    if menu_index == 0:
        print(
            "[1] Create a new Test Case | [2] Edit an existing Test Case | [3] Delete a Test Case | [4] Exit\n"
        )
        print("To return to this page, you can always press 'Home'")

        while menu_index == 0:
            key = get_keypress()
            if key == "1":
                menu_index = 1
                sub_menu()
            elif key == "4":
                exit()
            elif key == "Home":
                initialize_tc_interface()


def sub_menu():
    global tc_menu_index

    sub_menu_input = ""
    clear_screen(1, menu_index, tc_menu_index, logo)

    print(
        "[1] Create a new Test Case | [2] DanskeSpil A/S - Test Case | [4] Return to Main Menu"
    )

    while tc_menu_index == 0:
        key = get_keypress()
        if key == "1":
            tc_menu_index = 1
            menu_new_test_case(1)
        elif key == "2":
            tc_menu_index = 2
            menu_new_test_case(2)
        elif key == "4":
            initialize_tc_interface()


def menu_new_test_case(option: int):
    global menu_index
    global tc_menu_index

    csv_file_path = ""

    match option:
        case 1:
            csv_file_path = "src/data/test_case_data.csv"
            clear_screen(1, menu_index, tc_menu_index, logo)
            data = tc_handle_user_input(csv_file_path)
            wrap_csv(data, csv_file_path)

        case 2:
            csv_file_path = "src/data/ds_test_case_data.csv"
            clear_screen(1, menu_index, tc_menu_index, logo)
            data = ds_test_case()
            wrap_csv(data, csv_file_path)


def wrap_csv(data, csv_file_path):
    global menu_index, tc_menu_index

    df = convert_dict_to_dataframe(data)
    create_csv_file(df, csv_file_path)
    csv_progress_bar(csv_file_path)

    menu_index = 0
    tc_menu_index = 0
    initialize_tc_interface()
