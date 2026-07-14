import pandas as pd

# Load combined data
df = pd.read_csv("job_offers_germany_combined.csv",
                  sep=";", encoding="utf-8-sig")

print("=== INITIAL STATE ===")
print(f"Number of offers  : {df.shape[0]}")
print(f"Number of columns : {df.shape[1]}")

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

print("\n=== DUPLICATES ===")
print(f"Number of duplicates : {df.duplicated().sum()}")

# Remove duplicates
df_clean = df.drop_duplicates()

# Clean salary columns — remove obvious outliers
# Salaries below 10000 or above 500000 are likely errors
df_clean = df_clean[
    (df_clean["salary_min"].isna()) |
    (df_clean["salary_min"].between(10000, 500000))
]

df_clean = df_clean[
    (df_clean["salary_max"].isna()) |
    (df_clean["salary_max"].between(10000, 500000))
]

# Clean date column
df_clean["date"] = pd.to_datetime(df_clean["date"], errors="coerce")

print(f"\n=== AFTER CLEANING ===")
print(f"Before : {df.shape[0]} offers")
print(f"After  : {df_clean.shape[0]} offers")

# Save clean file
df_clean.to_csv("data/job_offers_germany_combined_clean.csv",
                 index=False, encoding="utf-8-sig", sep=";")

print("\nClean file saved : job_offers_germany_combined_clean.csv")