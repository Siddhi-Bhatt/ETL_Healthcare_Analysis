# 🏥 Healthcare Admissions Analytics Dashboard

An end-to-end **data analytics project** that analyzes healthcare admission records stored in an **Oracle Database**, visualized through an **interactive Power BI dashboard**, and supported by a **Python-based data pipeline**.

This project demonstrates real-world data handling, database integration, dashboard storytelling, and business insights — similar to industry analytics workflows.

---

## 📌 Project Overview
- Analyze patient admission data  
- Identify trends in medical conditions, billing, and test results  
- Present insights through an interactive dashboard  
- Simulate an auto-refreshable analytics system (database → dashboard)  

---

# 🛠️ Tech Stack
- **Data Source:** Kaggle Healthcare Admissions Dataset  
- **Backend / Database:** Oracle Database (SQL tables for structured storage)  
- **Data Processing:** Python (pandas, numpy, cx_Oracle)  
- **Visualization:** Power BI (interactive charts, filters, KPI cards)  
- **Version Control:** GitHub (documentation, scripts, screenshots)  

---

# 🗄️ Database Schema
**Table: healthcare_admissions**

| Column Name       | Data Type     | Description                          |
|-------------------|--------------|--------------------------------------|
| AGE               | NUMBER       | Patient age                          |
| GENDER            | NUMBER       | Encoded gender                       |
| BLOOD_TYPE        | NUMBER       | Encoded blood group                  |
| MEDICAL_CONDITION | NUMBER       | Encoded medical condition            |
| BILLING_AMOUNT    | NUMBER(10,2) | Total billing amount                 |
| ADMISSION_TYPE    | NUMBER       | Emergency / Routine / etc            |
| MEDICATION        | NUMBER       | Prescribed medication                |
| TEST_RESULTS      | NUMBER       | Test outcome                         |
| LOAD_DATE         | DATE         | Data load timestamp                  |

---

# 🔄 Data Refresh Logic
- Dataset is static but refresh behavior is simulated  
- Power BI uses **DirectQuery / Scheduled Refresh**  
- Python ETL updates Oracle DB → Power BI reflects changes automatically  

---

# 📊 Dashboard Features
- **KPIs:** Total Admissions, Avg Billing Amount, Test Results Status  
- **Visualizations:** Admissions by Condition, Billing by Admission Type, Test Results Distribution, Age Group Analysis, Gender Distribution  
- **Filters:** Admission Type, Medical Condition, Test Result Status  
<img width="1337" height="753" alt="Screenshot (100)" src="https://github.com/user-attachments/assets/d11e0158-8e83-4e15-a25c-a377e1196b6d" />

---

# 📖 Insights
- Certain medical conditions lead to higher billing  
- Emergency admissions contribute disproportionately to revenue  
- Abnormal test results more common in specific age groups  
- Elderly patients show higher admission frequency & billing  
- Gender-based patterns visible across conditions and outcomes  

---

# 🚀 Future Enhancements 
- Replace static Kaggle data with real-time API
- Deploy dashboard via Superset / Metabase
- Build Flask/FastAPI backend 
- Host dashboard on portfolio website

---

# 🧠 Skills Demonstrated 
- SQL (Oracle)
- Data Modeling
- Python ETL
- Power BI Dashboard Design
- Data Storytelling
- Analytics Architecture 
