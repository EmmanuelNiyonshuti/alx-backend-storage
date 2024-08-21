-- 0 create a table users with id(pk), email and name attributes.
-- can be executed on the current database context.

-- CREATE DATABASE IF NOT EXISTS holberton;
-- USE holberton;
CREATE TABLE IF NOT EXISTS users(
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY (id)
);
