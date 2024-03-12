-- Ensure creation of a table in the current database if it doesn't exist
-- SQL command to create a table named 'first_table' in the current database of your MySQL server
CREATE TABLE IF NOT EXISTS first_table (
id INT,
name VARCHAR(256));
