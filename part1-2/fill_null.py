import pandas as pd
from data_load import dataset


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