import requests
import json

# Tes clés Adzuna
APP_ID  = "ee9f9103"
APP_KEY = "ff8f3ca74cb967af884fdcd0166df600"

# Endpoint Adzuna pour l'Allemagne
url = "https://api.adzuna.com/v1/api/jobs/de/search/1"

params = {
    "app_id"          : APP_ID,
    "app_key"         : APP_KEY,
    "what"            : "Data Analyst",
    "where"           : "Berlin",
    "results_per_page": 5,
    "content-type"    : "application/json"
}

response = requests.get(url, params=params)

print(f"Status : {response.status_code}")
print(json.dumps(response.json(), indent=4, ensure_ascii=False))