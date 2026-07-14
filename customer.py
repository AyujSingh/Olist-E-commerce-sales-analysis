import pandas as pd

df=pd.read_csv('olist_customers_dataset.csv')
print(df.head())


df.rename(columns={'customer_zip_code_prefix': 'customer_zip_code'}, inplace=True)
df["customer_zip_code"] = df["customer_zip_code"].astype(str).str.zfill(5)
print(df.info())


print(df['customer_id'].nunique())
print(df['customer_unique_id'].nunique())


print(df['customer_zip_code'].head())


from sqlalchemy import create_engine
from sqlalchemy.engine import URL

url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="Ayujs2712@",
    host="localhost",
    port=3306,
    database="analysis"
)

engine = create_engine(url)


from sqlalchemy import text

with engine.connect() as connection:
    result = connection.execute(text("SELECT 1"))
    print(result.fetchone())
df.to_sql(
    "customers",
    con=engine,
    if_exists="replace",
    index=False
)

print("Customers table uploaded successfully")