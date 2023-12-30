import pandas as pd
import pathlib
import numpy as np
import yaml
import sys
from sklearn.model_selection import train_test_split
# reading data from csv file
def load_input(file_path):
    df = pd.read_csv(file_path)
    return df
def split_data(df,test_split,seed):
    train,test = train_test_split(df,test_size=test_split,random_state=seed)
    return train,test
def save_data(train,test,output_path):
    pathlib.Path(output_path).mkdir(parents=True,exist_ok=True)
    train.to_csv(output_path+'\train.csv',index = False)
    test.to_csv(output_path+'\test.csv',index= False)

def main():
    current_directory = pathlib.Path(__file__)
    home_directory = current_directory.parent.parent.parent
    params_file = home_directory.as_posix()+'params.yaml'
    params = yaml.safe_load(open(params_file))['make_dataset']

    input_file = sys.argv[1]
    data_path = home_directory.as_posix()+input_file
    output_path = home_directory.as_posix()+'data/processed'

    data = load_input(data_path)
    train_data,test_data = split_data(data,params['test_split'],params['seed'])
    save_data(train_data,test_data,output_path=)

if __name__ == "__main__":
    main()