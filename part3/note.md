
I find outlier from unit_price and discount percent and also flag them
I used np.where and also boolean masking to find and flag outliers of both columns
I also derived a new column called total amount using vectorization...I used this formula (quantity × unit_price × (1 − discount_percent/100) + shipping_cost)
I also use conditioning in np.where to get order_size (small, medium and large) using total_amount
