import pandas as pd
from drop_duplicates import dataset
#function to strip white spaces from string columns
def strip_white_spaces(dataset: pd.DataFrame):
    dataset["customer_name"] = dataset["customer_name"].str.strip()
    dataset["product_name"] = dataset["product_name"].str.strip()
    dataset["product_category"] = dataset["product_category"].str.strip()
    dataset["region"] = dataset["region"].str.strip()
    dataset["payment_method"] = dataset["payment_method"].str.strip()
    dataset["order_status"] = dataset["order_status"].str.strip()

strip_white_spaces(dataset)

print(dataset.head(10))
