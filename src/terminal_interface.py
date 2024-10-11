from assets.art import logo
import os
import keyboard
import datetime
import csv

menu_index: int = 0
csv_file_path = "data/test_case_data.csv"


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
        f"[1] Create a new Test Case | [2] Edit an existing Test Case | [3] Delete a Test Case | [4] Exit\n"
    )
    print(f"To return to this page, you can always press 'Home'")


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


def menu_new_test_case():
    clear_screen()
    tc_title = str(
        input(
            f"Test Case Title \nA short description of the test, e.g., 'Verify login functionality with valid credentials\n"
        )
    )

    clear_screen()
    print(f"TC Title: {tc_title}")
    tc_desc: str = str(input("Test Description: "))
    tc_req_id: str = str(input("Requirement ID: "))
    tc_req_title: str = str(input("Requirement title: "))
    ac_id: int = int(input("Acceptance Criteria ID: "))
    ac_desc: str = str(input("Acceptance Criteria Description: "))
    tc_preconditions: list = new_test_case_preconditions()
    test_type: str = str(
        input("Test Type (Ex: GUI, Acceptance, Integration etc.): ")
    ).lower()
    test_steps: list = new_test_case_steps()
    test_data: dict = new_test_case_data()
    expected_result: str = str(input("Expected Result: "))
    actual_result: str = str(input("Actual Result: "))
    test_status = ""
    # created_time: datetime = datetime.now()
    implemented_time = ""
    domain: str = str(input("Domain: "))
    label: str = str(input("Label: "))

    headers = [
        "Test Description",
        "Requirement ID",
        "Requirement Title",
        "Acceptance Criteria ID",
        "Acceptance Criteria Description",
        "Preconditions",
        "Test Type",
        "Test Steps",
        "Test Data",
        "Expected Result",
        "Actual Result",
        "Test Status",
        "Created Time",
        "Implemented Time",
        "Domain",
        "Label",
    ]

    test_case_data = {
        "Test Description": tc_desc,
        "Requirement ID": tc_req_id,
        "Requirement Title": tc_req_title,
        "Acceptance Criteria ID": ac_id,
        "Acceptance Criteria Description": ac_desc,
        "Preconditions": str(tc_preconditions),
        "Test Type": test_type,
        "Test Steps": str(test_steps),
        "Test Data": str(test_data),
        "Expected Result": expected_result,
        "Actual Result": actual_result,
        "Test Status": test_status,
        # "Created Time": created_time,
        "Implemented Time": implemented_time,
        "Domain": domain,
        "Label": label,
    }

    with open(csv_file_path, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(test_case_data)

    print(f"Test case data successfully saved to {csv_file_path}")


def new_test_case_preconditions():
    tc_preconditions: list = []
    new_precondition: bool = True

    os.makedirs("data", exist_ok=True)

    print(
        "Please type each pre-condition for given test case, seperated by pressing enter. \nBy pressing enter without giving any input concludes the pre-conditions."
    )
    while new_precondition:
        precondition = str(input(f"{len(tc_preconditions) + 1}: "))

        if precondition == "":
            new_precondition = False
        else:
            tc_preconditions.append(precondition)

    print(tc_preconditions)


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
    print(tc_steps)


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

    print(tc_data)
