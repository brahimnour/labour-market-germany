import requests
import json
import pandas as pd
import time

APP_ID  = "ee9f9103"
APP_KEY = "ff8f3ca74cb967af884fdcd0166df600"

url = "https://api.adzuna.com/v1/api/jobs/de/search/1"

jobs = [
    "Data Analyst",
    "Python Developer",
    "Data Engineer",
    "Machine Learning",
    "Software Engineer"
]

cities = [
    "Berlin",
    "Munich",
    "Hamburg",
    "Frankfurt",
    "Cologne"
]

all_offers = []

for job in jobs:
    for city in cities:
        print(f"Searching: {job} in {city}...")

        params = {
            "app_id"          : APP_ID,
            "app_key"         : APP_KEY,
            "what"            : job,
            "where"           : city,
            "results_per_page": 50,
            "content-type"    : "application/json"
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()

            if "results" in data:
                for offer in data["results"]:

                    # Extraire salary_min et salary_max en securite
                    salary_min = offer.get("salary_min", None)
                    salary_max = offer.get("salary_max", None)

                    # Calculer le salaire moyen si les deux sont disponibles
                    if salary_min and salary_max:
                        salary_avg = (salary_min + salary_max) / 2
                    else:
                        salary_avg = None

                    all_offers.append({
                        "title"        : offer.get("title", "Not provided"),
                        "company"      : offer.get("company", {}).get("display_name", "Not provided"),
                        "city"         : city,
                        "date"         : offer.get("created", "Not provided")[:10],
                        "contract_time": offer.get("contract_time", "Not provided"),
                        "salary_min"   : salary_min,
                        "salary_max"   : salary_max,
                        "salary_avg"   : salary_avg,
                        "category"     : offer.get("category", {}).get("label", "Not provided"),
                        "description"  : offer.get("description", "Not provided"),
                        "latitude"     : offer.get("latitude", None),
                        "longitude"    : offer.get("longitude", None),
                        "url"          : offer.get("redirect_url", "Not provided"),
                        "search_job"   : job
                    })

                print(f"Found : {len(data['results'])} offers")

        else:
            print(f"Error {response.status_code}")

        # Pause pour respecter les limites de l'API
        time.sleep(1)

# Résultats
print(f"\nTotal offers collected : {len(all_offers)}")

# Sauvegarder
df = pd.DataFrame(all_offers)
print(df.head())
print(f"\nDimensions : {df.shape[0]} rows x {df.shape[1]} columns")

df.to_csv("adzuna_offers_germany.csv",
          index=False, encoding="utf-8-sig", sep=";")

print("\nFile saved : adzuna_offers_germany.csv")