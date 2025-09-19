import pandas as pd
import numpy as np

# Define the file path
file_path = 'Data/OLA_DataSet.xlsx'

# Load the dataset
print("Loading the dataset...")
df = pd.read_excel(file_path)
print("Dataset loaded successfully!")

# --- Initial Exploration ---

# 1. Get a summary of the DataFrame (non-null counts, data types)
print("DataFrame Info:")
df.info()

# 2. See the first few rows
print("\nFirst 5 Rows:")
print(df.head())

# 3. Get descriptive statistics for numerical columns
print("\nDescriptive Statistics:")
print(df.describe())

# 4. Check for missing values in each column
print("\nMissing Values Count:")
print(df.isnull().sum())

# 5. List all column names
print("\nColumn Names:")
print(df.columns)


# --- Data Cleaning and Transformation ---

# --- 1. Combine Date and Time into a single datetime column ---
print("\nCombining 'Date' and 'Time' into 'booking_timestamp'...")
# Note: The 'Time' column is of type 'object', but pandas can handle it.
df['booking_timestamp'] = pd.to_datetime(df['Date'].dt.date.astype(str) + ' ' + df['Time'].astype(str))
# Drop the original Date and Time columns
df.drop(['Date', 'Time'], axis=1, inplace=True)
print("Done.")


# --- 2. Handle Missing Values Strategically ---
print("\nHandling missing values...")

# For ratings and TAT, NaN likely means the ride wasn't completed. 
# Filling with 0 is a reasonable choice as it won't affect averages of completed rides.
cols_to_fill_zero = ['V_TAT', 'C_TAT', 'Driver_Ratings', 'Customer_Rating']
df[cols_to_fill_zero] = df[cols_to_fill_zero].fillna(0)
print("Filled ratings, V_TAT, and C_TAT NaNs with 0.")

# For categorical columns, fill with 'Not Applicable'.
df['Payment_Method'].fillna('Not Applicable', inplace=True)
df['Incomplete_Rides_Reason'].fillna('Not Applicable', inplace=True)
print("Filled Payment_Method and Incomplete_Rides_Reason NaNs with 'Not Applicable'.")

# For cancellation columns, NaN means 'Not Canceled'.
df['Canceled_Rides_by_Customer'].fillna('Not Canceled', inplace=True)
df['Canceled_Rides_by_Driver'].fillna('Not Canceled', inplace=True)
print("Filled cancellation NaNs with 'Not Canceled'.")

# The 'Incomplete_Rides' column also seems to indicate a status.
df['Incomplete_Rides'].fillna('Completed or Canceled', inplace=True)
print("Filled Incomplete_Rides NaNs.")


# --- 3. Standardize Text Formats ---
print("\nStandardizing text columns to lowercase...")
df['Vehicle_Type'] = df['Vehicle_Type'].str.lower()
df['Booking_Status'] = df['Booking_Status'].str.lower()
df['Payment_Method'] = df['Payment_Method'].str.lower()
print("Done.")


# --- 4. Reorder Columns for SQL Import ---
print("\nStep 4: Reordering columns for SQL import...")
sql_column_order = [
    'Booking_ID', 'Booking_Status', 'Customer_ID', 'Vehicle_Type', 
    'Pickup_Location', 'Drop_Location', 'V_TAT', 'C_TAT',
    'Canceled_Rides_by_Customer', 'Canceled_Rides_by_Driver',
    'Incomplete_Rides', 'Incomplete_Rides_Reason', 'Booking_Value',
    'Payment_Method', 'Ride_Distance', 'Driver_Ratings', 'Customer_Rating',
    'booking_timestamp', 'Vehicle Images'
]
df = df[sql_column_order]
print("Columns reordered.")


# --- 5. Final Verification ---
print("\n--- Verification ---")
print("Missing values in dataset:", df.isnull().sum().sum())

print("\nCleaned DataFrame Info:")
df.info()


# --- 6. Save the Cleaned Data ---
cleaned_file_path = 'ola_ride_dataset.csv'
print(f"\nSaving cleaned data to '{cleaned_file_path}'...")
df.to_csv(cleaned_file_path, index=False)
print("Cleaned data saved successfully!")