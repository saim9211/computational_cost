import pandas as pd
from sqlalchemy import create_engine

# Load CSV
engine = create_engine(
    "mysql+pymysql://root:9211@localhost/cloudgpu_advisor"
)

query = """
SELECT *
FROM gpu_daily_prices
"""

df = pd.read_sql(query, engine)

print(df.head())
print(df.shape)

# convert the snapshot_date column to datetime
df["snapshot_date"] = pd.to_datetime(
    df["snapshot_date"]
)
print(df['snapshot_date'].dtypes)

# adding the weeks and the month of the year to the dataset for training the model

df["day_of_week"] = df["snapshot_date"].dt.dayofweek

df["month"] = df["snapshot_date"].dt.month

df["day"] = df["snapshot_date"].dt.day

print(df.head())
print(df.shape)

# save for training the ml modal

df.to_csv(
    "training_dataset.csv",
    index=False
)



df = df.sort_values(
    ["gpu_model", "provider", "snapshot_date"]
)

df["price_lag_1"] = (
    df.groupby(["gpu_model", "provider"])["avg_price"]
      .shift(1)
)

df["price_lag_2"] = (
    df.groupby(["gpu_model", "provider"])["avg_price"]
      .shift(2)
)
df["price_lag_3"] = (
    df.groupby(["gpu_model", "provider"])["avg_price"]
      .shift(3)
)

df.to_csv(
    "gpu_forecasting_dataset.csv",
    index=False
)