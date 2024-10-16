def generate_test_case_id(current_count):
    return f"TC{current_count:03d}"


def tc_preconditions():
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


def tc_steps():
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

    return [step for step in tc_steps if step.strip()]


def tc_data():
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



