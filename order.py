import pandas as pd
df=pd.read_csv('olist_orders_dataset.csv')
print(df.head())
print(df.info())
date_columns = [
    'order_purchase_timestamp',
    'order_approved_at',
    'order_delivered_carrier_date',
    'order_delivered_customer_date',
    'order_estimated_delivery_date'
]

for col in date_columns:
    df[col] = pd.to_datetime(df[col])
print(df.info())

print(df["order_id"].nunique())
print(df["customer_id"].nunique())
print(df["order_status"].nunique())
print(
    df[
        (df['order_status'] == 'delivered') &
        (df['order_delivered_customer_date'].isna())
    ]
)


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
    "orders",
    con=engine,
    if_exists="replace",
    index=False
)

print("Customers table uploaded successfully")

