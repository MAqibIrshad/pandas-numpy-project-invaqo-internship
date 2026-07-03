
ISSUE_1="Removing Null Values"
columns_affected = customer_email, quantity, unit_price, discount_percent, shipping cost, region and payment_method

ISSUE_2="Categorical/Textual instance standarization"
customer_name, product_name, product_category, region, payment_method

ISSUE_3="Data with Datatype inconsistency (like numeric columns having str values):
quantity

ISSUE_4="Dropping Duplicates"
from whole dataset

ISSUE_5="Dtype Error handling (using to_numeric)"
order_id, quantity, unit_price, discount_percent, shipping_cost

ISSUE_6="Categorical String Mappiny (using replace function)"
on product_category

ISSUE_7="Diverse Date patterns in one column using str to datetime function"
order_date

ISSUE_8="Outlier detection and flagging"
on unit price and discount price using z score
also use np.where and boolean masking both for unit_price and discount_percent's outliers

ISSUE_9="A need of column total amount using formula: quantity × unit_price × (1 − discount_percent/100) + shipping_cost"
Using Vectorization

ISSUE_10="Order Size"
used conditioning using np.where wot get order_size (small, medium and large) using total_amount column


QUERY:1
I found which category of products is the top performer. I also use groupby to get total sales per category
                (groupby with product_category considering total_amount and idxmax function)
QUERY:2
I also found orders per region
            (groupby with region considering order_id with count function)
QUERY:3
I also make query for getting most common payment method and also the variation of this payment method accross regions
            (np.argmax, groupby with region considering payment_method, apply and mode functions)
QUERY:4
I also found percentage of orders returned/cancelled
            (make another column is_bad_order applying isin() with list ["returned", "cancelled"] on order_status)
QUERY:5
I also found top 5 products with respect to revenue
            (groupby with product name considering total_amount, sum and sort_values functions)
QUERY:6
I also find month over month change of month with previous (percentage)
            (groupby month considering "total_amount", sum and sort_index functions)
            (also used pct_change function to check change of revenue percentage over months )