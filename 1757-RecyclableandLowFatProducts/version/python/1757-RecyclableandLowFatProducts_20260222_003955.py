# Last updated: 2/22/2026, 12:39:55 AM
1import pandas as pd
2
3def find_products(products: pd.DataFrame) -> pd.DataFrame:
4    
5    res=products.loc[
6        (products['low_fats']=='Y') & (products['recyclable']=='Y'),["product_id"]
7    ]
8
9    return res