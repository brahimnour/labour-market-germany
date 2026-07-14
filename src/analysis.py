import pandas as pd
import matplotlib.pyplot as plt #biblio génératrice de graphiques
df = pd.read_csv("job_offers_germany_clean.csv", sep=";", encoding="utf-8-sig")
print("Data overview")
print(df.head())

print(f"\n Top regions : {df.shape[0]}")
print("\n=== Top regions ===")
top_regions = df["region"].value_counts().head(10)
print(top_regions)
print("\n=== Top jobs ===")
top_jobs = df["job"].value_counts().head(10)
print(top_jobs)
print("\n=== Top companies ===")
top_companies = df["company"].value_counts().head(10)
print(top_companies)

# GRAPH 1: Top 10 regions

plt.figure(figsize=(10, 6))#10 la longeur , 6 hauteur en pouces 
top_regions.plot(kind="barh", color="steelblue") #graph en barh ; le plus lisible pour les lons noms
plt.title("Top 10 Regions Hiring in Germany")
plt.xlabel("Number of offers") 
plt.ylabel("Region")
plt.tight_layout()# Ajuste automatiquement les marges pour que rien ne soit coupé.
plt.savefig("top_regions.png")
plt.show()
print("Graph saved: top_regions.png")


# GRAPH 2: Top 10 jobs

plt.figure(figsize=(10, 6))
top_jobs.plot(kind="barh", color="darkorange")
plt.title("Top 10 Most Demanded IT Jobs in Germany")
plt.xlabel("Number of offers")
plt.ylabel("Job title")
plt.tight_layout()
plt.savefig("top_jobs.png")
plt.show()
print("Graph saved: top_jobs.png")


# GRAPH 3: Top 10 companies

plt.figure(figsize=(10, 6))
top_companies.plot(kind="barh", color="green")
plt.title("Top 10 Companies Hiring in Germany")
plt.xlabel("Number of offers")
plt.ylabel("Company")
plt.tight_layout()
plt.savefig("top_companies.png")
plt.show()
print("Graph saved: top_companies.png")


# GRAPH 4: Offers over time

# Convert date column to datetime format
df["date"] = pd.to_datetime(df["date"])

# Group offers by week
offers_by_week = df.groupby(df["date"].dt.isocalendar().week).size()
# pd.to_datetime(df["date"])Convertit la colonne date de texte en vrai format date — comme ça pandas peut faire des calculs dessus.
# dt.isocalendar().week Extrait le numéro de semaine de chaque date — semaine 1, semaine 2, etc.
# groupby(...).size() Regroupe les offres par semaine et compte combien il y en a par semaine.
plt.figure(figsize=(12, 6))
#kind="line" Graphique en ligne au lieu de barres — parfait pour montrer une évolution dans le temps.
#marker="o" Ajoute un point à chaque semaine sur la ligne.
offers_by_week.plot(kind="line", color="purple", marker="o")
plt.title("Job Offers Evolution Over Time (by week)")
plt.xlabel("Week number")
plt.ylabel("Number of offers")
plt.tight_layout()
plt.savefig("offers_over_time.png")
plt.show()
print("Graph saved: offers_over_time.png")

# GRAPH 5: Top skills demanded
# =====================

# List of technical skills to search for in job titles
skills = [
    "Python", "SQL", "Excel", "Power BI", "Tableau",
    "Machine Learning", "Deep Learning", "AWS", "Azure",
    "Docker", "Kubernetes", "Spark", "Hadoop",
    "TensorFlow", "PyTorch", "Git", "Linux", "Java",
    "JavaScript", "Scala"
]

# Count how many job titles mention each skill
skill_counts = {}

for skill in skills:
    # Check if the skill appears in the title column (case insensitive)
    count = df["title"].str.contains(skill, case=False, na=False).sum()
    skill_counts[skill] = count

# Convert to pandas Series and sort
skill_series = pd.Series(skill_counts).sort_values(ascending=False)

# Keep only skills that appear at least once
skill_series = skill_series[skill_series > 0]

print("\n=== TOP SKILLS ===")
print(skill_series)

# Graph
plt.figure(figsize=(10, 6))
skill_series.plot(kind="barh", color="crimson")
plt.title("Most Demanded IT Skills in Germany")
plt.xlabel("Number of job offers mentioning this skill")
plt.ylabel("Skill")
plt.tight_layout()
plt.savefig("top_skills.png")
plt.show()
print("Graph saved: top_skills.png")

