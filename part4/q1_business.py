#What are total sales (total_amount) by product_category? Which category is the top performer?

import pandas as pd

dataset = pd.read_csv("cleaned_processed.csv")

category_total_sales = dataset.groupby("product_category")["total_amount"].sum()

print(category_total_sales)

top_performer_category = category_total_sales.idxmax()
print(top_performer_category)

top_value = category_total_sales.max()
print(top_value)



