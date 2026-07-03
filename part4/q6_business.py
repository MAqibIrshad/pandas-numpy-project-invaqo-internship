#Is there a month-over-month sales trend across Jan–Jun 2025? (You’ll need .dt.month or .dt.to_period('M') on your cleaned date column.
from q5_business import dataset
import pandas as pd
print(dataset["order_date"].dtype)
dataset["order_date"] = pd.to_datetime(dataset["order_date"])
dataset["month"] = dataset["order_date"].dt.to_period("M")

monthly_sales = dataset.groupby("month")["total_amount"].sum().sort_index()

print(monthly_sales)

mom_change = monthly_sales.pct_change() * 100
print(mom_change)

trend = pd.DataFrame({
    "monthlysales": monthly_sales,
    "month-over-month change": mom_change
})

print(trend)
