from to_numeric import dataset
import pandas as pd
print(dataset["product_category"].head(20))

mapping = {
    "home & kitchen": "Home & Kitchen",
    "home&kitchen":"Home & Kitchen",
    "sports & outdoors": "Sports & Outdoors",
    "sports&outdoors": "Sports & Outdoors",
    "sports and outdoors": "Sports & Outdoors"
}

dataset["product_category"] = dataset["product_category"].replace(mapping)
print(dataset.head(10))

dataset.to_csv("cleaned_processed")

