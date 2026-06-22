import pandas as pd
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="airbnb_analytics"
)
cursor = conn.cursor()
print("Connected successfully\n")

# Helper: run a query and print results neatly 
def run_query(title, query):
    print("=" * 55)
    print(f"  {title}")
    print("=" * 55)
    cursor.execute(query)
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=columns)
    print(df.to_string(index=False))
    print()

# Run all analyses 

run_query(
    "Q1: Average Price by Room Type",
    """
    SELECT room_type,
           ROUND(AVG(price), 2) AS avg_price,
           COUNT(*) AS total_listings
    FROM listings
    GROUP BY room_type
    ORDER BY avg_price DESC
    """
)

run_query(
    "Q2: Average Price by Neighbourhood Group",
    """
    SELECT neighbourhood_group,
           ROUND(AVG(price), 2) AS avg_price,
           COUNT(*) AS total_listings
    FROM listings
    GROUP BY neighbourhood_group
    ORDER BY avg_price DESC
    """
)

run_query(
    "Q3: Top 10 Most Expensive Neighbourhoods",
    """
    SELECT neighbourhood,
           neighbourhood_group,
           ROUND(AVG(price), 2) AS avg_price,
           COUNT(*) AS total_listings
    FROM listings
    GROUP BY neighbourhood, neighbourhood_group
    ORDER BY avg_price DESC
    LIMIT 10
    """
)

run_query(
    "Q4: Top 10 Neighbourhoods by Listing Count",
    """
    SELECT neighbourhood,
           neighbourhood_group,
           COUNT(*) AS total_listings
    FROM listings
    GROUP BY neighbourhood, neighbourhood_group
    ORDER BY total_listings DESC
    LIMIT 10
    """
)

run_query(
    "Q5: Top 10 Hosts by Number of Listings",
    """
    SELECT host_id,
           host_name,
           COUNT(*) AS total_listings
    FROM listings
    GROUP BY host_id, host_name
    ORDER BY total_listings DESC
    LIMIT 10
    """
)

run_query(
    "Q6: Top 10 Most Reviewed Hosts",
    """
    SELECT host_id,
           host_name,
           SUM(number_of_reviews) AS total_reviews,
           COUNT(*) AS total_listings
    FROM listings
    GROUP BY host_id, host_name
    ORDER BY total_reviews DESC
    LIMIT 10
    """
)

run_query(
    "Q7: Average Availability by Room Type",
    """
    SELECT room_type,
           ROUND(AVG(availability_365), 1) AS avg_days_available
    FROM listings
    GROUP BY room_type
    ORDER BY avg_days_available DESC
    """
)

run_query(
    "Q8: Fully Booked Listings (0 days available)",
    """
    SELECT COUNT(*) AS fully_booked_listings
    FROM listings
    WHERE availability_365 = 0
    """
)

run_query(
    "Q9: Always Available Listings (365 days)",
    """
    SELECT COUNT(*) AS always_available_listings
    FROM listings
    WHERE availability_365 = 365
    """
)

#  Cleanup 
cursor.close()
conn.close()
print("Connection closed")