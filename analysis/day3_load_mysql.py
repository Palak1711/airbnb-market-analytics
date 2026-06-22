import math
import pandas as pd
import mysql.connector

# Load cleaned dataset
df = pd.read_csv("data/listings_clean_utf8.csv")
print("Loaded:", df.shape)

#Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="airbnb_analytics"
)
cursor = conn.cursor()
print("Connected successfully")

# Clear table before reload (safe to rerun script)
cursor.execute("TRUNCATE TABLE listings")

#  Insert data 
insert_query = """
INSERT INTO listings (
    id, name, host_id, host_name, neighbourhood_group,
    neighbourhood, room_type, price, minimum_nights,
    number_of_reviews, availability_365
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

def clean_value(v):
    """Convert NaN / missing values into proper SQL NULL (None)."""
    if v is None:
        return None
    if isinstance(v, float) and math.isnan(v):
        return None
    return v

data = [tuple(clean_value(v) for v in row) for row in df.to_numpy()]

cursor.executemany(insert_query, data)
conn.commit()
print(f"{cursor.rowcount} rows inserted")

#  Verify 
cursor.execute("SELECT COUNT(*) FROM listings")
print("Row count in MySQL:", cursor.fetchone()[0])

cursor.execute("SELECT * FROM listings LIMIT 5")
for row in cursor.fetchall():
    print(row)

# Cleanup
cursor.close()
conn.close()
print("Connection closed")