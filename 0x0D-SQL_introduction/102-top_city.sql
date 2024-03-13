-- Ensure retrieval of the average temperature by city for specific months
-- SQL query to display the average temperature by city for months 7 and 8, ordered by temperature, limited to the top 3 cities
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
