import requests
import json

headers = {
    "X-API-Key": "jobboerse-jobsuche"
}

url_liste = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs"

params = {
    "was": "Data Analyst",
    "wo": "Berlin",
    "page": 1,
    "size": 10
}

response = requests.get(url_liste, params=params, headers=headers)
data = response.json()

# Chercher une offre récente
for offre in data["stellenangebote"]:
    refnr = offre["refnr"]
    date  = offre["aktuelleVeroeffentlichungsdatum"]
    print(f"Date : {date} | Ref : {refnr}")

    # Tester le detail de cette offre
    url_detail = f"https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobdetails/{refnr}"
    response_detail = requests.get(url_detail, headers=headers)

    if response_detail.status_code == 200:
        print("OFFRE TROUVEE !")
        detail = response_detail.json()
        print(json.dumps(detail, indent=4, ensure_ascii=False))
        break
    else:
        print(f"Status {response_detail.status_code} — offre expiree, on essaie la suivante...")
        print("")