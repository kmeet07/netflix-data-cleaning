import pandas as pd

# Load the dataset
df = pd.read_csv("netflix_titles.csv")

# Initial check
print("Initial data shape:", df.shape)
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# -------------------------------
# 1. Handle Missing Values
# -------------------------------

# Fill 'director' and 'cast' missing values with 'Unknown'
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Unknown', inplace=True)

# Drop rows where 'country', 'date_added', or 'rating' is missing
df.dropna(subset=['country', 'date_added', 'rating'], inplace=True)

# -------------------------------
# 2. Remove Duplicates
# -------------------------------
df.drop_duplicates(inplace=True)

# -------------------------------
# 3. Standardize Text Columns
# -------------------------------
string_columns = ['type', 'title', 'director', 'cast', 'country', 'rating', 'listed_in']
for col in string_columns:
    df[col] = df[col].astype(str).str.lower().str.strip()

# -------------------------------
# 4. Convert Date Format
# -------------------------------
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# -------------------------------
# 5. Rename Columns
# -------------------------------
df.columns = df.columns.str.lower().str.replace(" ", "_")

# -------------------------------
# 6. Fix Data Types
# -------------------------------
df['show_id'] = df['show_id'].astype(str)

# -------------------------------
# 7. Save Cleaned Dataset
# -------------------------------
df.to_csv("cleaned_netflix_titles.csv", index=False)

# -------------------------------
# 8. Summary
# -------------------------------
print("\n✅ Cleaning Complete!")
print("Cleaned data shape:", df.shape)
print("\nRemaining missing values:")
print(df.isnull().sum())
print("\nData types:")
print(df.dtypes)
