import pandas as pd
import matplotlib.pyplot as plt
# Load combined clean data
df = pd.read_csv("job_offers_germany_combined_clean.csv",
                  sep=";", encoding="utf-8-sig")

print(f"Total offers : {df.shape[0]}")
# Normaliser les noms de villes
df["city"] = df["city"].replace({
    "Frankfurt am Main" : "Frankfurt",
    "Eschborn, Taunus"  : "Frankfurt",
    "Langen (Hessen)"   : "Frankfurt",
    "Bad Vilbel"        : "Frankfurt"
})

# ANALYSE 1 : Top regions
print("\n=== TOP REGIONS ===")
top_regions = df["city"].value_counts().head(10)
print(top_regions)

# ANALYSE 2 : Top jobs
print("\n=== TOP JOBS ===")
top_jobs = df["title"].value_counts().head(10)
print(top_jobs)

# ANALYSE 3 : Top companies
print("\n=== TOP COMPANIES ===")
top_companies = df["company"].value_counts().head(10)
print(top_companies)

# ANALYSE 4 : Contract types
print("\n=== CONTRACT TYPES ===")
contract_types = df["contract_time"].value_counts()
print(contract_types)

# ANALYSE 5 : Salary analysis
print("\n=== SALARY ANALYSIS ===")
df_salary = df[df["salary_avg"].notna()]
print(f"Offers with salary : {len(df_salary)}")
print(f"Average salary     : {df_salary['salary_avg'].mean():.0f} EUR")
print(f"Min salary         : {df_salary['salary_min'].min():.0f} EUR")
print(f"Max salary         : {df_salary['salary_max'].max():.0f} EUR")

# ANALYSE 6 : Salary by city
print("\n=== AVERAGE SALARY BY CITY ===")
salary_by_city = df_salary.groupby("city")["salary_avg"].mean().sort_values(ascending=False)
print(salary_by_city)

# ANALYSE 7 : Data sources
print("\n=== DATA SOURCES ===")
print(df["source"].value_counts())
# GRAPH 1 : Top cities
fig, ax = plt.subplots(figsize=(10, 5))
top_cities = df["city"].value_counts().head(8)
top_cities.plot(kind="barh", ax=ax, color="#6B1E2E")
ax.set_title("Top Cities Hiring in Germany")
ax.set_xlabel("Number of offers")
plt.tight_layout()
plt.savefig("top_cities.png")
plt.show()

# GRAPH 2 : Salary by city
fig, ax = plt.subplots(figsize=(10, 5))
salary_by_city.plot(kind="barh", ax=ax, color="#C48A8A")
ax.set_title("Average Salary by City (EUR)")
ax.set_xlabel("Average salary (EUR)")
plt.tight_layout()
plt.savefig("salary_by_city.png")
plt.show()

# GRAPH 3 : Contract types
fig, ax = plt.subplots(figsize=(8, 5))
contract_types = df[df["contract_time"] != "Not provided"]["contract_time"].value_counts()
contract_types.plot(kind="bar", ax=ax, color=["#6B1E2E", "#C48A8A"])
ax.set_title("Contract Types Distribution")
ax.set_xlabel("Contract type")
ax.set_ylabel("Number of offers")
plt.tight_layout()
plt.savefig("contract_types.png")
plt.show()

# GRAPH 4 : Salary distribution
fig, ax = plt.subplots(figsize=(10, 5))
df_salary["salary_avg"].hist(bins=20, ax=ax, color="#6B1E2E", edgecolor="white")
ax.set_title("Salary Distribution in Germany IT Market")
ax.set_xlabel("Salary (EUR)")
ax.set_ylabel("Number of offers")
plt.tight_layout()
plt.savefig("salary_distribution.png")
plt.show()

print("\nAll graphs saved !")