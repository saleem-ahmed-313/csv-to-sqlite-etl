# 📊 CSV to SQLite ETL Pipeline

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![Status](https://img.shields.io/badge/Project-Simple%20Demo-orange.svg)]()  

This project demonstrates a basic **ETL (Extract, Transform, Load) pipeline** in Python.  
It reads data from a **CSV file**, cleans/transforms it, and loads the results into a **SQLite database**.

---

## 🚀 Features
- **Extractor** → Reads data from a CSV file.  
- **Transformer** → Cleans and validates data (trims spaces, checks age, fills missing values).  
- **Loader** → Loads data into a SQLite database (`etl_demo.db`).  
- **Pipeline** → Orchestrates the ETL process end-to-end.  

---

## 🏗️ How It Works
1. **Extract**: Reads raw data from `input.csv`.  
2. **Transform**:  
   - Trims spaces from names and cities.  
   - Replaces empty values with `"Unknown"`.  
   - Converts age to integer (or `None` if invalid).  
3. **Load**: Inserts cleaned data into SQLite (`people` table).  

---

## 📦 Setup Instructions

### 1️⃣ Clone the repo
```bash
git clone https://github.com/your-username/csv-to-sqlite-etl.git
cd csv-to-sqlite-etl
