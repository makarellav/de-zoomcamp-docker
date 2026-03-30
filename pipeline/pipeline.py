import sys
import pandas as pd

print("hello pipeline")

month = int(sys.argv[1])

print(f"running pipeline for month {month}")
print("arguments", sys.argv)

df = pd.DataFrame({ "day": [1, 2, 3], "num_passengers": [10, 56, 44] })
df['month'] = month

print(df.head())

df.to_parquet(f"output_{month}.parquet")