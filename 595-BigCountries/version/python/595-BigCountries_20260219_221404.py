# Last updated: 2/19/2026, 10:14:04 PM
1import pandas as pd
2
3def big_countries(world: pd.DataFrame) -> pd.DataFrame:
4    
5    big_countries=world[
6        (world['area']>=3000000) |
7        (world['population']>=25000000)
8    ]
9
10    return big_countries[['name','population','area']]