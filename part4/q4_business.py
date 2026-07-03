
#What percentage of orders are Returned or Cancelled? Does that rate differ meaningfully by category?

from q3_business import dataset

# def percentage_of_orders_returned_cancelled(dataset):
#     trues = 0
#     falses = 0
#     dataset["is_bad_order"] = dataset["order_status"].isin(["returned", "cancelled"])
#     is_bad_order = dataset["is_bad_order"]
#     for value in is_bad_order:
#         if value:
#             trues = trues+1
#         else:
#             falses = falses+1
#     return trues/dataset["is_bad_order"].size() * 100

    

# print(percentage_of_orders_returned_cancelled(dataset))


def percentage_of_orders_returned_cancelled(dataset):
    dataset["is_bad_order"] = dataset["order_status"].str.lower().isin(["returned", "cancelled"])
    
    return dataset["is_bad_order"].mean() * 100

print(percentage_of_orders_returned_cancelled(dataset))