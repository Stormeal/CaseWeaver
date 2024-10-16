import os
import keyboard
import pandas as pd

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
    clear_screen(1, menu_index, logo)
    print(
        "Welcome to ScriptWeaver, I'm here to help you create Test Cases for your projects!\nYou have a few options to choose from:"
    )
    menu()


def menu():
    global menu_index
    if menu_index == 0:
        print(
            "[1] Create a new Test Case | [2] Edit an existing Test Case | [3] Delete a Test Case | [4] Exit\n"
        )
        print("To return to this page, you can always press 'Home'")

        while menu_index == 0:
            if keyboard.is_pressed("1"):
                menu_index = 1
                sub_menu()
            elif keyboard.is_pressed("4"):
                exit()
            elif keyboard.is_pressed("Home"):
                initialize_tc_interface()


def sub_menu():
    global tc_menu_index

    sub_menu_input = None
    clear_screen(1,menu_index, logo)
    if tc_menu_index == 0:
        sub_menu_input = str(
            input(
                "[1] Create a new Test Case | [2] DanskeSpil A/S - Test Case | [4] Return to Main Menu: "
            )
        )

    try:
        sub_menu_input = int(sub_menu_input)  # Convert input to integer
    except ValueError:
        print("Invalid input, returning to the home page.")
        initialize_tc_interface()
        return  # Exit the function if input is invalid

    match sub_menu_input:
        case 1:
            tc_menu_index = 1
            menu_new_test_case(1)
        case 2:
            tc_menu_index = 2
            menu_new_test_case(2)
        case 4:
            initialize_tc_interface()
        case _:
            print("Unknown command, returning to home page")
            initialize_tc_interface()


def menu_new_test_case(option: int):
    global menu_index
    global tc_menu_index

    csv_file_path = ""

    match option:
        case 1:
            csv_file_path = "src/data/test_case_data.csv"
            clear_screen(1, menu_index, logo)
            data = tc_handle_user_input(csv_file_path)
            wrap_csv(data, csv_file_path)

        case 2:
            csv_file_path = "src/data/ds_test_case_data.csv"
            clear_screen(1, menu_index, logo)
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