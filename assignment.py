# ============================================================
# PYTHON PROGRAM
# 1. Explore Regex Patterns
# 2. Explore Datetime Functions in Pandas
# 3. Import CSV, Perform Data Cleaning & Data Analysis
# ============================================================

import re
import pandas as pd

# ============================================================
# PART 1 : REGEX PATTERNS
# ============================================================

print("========== REGEX EXAMPLES ==========\n")

# Email Validation
email = "student123@gmail.com"
email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

if re.match(email_pattern, email):
    print("Valid Email:", email)
else:
    print("Invalid Email")

# Mobile Number Validation (Indian)
mobile = "9876543210"
mobile_pattern = r'^[6-9]\d{9}$'

if re.match(mobile_pattern, mobile):
    print("Valid Mobile Number:", mobile)
else:
    print("Invalid Mobile Number")

# Alphabetic String Validation
name = "Python"
string_pattern = r'^[A-Za-z]+$'

if re.match(string_pattern, name):
    print("Valid String:", name)
else:
    print("Invalid String")

# Password Validation
password = "Python@123"
password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'

if re.match(password_pattern, password):
    print("Strong Password")
else:
    print("Weak Password")

# Extract Numbers
text = "Python version 3 released in 2008."
numbers = re.findall(r'\d+', text)
print("Numbers Found:", numbers)

# Extract Words Starting with P
sentence = "Python Pandas Programming Practice"
words = re.findall(r'\bP\w+', sentence)
print("Words Starting with P:", words)


# ============================================================
# PART 2 : DATETIME FUNCTIONS IN PANDAS
# ============================================================

print("\n========== DATETIME FUNCTIONS ==========\n")

date_data = {
    'Date': ['2025-01-10', '2025-03-15', '2025-06-20']
}

date_df = pd.DataFrame(date_data)

# Convert to datetime
date_df['Date'] = pd.to_datetime(date_df['Date'])

# Extract datetime information
date_df['Year'] = date_df['Date'].dt.year
date_df['Month'] = date_df['Date'].dt.month
date_df['Month_Name'] = date_df['Date'].dt.month_name()
date_df['Day'] = date_df['Date'].dt.day
date_df['Day_Name'] = date_df['Date'].dt.day_name()
date_df['Weekday'] = date_df['Date'].dt.weekday
date_df['Leap_Year'] = date_df['Date'].dt.is_leap_year

print(date_df)

# Current Date and Time
current_time = pd.Timestamp.now()
print("\nCurrent Date & Time:")
print(current_time)

# Date Difference
date1 = pd.Timestamp("2025-01-01")
date2 = pd.Timestamp("2025-06-01")

difference = date2 - date1
print("\nDifference Between Dates:")
print(difference)

# Add Days
future_date = date1 + pd.Timedelta(days=30)
print("\nDate After 30 Days:")
print(future_date)


# ============================================================
# PART 3 : CSV DATA CLEANING & ANALYSIS
# ============================================================

print("\n========== CSV DATA ANALYSIS ==========\n")

# Create a sample CSV file
student_data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Rohan", "Priya"],
    "Age": [20, 21, None, 22, 20, 21],
    "Marks": [85, 90, 75, None, 88, 90],
    "City": ["Delhi", "Mumbai", "Pune", "Delhi", "Mumbai", "Mumbai"]
}

sample_df = pd.DataFrame(student_data)

# Save CSV
sample_df.to_csv("students.csv", index=False)

# Read CSV
df = pd.read_csv("students.csv")

print("Original Data:\n")
print(df)

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill Missing Values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Remove Duplicate Rows
df = df.drop_duplicates()

print("\nCleaned Data:\n")
print(df)

# ---------------- Data Analysis ----------------

print("\nAverage Marks:", df["Marks"].mean())
print("Maximum Marks:", df["Marks"].max())
print("Minimum Marks:", df["Marks"].min())

# Top Student
print("\nTop Student:")
print(df[df["Marks"] == df["Marks"].max()])

# Students by City
print("\nStudents in Each City:")
print(df["City"].value_counts())

# Age Statistics
print("\nAge Statistics:")
print(df["Age"].describe())

# Sort Students by Marks
print("\nStudents Sorted by Marks:")
print(df.sort_values(by="Marks", ascending=False))

print("\n========== PROGRAM COMPLETED SUCCESSFULLY ==========")