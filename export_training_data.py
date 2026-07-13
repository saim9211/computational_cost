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

# save for training the ml modal
print(df.shape)

df.to_csv(
    "training_dataset.csv",
    index=False
)

