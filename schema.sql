-- Create the database ola_rides_db
CREATE DATABASE IF NOT EXISTS ola_ride_db;
USE ola_ride_db;


-- Create the table ola_rides
CREATE TABLE IF NOT EXISTS ola_rides (
    Booking_ID VARCHAR(255) PRIMARY KEY,
    Booking_Status VARCHAR(50),
    Customer_ID VARCHAR(255),
    Vehicle_Type VARCHAR(50),
    Pickup_Location VARCHAR(255),
    Drop_Location VARCHAR(255),
    V_TAT FLOAT,
    C_TAT FLOAT,
    Canceled_Rides_by_Customer VARCHAR(255),
    Canceled_Rides_by_Driver VARCHAR(255),
    Incomplete_Rides VARCHAR(255),
    Incomplete_Rides_Reason VARCHAR(255),
    Booking_Value INT,
    Payment_Method VARCHAR(50),
    Ride_Distance INT,
    Driver_Ratings FLOAT,
    Customer_Rating FLOAT,
    booking_timestamp DATETIME,
    Vehicle_Images TEXT
);

-- Load data into table
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/ola_ride_dataset.csv'
INTO TABLE ola_rides
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

-- Verify loaded data
SELECT * FROM ola_rides LIMIT 5;
