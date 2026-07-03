import pandas as pd
import numpy as np
df = pd.read_csv("cleaned_processed.csv")


df.head(10)

def outlier_detection_and_flag(dataset: pd.DataFrame):
    dataset["mean_unit_price"] = dataset.groupby("product_category")["unit_price"].transform("mean")
    dataset["std_unit_price"] = dataset.groupby("product_category")["unit_price"].transform("std")
    dataset["z_score"] = np.where(
    dataset["std_unit_price"] > 0,
    (dataset["unit_price"] - dataset["mean_unit_price"]) / dataset["std_unit_price"],
    0
)
    # Flag outliers (|z| > 3)
    dataset["is_outlier"] = np.abs(dataset["z_score"]) > 3
    #negative price is invalid so we flag
    dataset["negative_unit_price"] = dataset["unit_price"] < 0
    #flag z score invalid values also
    dataset["negative_z_score"] = dataset["z_score"] 
    #see suspicious row in rows
    dataset["needs_review"] = (
    (dataset["unit_price"] < 0) |
    (np.abs(dataset["z_score"]) > 3)
)

outlier_detection_and_flag(df)

print(df.head(10))



