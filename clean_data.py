import pandas as pd
import os

# Load raw data
raw_path = "../raw_data/healthcare_admissions.csv"
df = pd.read_csv(raw_path)

print("Initial Data Info:")
print(df.info())
print("\nMissing values per column:\n", df.isnull().sum())

# --- Step 1: Rename columns for SQL compatibility ---
df.rename(columns={
    'Age': 'age',
    'Gender': 'gender',
    'Blood Type': 'blood_type',
    'Medical Condition': 'medical_condition',
    'Billing Amount': 'billing_amount',
    'Admission Type': 'admission_type',
    'Medication': 'medication',
    'Test Results': 'test_results'
}, inplace=True)

# --- Step 2: Handle missing values ---
# Here all numeric columns are filled with 0 if missing
numeric_cols = ['age', 'gender', 'blood_type', 'medical_condition', 'billing_amount',
                'admission_type', 'medication', 'test_results']

df[numeric_cols] = df[numeric_cols].fillna(0)

# --- Step 3: Remove unrealistic ages and billing amounts ---
df = df[(df['age'] > 0) & (df['age'] < 120)]
df = df[df['billing_amount'] >= 0]

# --- Step 4: Ensure proper data types ---
df[numeric_cols] = df[numeric_cols].astype(int)
df['billing_amount'] = df['billing_amount'].astype(float)

# --- Step 5: Save cleaned data ---
os.makedirs("../clean_data", exist_ok=True)
clean_path = "../clean_data/healthcare_admissions_clean.csv"
df.to_csv(clean_path, index=False)

print(f"\n✅ Cleaned CSV saved at: {clean_path}")
print("Preview of cleaned data:")
print(df.head())
