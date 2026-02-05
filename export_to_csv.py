from datasets import load_dataset
import pandas as pd
import os

# Create raw_data folder if not exists
os.makedirs("../raw_data", exist_ok=True)

print("Loading dataset from HuggingFace...")
ds = load_dataset("syncora/synthetic-healthcare-admissions")

# Convert train split to pandas DataFrame
df = ds["train"].to_pandas()

# Save as CSV
output_path = "../raw_data/healthcare_admissions.csv"
df.to_csv(output_path, index=False)

print("CSV file created successfully!")
print("Saved at:", output_path)
print("\nColumns in dataset:")
print(df.columns)
