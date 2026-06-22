
USE airbnb_analytics;


-- ANALYSIS: PRICING TRENDS


-- Q1: Average price by room type
SELECT
    room_type,
    ROUND(AVG(price), 2) AS avg_price,
    COUNT(*) AS total_listings
FROM listings
GROUP BY room_type
ORDER BY avg_price DESC;

-- Q2: Average price by neighbourhood group (borough)
SELECT
    neighbourhood_group,
    ROUND(AVG(price), 2) AS avg_price,
    COUNT(*) AS total_listings
FROM listings
GROUP BY neighbourhood_group
ORDER BY avg_price DESC;


-- ANALYSIS: NEIGHBOURHOOD PEROFORMANCE


-- Q3: Top 10 most expensive neighbourhoods (avg price)
SELECT
    neighbourhood,
    neighbourhood_group,
    ROUND(AVG(price), 2) AS avg_price,
    COUNT(*) AS total_listings
FROM listings
GROUP BY neighbourhood, neighbourhood_group
ORDER BY avg_price DESC
LIMIT 10;

-- Q4: Top 10 neighbourhoods with most listings
SELECT
    neighbourhood,
    neighbourhood_group,
    COUNT(*) AS total_listings
FROM listings
GROUP BY neighbourhood, neighbourhood_group
ORDER BY total_listings DESC
LIMIT 10;


-- ANALYSIS: HOST ANALYSIS


-- Q5: Top 10 hosts with most listings
SELECT
    host_id,
    host_name,
    COUNT(*) AS total_listings
FROM listings
GROUP BY host_id, host_name
ORDER BY total_listings DESC
LIMIT 10;

-- Q6: Top 10 most reviewed hosts (total reviews across all listings)
SELECT
    host_id,
    host_name,
    SUM(number_of_reviews) AS total_reviews,
    COUNT(*) AS total_listings
FROM listings
GROUP BY host_id, host_name
ORDER BY total_reviews DESC
LIMIT 10;


-- ANALYSIS: AVAILABILITY PATTERNS


-- Q7: Average availability by room type
SELECT
    room_type,
    ROUND(AVG(availability_365), 1) AS avg_days_available
FROM listings
GROUP BY room_type
ORDER BY avg_days_available DESC;

-- Q8: Listings with 0 availability (fully booked all year)
SELECT
    COUNT(*) AS fully_booked_listings
FROM listings
WHERE availability_365 = 0;

-- Q9: Listings available all year (365 days)
SELECT
    COUNT(*) AS always_available_listings
FROM listings
WHERE availability_365 = 365;