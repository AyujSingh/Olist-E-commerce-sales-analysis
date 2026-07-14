import pandas as pd
df=pd.read_csv('olist_products_dataset.csv')
print(df.head())
print(df.info())
print("Unique product IDs:", df['product_id'].nunique())
print("Total rows:", len(df))
print("Missing values:")
print(df.isnull().sum())
missing_610 = df[
    df['product_category_name'].isna()
]

print(missing_610[
    [
        'product_category_name',
        'product_name_lenght',
        'product_description_lenght',
        'product_photos_qty'
    ]
].isna().sum())
df.rename(columns={'product_name_lenght': 'product_name_length', 'product_description_lenght': 'product_description_length'}, inplace=True)
df["product_category_name"]= df["product_category_name"].fillna("unknown")
print(df.duplicated().sum())


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
    "products",
    con=engine,
    if_exists="replace",
    index=False
)

print("Customers table uploaded successfully")