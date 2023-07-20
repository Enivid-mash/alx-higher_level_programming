-- Create the database hbtn_0d_usa if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to using the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create the table cities in the hbtn_0d_usa database
-- The table has an auto-incrementing primary key (id), a foreign key (state_id) referencing the states table,
-- and non-null name and state_id columns
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states (id)
);
