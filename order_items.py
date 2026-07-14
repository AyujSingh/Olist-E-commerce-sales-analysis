import pandas as pd
df=pd.read_csv('olist_order_items_dataset.csv')
print(df.head())
print(df.info())
df['shipping_limit_date'] = pd.to_datetime(df['shipping_limit_date'])
print(df.info())

print("Unique order IDs:", df['order_id'].nunique())
print("Unique product IDs:", df['product_id'].nunique())
print("Unique seller IDs:", df['seller_id'].nunique())

print("Missing values:")
print(df.isnull().sum())

print("Duplicate rows:", df.duplicated().sum())
print("Total rows:", len(df))
print(df.duplicated(subset=['order_id', 'order_item_id']).sum())


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
    "order_items",
    con=engine,
    if_exists="replace",
    index=False
)

print("Customers table uploaded successfully")