import os
import time
import pandas as pd


def clear_screen(option: int, menu_index, logo):
    match option:
        case 1:
            os.system("cls||clear")
            print(logo)
            if menu_index > 0:
                print(current_menu(menu_index))
                print("----------------------------------------------------")
        case _:
            return "Incorrect option"


def current_menu(menu_index: int):
    match menu_index:
        case 1:
            return "Create a new Test Case"
        case _:
            return ""


def format_time(datetime):
    return datetime.strftime("%d/%m/%Y - %H:%M")


def convert_dict_to_dataframe(data: dict):
    # Converts the dictionary to DataFrame
    df = pd.DataFrame(data)
    return df


def create_csv_file(dataframe, csv_file_path):
    if os.path.exists(csv_file_path):
        dataframe.to_csv(csv_file_path, mode="a", header=False, index=False)
    else:
        dataframe.to_csv(csv_file_path, index=False)


def current_csv_count(csv_file_path):
    if os.path.exists(csv_file_path):
        existing_df = pd.read_csv(csv_file_path)
        return len(existing_df) + 1
    else:
        return 1


def printProgressBar(
    iteration,
    total,
    prefix="",
    suffix="",
    decimals=1,
    length=100,
    fill="█",
    printEnd="\r",
):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + "-" * (length - filledLength)
    print(f"\r{prefix} |{bar}| {percent}% {suffix}", end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


def csv_progress_bar(csv_file_path):
    df = pd.read_csv(csv_file_path)  # Replace with the path to your CSV file

    # Get the total number of columns to be processed
    total_columns = len(df.columns)

    # Initial call to print 0% progress
    printProgressBar(0, total_columns, prefix="Progress:", suffix="Complete", length=50)

    # Iterate over each column in the CSV
    for i, column in enumerate(df.columns):
        # Do stuff with the column...
        time.sleep(0.1)  # Simulating work with sleep

        # Update Progress Bar
        printProgressBar(
            i + 1, total_columns, prefix="Progress:", suffix="Complete", length=50
        )

    print(f"Test case data successfully saved to {csv_file_path}")

    time.sleep(1)
