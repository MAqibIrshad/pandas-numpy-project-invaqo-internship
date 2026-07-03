from outlier_flag01 import df
import pandas as pd
import numpy as np

def outlier_discount_price_transform(ds: pd.DataFrame):
    # Mean and std per product category
    ds["discount_mean_percent"] = (
        ds.groupby("product_category")["discount_percent"]
          .transform("mean")
    )

    ds["discount_std_percent"] = (
        ds.groupby("product_category")["discount_percent"]
          .transform("std")
    )

    # rows with invalid prices
    mask = (
        (ds["discount_percent"] < 0) |
        (ds["discount_percent"] > 100)
    )

    # initialize z score
    ds["z_score_discount_percent"] = 0.0

    # compute z score only for masked rows when true
    ds.loc[mask, "z_score_discount_percent"] = (
        (ds.loc[mask, "discount_percent"] -
         ds.loc[mask, "discount_mean_percent"])
        /
        ds.loc[mask, "discount_std_percent"]
    )

    # flag outliers
    ds["disc_percent_is_outlier"] = (
        ds["z_score_discount_percent"].abs() > 3
    )

    #needs_review suspicious values
    ds["disc_percent_needs_review"] = (
        (ds["discount_percent"] < 0) |
        (ds["z_score_discount_percent"].abs() > 3)
    )

    return ds

dataset = outlier_discount_price_transform(df)