import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector
import os

# Setup
os.makedirs("images", exist_ok=True)

# Set seaborn style — makes all charts look clean and professional
sns.set_theme(style="whitegrid")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="airbnb_analytics"
)
cursor = conn.cursor()
print("Connected successfully\n")

# Helper: run query and return as DataFrame 
def fetch(query):
    cursor.execute(query)
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    return pd.DataFrame(rows, columns=columns)


# CHART 1: Average Price by Room Type

df1 = fetch("""
    SELECT room_type,
           ROUND(AVG(price), 2) AS avg_price
    FROM listings
    GROUP BY room_type
    ORDER BY avg_price DESC
""")

plt.figure(figsize=(8, 5))
sns.barplot(data=df1, x="room_type", y="avg_price", palette="Blues_d")
plt.title("Average Price by Room Type", fontsize=14, fontweight="bold")
plt.xlabel("Room Type")
plt.ylabel("Average Price (USD)")
plt.tight_layout()
plt.savefig("images/avg_price_by_room_type.png", dpi=150)
plt.close()
print("Chart 1 saved: avg_price_by_room_type.png")


# CHART 2: Average Price by Neighbourhood Group

df2 = fetch("""
    SELECT neighbourhood_group,
           ROUND(AVG(price), 2) AS avg_price
    FROM listings
    WHERE neighbourhood_group IS NOT NULL
    GROUP BY neighbourhood_group
    ORDER BY avg_price DESC
""")

plt.figure(figsize=(9, 5))
sns.barplot(data=df2, x="neighbourhood_group", y="avg_price", palette="Oranges_d")
plt.title("Average Price by Neighbourhood Group", fontsize=14, fontweight="bold")
plt.xlabel("Neighbourhood Group")
plt.ylabel("Average Price (USD)")
plt.tight_layout()
plt.savefig("images/avg_price_by_neighbourhood.png", dpi=150)
plt.close()
print("Chart 2 saved: avg_price_by_neighbourhood.png")


# CHART 3: Top 10 Neighbourhoods by Listing Count

df3 = fetch("""
    SELECT neighbourhood,
           COUNT(*) AS total_listings
    FROM listings
    GROUP BY neighbourhood
    ORDER BY total_listings DESC
    LIMIT 10
""")

plt.figure(figsize=(10, 6))
sns.barplot(data=df3, x="total_listings", y="neighbourhood", palette="Greens_d")
plt.title("Top 10 Neighbourhoods by Listing Count", fontsize=14, fontweight="bold")
plt.xlabel("Total Listings")
plt.ylabel("Neighbourhood")
plt.tight_layout()
plt.savefig("images/top10_neighbourhoods_listings.png", dpi=150)
plt.close()
print("Chart 3 saved: top10_neighbourhoods_listings.png")


# CHART 4: Top 10 Hosts by Number of Listings

df4 = fetch("""
    SELECT host_name,
           COUNT(*) AS total_listings
    FROM listings
    GROUP BY host_id, host_name
    ORDER BY total_listings DESC
    LIMIT 10
""")

plt.figure(figsize=(10, 6))
sns.barplot(data=df4, x="total_listings", y="host_name", palette="Purples_d")
plt.title("Top 10 Hosts by Number of Listings", fontsize=14, fontweight="bold")
plt.xlabel("Total Listings")
plt.ylabel("Host Name")
plt.tight_layout()
plt.savefig("images/top10_hosts.png", dpi=150)
plt.close()
print("Chart 4 saved: top10_hosts.png")


# CHART 5: Average Availability by Room Type

df5 = fetch("""
    SELECT room_type,
           ROUND(AVG(availability_365), 1) AS avg_days_available
    FROM listings
    GROUP BY room_type
    ORDER BY avg_days_available DESC
""")

plt.figure(figsize=(8, 5))
sns.barplot(data=df5, x="room_type", y="avg_days_available", palette="Reds_d")
plt.title("Average Availability by Room Type (Days/Year)", fontsize=14, fontweight="bold")
plt.xlabel("Room Type")
plt.ylabel("Avg Days Available (out of 365)")
plt.tight_layout()
plt.savefig("images/availability_by_room_type.png", dpi=150)
plt.close()
print("Chart 5 saved: availability_by_room_type.png")

# Cleanup
cursor.close()
conn.close()
print("\nAll charts saved to images/ folder")
print("Connection closed")