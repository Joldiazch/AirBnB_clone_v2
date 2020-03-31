-- Script that prepares a MySQL server for the project
-- Creates a new tests user along with its paswword and permissions
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE NEW USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;