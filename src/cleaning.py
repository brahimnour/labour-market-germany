import pandas as pd
# Load raw data
df = pd.read_csv("job_offers_germany.csv", sep=";", encoding="utf-8-sig")

print("Initial state ")
print(f"Numbers of offers : {df.shape[0]}")
print(f"Numbers of columns : {df.shape[1]}")

print("\n Missing values ")
print(df.isnull().sum())

print("\n Duplicates")
print(f"Number of duplicates : {df.duplicated().sum()}")

print("\n Data overview ")
print(df.head())
# We create a new DataFrame because we always keep the raw data untouched
df_propre = df.drop_duplicates()
#verification
print(f"Before cleaning : {df.shape[0]} offres")
print(f"After cleaning : {df_propre.shape[0]} offres")
print(f"Duplicates removed : {df.shape[0] - df_propre.shape[0]}")
# Save clean data to a new file
df_propre.to_csv("job_offers_germany_clean.csv", index=False, encoding="utf-8-sig", sep=";")

print("\n Clean file saved successfully !")
