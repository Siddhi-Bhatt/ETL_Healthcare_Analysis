import pandas as pd
import sqlite3
import os

# Paths
clean_csv_path = "../clean_data/healthcare_admissions_clean.csv"
db_path = "../etl_healthcare.db"  # SQLite database file

# Load cleaned CSV
df = pd.read_csv(clean_csv_path)

# Connect to SQLite database (creates it if not exists)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS healthcare_admissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age INTEGER,
    gender INTEGER,
    blood_type INTEGER,
    medical_condition INTEGER,
    billing_amount REAL,
    admission_type INTEGER,
    medication INTEGER,
    test_results INTEGER
)
""")

# Load data into SQL
df.to_sql('healthcare_admissions', conn, if_exists='replace', index=False)

print(f"✅ Data loaded into SQL database: {db_path}")

# Optional: check first 5 rows
query_result = pd.read_sql_query("SELECT * FROM healthcare_admissions LIMIT 5", conn)
print(query_result)

# Close connection
conn.close()
