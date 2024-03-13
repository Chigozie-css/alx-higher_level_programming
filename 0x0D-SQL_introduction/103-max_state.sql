-- Ensure retrieval of the maximum temperature of each state
-- SQL query to display the maximum temperature of each state, ordered by state name, limited to the top 3 states
SELECT state, MAX(value) as max_temp FROM temperatures
	GROUP BY state
	ORDER BY state
	LIMIT 3;
