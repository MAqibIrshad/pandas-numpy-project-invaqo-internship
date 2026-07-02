import pandas as pd
from strip_white_spaces import dataset
#for data type error handling in numeric columns only

def to_numeric(dataset: pd.DataFrame):
    dataset["order_id"] = pd.to_numeric(dataset["order_id"])
    dataset["quantity"] = pd.to_numeric(dataset["quantity"])
    dataset["unit_price"] = pd.to_numeric(dataset["unit_price"])
    dataset["discount_percent"] = pd.to_numeric(dataset["discount_percent"])
    dataset["shipping_cost"] = pd.to_numeric(dataset["shipping_cost"])

to_numeric(dataset)

print(dataset.dtypes)