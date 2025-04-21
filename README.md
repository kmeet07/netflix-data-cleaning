# Netflix Dataset - Data Cleaning Task

## 🧹 Task 1: Data Cleaning and Preprocessing

### 📂 Dataset Used
Netflix Movies and TV Shows from Kaggle  
[Link](https://www.kaggle.com/datasets/shivamb/netflix-shows)

---

### ✅ Summary of Cleaning Steps

- **Missing Values:**
  - Filled missing values in `director` and `cast` with `'Unknown'`.
  - Dropped rows where `country`, `rating`, or `date_added` was missing.

- **Duplicates:**
  - Removed all duplicate rows (if any).

- **Standardization:**
  - Converted all text columns to lowercase and stripped spaces.
  - Standardized country, rating, and category fields.

- **Date Format:**
  - Converted `date_added` to datetime format using `pd.to_datetime()`.

- **Renaming Columns:**
  - Converted column names to lowercase and snake_case.

- **Data Types:**
  - Converted `show_id` to string, `date_added` to datetime.

---

### 📁 Files Included
- `netflix_titles.csv` – Original dataset
- `cleaned_netflix_titles.csv` – Cleaned dataset
- `netflix_cleaning.ipynb` – Jupyter notebook used for cleaning
- `README.md` – Summary of work done
