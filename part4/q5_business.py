#What are the top 5 products by total revenue? By total quantity sold? (Are they the same 5? Why might they differ?)
from q4_business import dataset
import pandas as pd
import numpy as np
print(dataset["total_amount"])

print(dataset["total_amount"].sum())

def top_5_products_by_revenue(dataset: pd.DataFrame):
    return (
        dataset.groupby("product_name")["total_amount"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

print(top_5_products_by_revenue(dataset))

