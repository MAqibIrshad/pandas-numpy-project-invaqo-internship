from derived_metrics03 import dataset
import numpy as np
import pandas as pd

choices = ["Small", "Medium", "Large"]

conditions = [
    dataset["total_amount"] < 100,
    (dataset["total_amount"] >= 100) & (dataset["total_amount"] < 500),
    dataset["total_amount"] >= 500
]

dataset["order_size"] = np.select(
    conditions,
    choices,
    default="Unknown"
)

dataset["total_amount"] = dataset["total_amount"].abs()

# dataset.to_csv("/home/inovaqo/Documents/project-pandas-numpy/part3/cleaned_processed.csv")

dataset.to_csv("/home/inovaqo/Documents/project-pandas-numpy/part4/processed.csv", index=False)
