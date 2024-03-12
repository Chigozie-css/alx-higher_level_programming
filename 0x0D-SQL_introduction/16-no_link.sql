-- List all records of a table with a non-null name value
-- SQL query to list all records of the table 'second_table' where the name value is not null, ordered by score descending
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
