import pandas as pd
import numpy as np
import re
dataset = pd.read_csv("messy_orders.csv")
print(dataset.head(10))
print(dataset.info())
print(dataset.describe())

print(dataset.isna().sum())