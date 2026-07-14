import requests #request: bibliotheque qui communique avec l'internet 
import json #pour que les données soient affiché proprement
import pandas as pd #pandas est excel de python : tableau avec des ligne et  des colonnes commen en excel mais juste du code

# L'adresse de l'API officielle allemande
#url : variable qu'on stocke dedans l'adresse de l'API = l'adresse ou on envoie la demande 
url = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs"

# Ce qu'on demande : offres "Data Analyst" à Berlin: le filtre dans le site 
#params = {"was": "Data Analyst","wo": "Berlin","page": 1,"size": 5}
# La clé d'accès publique (pas besoin de compte): pour dire que l'APi est accesible
# On envoie la demande à l'API
#response = requests.get(url, params=params, headers=headers)
# On affiche le résultat
#reponse_status: le code de reponse : si 200 c bon , si 404 page inrouvable, si 403 accés refusé 
#print("Statut :", response.status_code)
#print(response.json()): avec json brut les données recu en termibnal ne sont pas lisible
# pour que les données soient visibles plus proprement :
# data = response.json()
#indent: pour ajouter des espaces ds le resultat
#ensure_ascii=False :L'allemand a des caractères spéciaux comme ü, ö, ä, ß. Sans cette option, Python les transforme en codes bizarres
#print(json.dumps(data, indent=4, ensure_ascii=False)) 
#on va parcourir les offres et extraire juste les chaamps qu'on a besoin 
headers = {
    "X-API-Key": "jobboerse-jobsuche"
}
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
# Liste vide qui va stocker toutes nos offres
all_offers = []
for job in jobs:
    for city in cities:
        print(f"searching : {job} in {city}...")
        params = {
            "was": job,
            "wo": city,
            "page": 1,
            "size": 25
        }
        response = requests.get(url, params=params, headers=headers)
        data = response.json()
        if "stellenangebote" in data:

            for offre in data["stellenangebote"]:
                all_offers.append({
                    "title"      : offre["titel"],
                    "job"     : offre["beruf"],
                    "company" : offre.get("arbeitgeber", "Not provided"),
                    "city"      : offre["arbeitsort"].get("ort", "Not provided"),
                    "region"     : offre["arbeitsort"].get("region", "Not provided"),
                    "postal_code": offre["arbeitsort"].get("plz", "Not provided"),
                    "date"       : offre["aktuelleVeroeffentlichungsdatum"]
                })
#le f au debut en print sert a dire a python que le texte contient un variable (len())
print(f"\n Total offres collected : {len(all_offers)}")
print(f"\n First offre exemple :")
print(json.dumps(all_offers[0], indent=4, ensure_ascii=False))
df = pd.DataFrame(all_offers)
print(df.head())
print(f"\nDimensions : {df.shape[0]} rows x {df.shape[1]} columns")
df.to_csv("job_offers_germany.csv", index=False, encoding="utf-8-sig", sep=";")
print("\nCSV file saved successfully!")