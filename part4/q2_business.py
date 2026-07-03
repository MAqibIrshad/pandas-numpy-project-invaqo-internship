from q1_business import dataset
import pandas as pd
import numpy as np

print(dataset["order_id"].dtype)

mapping = {
    "e": "east",
    "w": "west",
    "n": "north",
    "s": "south"
}

dataset["region"] = dataset["region"].replace(mapping)

def found_orders_per_region(dataset: pd.DataFrame):
    all_orders_by_region = dataset.groupby("region")["order_id"].count()
    return all_orders_by_region, dataset

print(f"Orders Per Region...")
print("=======================")
all_orders_by_region, dataset = found_orders_per_region(dataset=dataset)
print(all_orders_by_region)