import pandas as pd
from sqlalchemy import create_engine

# Load CSV in to sql database
df = pd.read_csv("combined_gpu_data_unfiltered.csv")


# MySQL Connection
engine = create_engine(
    
    "mysql+pymysql://root:9211@localhost/cloudgpu_advisor"
)
# convert the last_updated column to datetime
df["last_updated"] = pd.to_datetime(
    df["last_updated"],
    utc=True,
    errors="coerce"
)

df["last_updated"] = df["last_updated"].dt.tz_localize(None)

df["extracted_at"] = pd.to_datetime(
    df["extracted_at"],
    format="%Y%m%d_%H%M%S",
    errors="coerce"
)
# import the data into the database

try:
    df.to_sql(
    "gpu_pricing_history",
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=1000
)

    print("Import completed")

except Exception as e:
    import traceback
    traceback.print_exc()

print(f"{len(df)} rows inserted")


