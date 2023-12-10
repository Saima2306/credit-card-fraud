import pandas as pd
# reading data from csv file
def read_input_file(file_path):
    return pd.read_csv(file_path)