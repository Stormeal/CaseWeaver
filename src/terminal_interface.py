from assets.art import logo
import os
import keyboard
import pandas as pd
import datetime

menu_index: int = 0
csv_file_path = "src/data/test_case_data.csv"


def clear_screen():
    global menu_index

    os.system("cls||clear")
    print(logo)
    if menu_index > 0:
        print(current_menu(menu_index))
        print("----------------------------------------------------")


def current_menu(menu_index: int):
    match menu_index:
        case 1:
            return "Create a new Test Case"
        case _:
            return ""


def initialize_tc_interface():
    clear_screen()
    print(
        "Welcome to ScriptWeaver, I'm here to help you create Test Cases for your projects!\nYou have a few options to choose from:"
    )
    menu()
    handle_input()


def menu():
    print(
        "[1] Create a new Test Case | [2] Edit an existing Test Case | [3] Delete a Test Case | [4] Exit\n"
    )
    print("To return to this page, you can always press 'Home'")


def handle_input():
    global menu_index

    while menu_index == 0:
        if keyboard.is_pressed("1"):
            menu_index = 1
            menu_new_test_case()
            return menu_index
        elif keyboard.is_pressed("4"):
            exit()
        elif keyboard.is_pressed("Home"):
            initialize_tc_interface()


def generate_test_case_id(current_count):
    return f"TC{current_count:03d}"


if os.path.exists(csv_file_path):
    existing_df = pd.read_csv(csv_file_path)
    current_count = len(existing_df) + 1
else:
    current_count = 1


def menu_new_test_case():
    clear_screen()

    data = handle_user_input()
    df = convert_dict_to_dataframe(data)
    create_csv_file(df)
    print(f"Test case data successfully saved to {csv_file_path}")


def handle_user_input():
    """
    Asks the user for input and returns a dictionary containing the test case data.
    """

    tc_id: str = generate_test_case_id(current_count)
    tc_title = str(input("Test Case Title: "))
    tc_desc: str = str(input("Test Description: "))
    tc_req_id: str = str(input("Requirement ID: "))
    tc_req_title: str = str(input("Requirement title: "))
    ac_id: int = int(input("Acceptance Criteria ID: "))
    ac_desc: str = str(input("Acceptance Criteria Description: "))
    tc_preconditions: list = new_test_case_preconditions()
    test_type: str = str(input("Test Type: ")).lower()
    test_steps: list = new_test_case_steps()
    test_data: dict = new_test_case_data()
    expected_result: str = str(input("Expected Result: "))
    actual_result: str = str(input("Actual Result: "))
    test_status = ""
    created_time = format_time(datetime.datetime.now())
    implemented_time = ""
    domain: str = str(input("Domain: "))
    label: str = str(input("Label: "))

    data = {
        "tc_id": [tc_id],
        "tc_title": [tc_title],
        "tc_desc": [tc_desc],
        "tc_req_id": [tc_req_id],
        "tc_req_title": [tc_req_title],
        "ac_id": [ac_id],
        "ac_desc": [ac_desc],
        "tc_preconditions": [str(tc_preconditions)],
        "test_type": [test_type],
        "test_steps": [str(test_steps)],
        "test_data": [str(test_data)],
        "expected_result": [expected_result],
        "actual_result": [actual_result],
        "test_status": [test_status],
        "created_time": [created_time],
        "implemented_time": [implemented_time],
        "domain": [domain],
        "label": [label],
    }

    return data


def format_time(datetime):
    return datetime.strftime("%d/%m/%Y - %H:%M")


def new_test_case_preconditions():
    tc_preconditions: list = []
    new_precondition: bool = True

    print(
        "Please type each pre-condition for given test case, seperated by pressing enter. \nBy pressing enter without giving any input concludes the pre-conditions."
    )
    while new_precondition:
        precondition = str(input(f"{len(tc_preconditions) + 1}: "))

        if precondition == "":
            new_precondition = False
        else:
            tc_preconditions.append(precondition)

    return tc_preconditions


def new_test_case_steps():
    tc_steps: list = []
    new_step: bool = True

    print(
        "Please type each test-step for given test case, seperated by pressing enter. \nBy pressing enter without giving any input concludes the test steps."
    )
    while new_step:
        step = str(input(f"{len(tc_steps) + 1}: "))

        if step == "":
            new_step = False
        else:
            tc_steps.append(step)

    return tc_steps


def new_test_case_data():
    tc_data: dict = {}
    new_data: bool = True

    print(
        "Please type each dataset for given test case, seperated by pressing enter. \nBy pressing enter without giving any key input concludes the test data.\nThe first input will be the key then value."
    )
    print(
        "A key symbolizes a unique identifier for the value. Ex: key = 'username', value = 'Jane Doe'"
    )

    while new_data:
        key = str(input(f"Key: {len(tc_data) + 1}: "))

        if key == "":
            new_data = False
        else:
            value = str(input(f"Value: {len(tc_data) + 1}: "))
            tc_data[key] = value

    return tc_data


def convert_dict_to_dataframe(data: dict):
    # Converts the dictionary to DataFrame
    df = pd.DataFrame(data)
    return df


def create_csv_file(dataframe):
    if os.path.exists(csv_file_path):
        dataframe.to_csv(csv_file_path, mode="a", header=False, index=False)
    else:
        dataframe.to_csv(csv_file_path, index=False)
