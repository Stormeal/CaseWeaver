import os
import pandas as pd

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