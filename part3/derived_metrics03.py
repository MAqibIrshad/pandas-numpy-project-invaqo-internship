#quantity × unit_price × (1 − discount_percent/100) + shipping_cost

from part3.boolean_masking_discount_percent02 import dataset
import pandas as pd
import numpy as np

dataset["total_amount"] = (dataset["quantity"] * dataset["unit_price"] * (1 - dataset["discount_percent"] + dataset["shipping_cost"]))

# print(dataset["total_amount"].info())
print(dataset["total_amount"].isna().sum())

dataset["total_amount"] = dataset["total_amount"].fillna(dataset["total_amount"].mean())

# print(dataset["total_amount"].info())
print(dataset["total_amount"].isna().sum())