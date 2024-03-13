-- Check if the user exists
SELECT User, Host FROM mysql.user WHERE User = 'user_0d_1' AND Host = 'localhost';

-- Check the grants for the user
SHOW GRANTS FOR 'user_0d_1'@'localhost';
