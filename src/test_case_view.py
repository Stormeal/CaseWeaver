import datetime

from helper.helper import current_csv_count, format_time
from helper.test_case_helper import (
    generate_test_case_id,
    tc_data,
    tc_preconditions,
    tc_steps,
)


def tc_handle_user_input(csv_file_path):
    """
    Asks the user for input and returns a dictionary containing the test case data.
    """

    tc_id: str = generate_test_case_id(current_csv_count(csv_file_path))
    tc_title = str(input("Test Case Title: "))
    tc_desc: str = str(input("Test Description: "))
    tc_req_id: str = str(input("Requirement ID: "))
    tc_req_title: str = str(input("Requirement title: "))
    ac_id: int = int(input("Acceptance Criteria ID: "))
    ac_desc: str = str(input("Acceptance Criteria Description: "))
    preconditions: list = tc_preconditions()
    test_type: str = str(input("Test Type: ")).lower()
    test_steps: list = tc_steps()
    test_data: dict = tc_data()
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
        "tc_preconditions": [str(preconditions)],
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


def ds_test_case():
    """
    Asks the user for input and returns a dictionary containing the test case data.
    """
    csv_file_path = "src/data/ds_test_case_data.csv"

    tc_id: str = generate_test_case_id(current_csv_count(csv_file_path))
    tc_summary = str(input("Summary: "))
    tc_desc: str = str(input("Description: "))
    test_steps: list = tc_steps()
    test_data: dict = tc_data()
    expected_result: str = str(input("Expected Result: "))
    tc_req_id: str = str(input("Requirement ID: "))
    tc_req_title: str = str(input("Requirement title: "))
    ac_id: int = int(input("Acceptance Criteria ID: "))
    ac_desc: str = str(input("Acceptance Criteria Description: "))
    preconditions: list = tc_preconditions()
    created_time = format_time(datetime.datetime.now())
    domain: str = str(input("Domain: "))
    label: str = str(input("Label: "))

    data = {
        "tc_id": [tc_id],
        "tc_summary": [tc_summary],
        "tc_desc": [tc_desc],
        "tc_req_id": [tc_req_id],
        "tc_req_title": [tc_req_title],
        "ac_id": [ac_id],
        "ac_desc": [ac_desc],
        "tc_preconditions": [str(preconditions)],
        "test_steps": [str(test_steps)],
        "test_data": [str(test_data)],
        "expected_result": [expected_result],
        "created_time": [created_time],
        "domain": [domain],
        "label": [label],
    }

    return data
