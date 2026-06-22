import pandas as pd
df=pd.read_excel("data/listings.xlsx")
df = df[
[
'id',
'name',
'host_id',
'host_name',
'neighbourhood_group',
'neighbourhood',
'room_type',
'price',
'minimum_nights',
'number_of_reviews',
'availability_365'
]
]
print(df.shape)
print(df.isnull().sum())
df = df.dropna(
subset=['price','neighbourhood']
)
print(df.shape)
print(df.head())
print(df.info())
df.to_csv(
    "data/listings_clean.csv",
    index=False
)

print("Cleaning completed")
df.to_csv(
    "data/listings_clean_utf8.csv",
    index=False,
    encoding="utf-8-sig"
)