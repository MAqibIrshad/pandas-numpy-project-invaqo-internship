I see null values in customer_email, quantity, unit_price, discount_percent, shipping cost, region and payment_method
I fill null values one by one 
I see mixture (lower and uppercase) of categorical or textual instances so for the sake of standardization i apply on each column lambda function to stay coherent inherently
I also see some mishaps regarded to data consistency in numeric columns; having string sequences like in quantity and unit price
I also see some duplicates in data and i drop all of them as per requirement
I also add dtype error handling feature for each numeric column
I also provide categorical string mappings to the replace function
I also see 5 kinds of date patterns in column "order_date" so i compare each value of order_date with 5 patterns and return when pattern matches
