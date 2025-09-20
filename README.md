# 🚗 Ola Ride Insights Dashboard

[![Ola Ride](https://img.shields.io/badge/Ola%20Ride-Analytics-green?logo=car&logoColor=white)](https://book.olacabs.com/)
[![MySQL](https://img.shields.io/badge/MySQL-Database-orange?logo=mysql)](https://www.mysql.com/)
[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)](https://streamlit.io/)
[![Power BI](https://img.shields.io/badge/PowerBI-Visualization-yellow?logo=powerbi)](https://powerbi.microsoft.com/)
[![VS Code](https://img.shields.io/badge/VSCode-Editor-0078d7?logo=visualstudiocode&logoColor=white)](https://code.visualstudio.com/)
[![pandas](https://img.shields.io/badge/pandas-Data%20Analysis-blue?logo=pandas)](https://pandas.pydata.org/)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📑 Table of Contents

- 📌 [Overview](#-overview)
- 🔍 [Features](#-features)
- 🗄 [Database Schema](#-database-schema)
- 🚀 [Tech Stack](#-tech-stack)
- 🏗 [Project Structure](#-project-structure)

---

## 📌 Overview

Ola Ride Insights Dashboard is a comprehensive data analytics platform designed to provide deep insights into ride booking patterns, customer behavior and vehicle usage for the Ola ride service. The dashboard combines SQL-based data analysis with Power BI visualizations (placeholders) to enable intuitive exploration of ride data.

---

## 🔍 Features

- Embedded sections for Power BI dashboard visualization
- Interactive dashboard with SQL-driven data exploration
- Powerful SQL Analysis page with predefined queries
- Dynamic query loading from a GitHub repository for flexibility

---

## 🗄 Database Schema

- Database: `ola_ride_db`
- Table: `ola_rides` with key fields:
  - `Booking_ID` (Primary Key)
  - `Customer_ID`
  - `Vehicle_Type`
  - `Pickup_Location`, `Drop_Location`
  - `booking_timestamp`
  - `Booking_Value`
  - `Payment_Method`
  - Additional fields including ride status, ratings and cancellation reasons
- Includes indexes on frequently queried columns for optimized performance

Refer to the `schema.sql` file for complete schema and data loading instructions.

---

## 🚀 Tech Stack

- **Python** → Data processing.
- **Streamlit** → Interactive dashboard.
- **MySQL** → Database storage & SQL analytics.
- **pandas** → Data manipulation.
- **Requests** → GitHub integration to load SQL queries dynamically

---

## 🏗 Project Structure

```
📦 Ola_Ride_Dashboard
┣ 📂.streamlit
┃ ┗ 📜 config.toml
┣ 📂Data
┃ ┗ 📜 OLA_DataSet.xlsx
┣ 📜 ola_dashboard_app.py
┣ 📜 process_data.py
┣ 📜 queries.sql
┣ 📜 requirements.txt
┗ 📜 README.md
```

---

## 👨‍💻 Author

**Neeraj Kumar**

---
