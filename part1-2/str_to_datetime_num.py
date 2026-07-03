import pandas as pd
from fill_null import dataset
#function to change string values in numeric columns

#function to change value of column in lowercase for standardization
def to_lower_case(value):
    return value.lower()


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

#converting string values in quantity column into num (int or float)
dataset["quantity"] = dataset["quantity"].apply(lambda x: str_to_num(x))
#converting string type columns into lowercase for standardization
dataset["customer_name"] = dataset["customer_name"].apply(lambda x: to_lower_case(x))
dataset["product_category"] = dataset["product_category"].apply(lambda x: to_lower_case(x))
dataset["product_name"] = dataset["product_name"].apply(lambda x: to_lower_case(x))
dataset["region"] = dataset["region"].apply(lambda x: to_lower_case(x))
dataset["payment_method"] = dataset['payment_method'].apply(lambda x: to_lower_case(x))
dataset["order_status"] = dataset["order_status"].apply(lambda x: x.upper())


dataset["unit_price"] = (
    dataset["unit_price"]
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)
#converting string values in quantity column into num (int or float)
# dataset["quantity"] = dataset["quantity"].apply(lambda x: str_to_num(x))

dataset["order_date"] = dataset["order_date"].apply(lambda x: str_to_datetime(x))
print(dataset["order_date"].unique())
print(dataset["order_date"].dtype)
