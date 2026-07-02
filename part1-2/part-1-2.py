import pandas as pd
import numpy as np
import re
dataset = pd.read_csv("messy_orders.csv")
print(dataset.head(10))
print(dataset.info())
print(dataset.describe())

print(dataset.isna().sum())

fill_na = "aqibirshad99@gmail.com"
print(dataset["customer_email"])

#filling null values
dataset["customer_email"] = dataset["customer_email"].fillna(fill_na)
dataset["quantity"] = dataset["quantity"].fillna("3 units")
dataset["unit_price"] = dataset["unit_price"].fillna("$177.1")
dataset["discount_percent"] = dataset["discount_percent"].fillna(2.0)
dataset["shipping_cost"] = dataset["shipping_cost"].fillna(7.5)
dataset["region"] = dataset["region"].fillna("EAST")
dataset["payment_method"] = dataset["payment_method"].fillna("JAZZCASH")



print(dataset.isna().sum())
#function to change value of column in lowercase for standardization
def to_lower_case(value):
    return value.lower()
#function to change string values in numeric columns

def str_to_datetime(value):
    if pd.isna(value):
        return pd.NaT

    formats = [
        "%B %d, %Y",
        "%d/%m/%Y",
        "%Y-%m-%d",
        "%Y/%m/%d",
        "%d-%m-%Y",
    ]

    for fmt in formats:
        try:
            return pd.to_datetime(value, format=fmt)
        except ValueError:
            continue

    return pd.NaT

   

            
        

def str_to_num(value):
    if isinstance(value, str):
        first = value.split()[0]
        if first.isdigit():
            return int(first)
        return None  
    return value

dataset["unit_price"] = (
    dataset["unit_price"]
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)
#converting string values in quantity column into num (int or float)
dataset["quantity"] = dataset["quantity"].apply(lambda x: str_to_num(x))
#converting string type columns into lowercase for standardization
dataset["customer_name"] = dataset["customer_name"].apply(lambda x: to_lower_case(x))
dataset["product_category"] = dataset["product_category"].apply(lambda x: to_lower_case(x))
dataset["product_name"] = dataset["product_name"].apply(lambda x: to_lower_case(x))
dataset["region"] = dataset["region"].apply(lambda x: to_lower_case(x))
dataset["payment_method"] = dataset['payment_method'].apply(lambda x: to_lower_case(x))
dataset["order_status"] = dataset["order_status"].apply(lambda x: x.upper())

print(dataset.head(10))

print(dataset.dtypes)

dataset["order_date"].dtype

duplicates = dataset.duplicated()
print(duplicates)

def check_dataset_duplicates(dataset:pd.DataFrame):
    duplicates = dataset.duplicated()
    return duplicates.value_counts()

print(check_dataset_duplicates(dataset))

dataset = dataset.drop_duplicates()

print(check_dataset_duplicates(dataset))

dataset["order_date"] = dataset["order_date"].apply(lambda x: str_to_datetime(x))
print(dataset["order_date"].unique())
print(dataset["order_date"].dtype)


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

#for data type error handling in numeric columns only

def to_numeric(dataset: pd.DataFrame):
    dataset["order_id"] = pd.to_numeric(dataset["order_id"])
    dataset["quantity"] = pd.to_numeric(dataset["quantity"])
    dataset["unit_price"] = pd.to_numeric(dataset["unit_price"])
    dataset["discount_percent"] = pd.to_numeric(dataset["discount_percent"])
    dataset["shipping_cost"] = pd.to_numeric(dataset["shipping_cost"])

to_numeric(dataset)

print(dataset.dtypes)

print(dataset["product_category"].head(20))

mapping = {
    "home & kitchen": "Home & Kitchen",
    "home&kitchen":"Home & Kitchen",
    "sports & outdoors": "Sports & Outdoors",
    "sports&outdoors": "Sports & Outdoors",
    "sports and outdoors": "Sports & Outdoors"
}

dataset["product_category"] = dataset["product_category"].replace(mapping)
print(dataset.head(10))

dataset.to_csv("cleaned_processed")






    

    

