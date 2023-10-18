mysql -uroot -p
-- Use the information_schema database
USE information_schema;

-- List all privileges of user_0d_1 on localhost
SELECT * FROM user_privileges WHERE grantee = "'user_0d_1'@'localhost'";

-- List all privileges of user_0d_2 on localhost
SELECT * FROM user_privileges WHERE grantee = "'user_0d_2'@'localhost'";
