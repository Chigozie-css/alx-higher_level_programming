-- Create the temperatures table if it doesn't exist
CREATE TABLE IF NOT EXISTS temperatures (
    city VARCHAR(255),
    value FLOAT
);

-- Insert data into the temperatures table
INSERT INTO temperatures (city, value) VALUES
    ('New York', 75.5),
    ('Los Angeles', 80.2),
    ('Chicago', 68.9),
    -- Add more data as needed
    ;
