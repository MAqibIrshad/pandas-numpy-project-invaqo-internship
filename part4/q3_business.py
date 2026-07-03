#Which payment_method is most common, and does it vary by region? (pivot_table or groupby with two keys)

import pandas as pd
import numpy as np
from q2_business import dataset

def most_common_payment_method_query(dataset:pd.DataFrame):
    credit_card = 0
    debit_card = 0
    cash_on_delivery = 0
    paypal= 0
    jazz_cash = 0

    # dataset["payment_method"].unique()
    payment_methods = dataset["payment_method"]
    for payment in payment_methods:
        if payment.lower() == "credit card":
            credit_card =  credit_card+1
        elif payment.lower() == "debit card":
            debit_card = debit_card + 1
        elif payment.lower() == "paypal":
            paypal = paypal + 1
        elif payment.lower() == "jazzcash":
            jazz_cash = jazz_cash+1
        elif payment.lower() == "cash on delivery":
            cash_on_delivery = cash_on_delivery+1
        else:
            print("No Way")

    methods = [
        "credit card",
        "debit card",
        "paypal",
        "jazz cash",
        "cash on delivery"
    ]

    counts = [
        credit_card,
        debit_card,
        paypal,
        jazz_cash,
        cash_on_delivery
    ]

    return methods[np.argmax(counts)]



print(most_common_payment_method_query(dataset))

def variation_of_common_payment_method_by_region(dataset: pd.DataFrame):
    return (
        dataset.groupby("region")["payment_method"]
        .apply(lambda x: x.mode()[0])
    )


variation_by_region = variation_of_common_payment_method_by_region(dataset)

print(variation_by_region)