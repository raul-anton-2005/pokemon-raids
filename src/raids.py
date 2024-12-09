import json
import requests
import time

def fetch_json(link):
    timestamp = int(time.time() * 1000)
    
    url = f"{link}{timestamp}"
    
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
    
pokemon_lf = 854
forms_lf = [2478, 2481]

json_nyc = fetch_json("https://nycpokemap.com/raids.php?time=")
json_sing = fetch_json("https://sgpokemap.com/raids.php?time=")

matching_raids = []
for raid in json_nyc.get("raids", []):
    if raid.get("pokemon_id") == pokemon_lf and raid.get("form") in forms_lf:
        matching_raids.append(raid)

for raid in json_sing.get("raids", []):
    if raid.get("pokemon_id") == pokemon_lf and raid.get("form") in forms_lf:
        matching_raids.append(raid)

if matching_raids:
    print(f"Raids con pokemon_id igual a {pokemon_lf} y form {forms_lf}:")
    for raid in matching_raids:
        print(raid)
        print() 
else:
    print(f"No se encontraron raids con pokemon_id igual a {pokemon_lf} y form {forms_lf}:")
