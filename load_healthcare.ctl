LOAD DATA
INFILE 'C:\ETL_Healthcare_Project\clean_data\healthcare_admissions_clean.csv'
INTO TABLE healthcare_admissions
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
TRAILING NULLCOLS
(
age,
gender,
blood_type,
medical_condition,
billing_amount,
admission_type,
medication,
test_results
)
