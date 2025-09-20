-- Q1:- All successful bookings
SELECT 
	Booking_ID,
    Customer_ID,
	Vehicle_Type,
    Pickup_Location,
    Drop_Location,
    booking_timestamp,
    Ride_Distance
FROM 
	ola_rides
WHERE 
	Booking_Status = 'success';


-- Q2:- Average ride distance by vehicle type:
SELECT
    Vehicle_Type,
    AVG(Ride_Distance) AS average_distance_km
FROM
    ola_rides
WHERE
    Booking_Status = 'success'
GROUP BY
    Vehicle_Type
ORDER BY
    average_distance_km DESC;
  
  
-- Q3:- Total rides canceled by customers
SELECT
    COUNT(*) AS total_cancellations_by_customer
FROM
    ola_rides
WHERE
    Canceled_Rides_by_Customer != 'Not Canceled';


-- Q4:- Top 5 customers by highest number of rides
SELECT
    Customer_ID,
    COUNT(Booking_ID) AS total_rides_booked
FROM
    ola_rides
GROUP BY
    Customer_ID
ORDER BY
    total_rides_booked DESC
LIMIT 5;


-- Q5:- Total cancellations by driver for personal & car-related issue
SELECT
    COUNT(*) AS total_cancellations
FROM
    ola_rides
WHERE
    Canceled_Rides_by_Driver = 'Personal & Car related issue';
 
 
-- Q6:- Maximum and minimum driver ratings for Prime Sedan bookings
SELECT
    MAX(Driver_Ratings) AS max_driver_rating,
    MIN(Driver_Ratings) AS min_driver_rating
FROM
    ola_rides
WHERE
    Vehicle_Type = 'prime sedan'
    AND Booking_Status = 'success';


-- Q7:- All rides where payment was made using UPI
SELECT 
	Booking_ID,
    Customer_ID,
	Vehicle_Type,
    booking_timestamp,
    CONCAT('₹', FORMAT(Booking_Value, 0)) AS Booking_Value,
    Payment_Method,
    Ride_Distance
FROM 
	ola_rides
WHERE 
	Payment_Method = 'upi';


-- Q8:- Average customer rating per vehicle type
SELECT
    Vehicle_Type,
    AVG(Customer_Rating) AS average_customer_rating,
    COUNT(*) AS total_rated_rides
FROM
    ola_rides
WHERE
    Booking_Status = 'success'
    AND Customer_Rating > 0
GROUP BY
    Vehicle_Type
ORDER BY
    average_customer_rating DESC;


-- Q9:- Total booking value
SELECT
    CONCAT('₹', FORMAT(SUM(Booking_Value), 0)) AS total_booking_value,
    COUNT(*) AS total_successful_rides,
    CONCAT('₹', FORMAT(AVG(Booking_Value), 2)) AS average_booking_value
FROM
    ola_rides
WHERE
    Booking_Status = 'success';


-- Q10:- List all incomplete rides along with their reasons
SELECT
    Booking_ID,
    Booking_Status,
    Customer_ID,
    Vehicle_Type,
    Pickup_Location,
    Drop_Location,
    Incomplete_Rides_Reason
FROM
    ola_rides
WHERE
    Incomplete_Rides != 'Completed or Canceled'
    AND Incomplete_Rides_Reason != 'Not Applicable'
ORDER BY
    Booking_ID;



