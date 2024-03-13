-- Check if the user user_0d_1 exists
SELECT User, Host FROM mysql.user WHERE User = 'user_0d_1' AND Host = 'localhost';

-- Check the grants for the user user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Check if the user user_0d_2 exists
SELECT User, Host FROM mysql.user WHERE User = 'user_0d_2' AND Host = 'localhost';

-- Check the grants for the user user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
