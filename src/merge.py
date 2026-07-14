import pandas as pd

# Charger les deux sources
df_bundesagentur = pd.read_csv("job_offers_germany_clean.csv",
                                sep=";", encoding="utf-8-sig")

df_adzuna = pd.read_csv("adzuna_offers_germany.csv",
                         sep=";", encoding="utf-8-sig")

print(f"Bundesagentur offers : {len(df_bundesagentur)}")
print(f"Adzuna offers        : {len(df_adzuna)}")

# Colonnes communes entre les deux sources
df_bundesagentur_clean = df_bundesagentur[[
    "title", "job", "company", "city", "region", "date"
]].copy()

df_adzuna_clean = df_adzuna[[
    "title", "company", "city", "date",
    "contract_time", "salary_min", "salary_max", "salary_avg",
    "category", "description", "latitude", "longitude"
]].copy()

# Ajouter une colonne source pour savoir d'où vient chaque offre
df_bundesagentur_clean["source"] = "Bundesagentur"
df_adzuna_clean["source"]        = "Adzuna"

# Combiner les deux DataFrames
df_combined = pd.concat([df_bundesagentur_clean, df_adzuna_clean],
                         ignore_index=True)

print(f"\nTotal combined offers : {len(df_combined)}")
print(f"Columns : {list(df_combined.columns)}")

# Supprimer les doublons
df_combined = df_combined.drop_duplicates(subset=["title", "company", "city"])
print(f"After removing duplicates : {len(df_combined)}")

# Sauvegarder
df_combined.to_csv("job_offers_germany_combined.csv",
                    index=False, encoding="utf-8-sig", sep=";")

print("\nFile saved : job_offers_germany_combined.csv")