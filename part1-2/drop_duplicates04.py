import pandas as pd
from str_to_datetime_num03 import dataset
def check_dataset_duplicates(dataset:pd.DataFrame):
    duplicates = dataset.duplicated()
    return duplicates.value_counts()

print(check_dataset_duplicates(dataset))

dataset = dataset.drop_duplicates()

print(check_dataset_duplicates(dataset))