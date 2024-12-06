import json

with open('src/raids.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

matching_raids = []
for raid in data.get("raids", []):
    if raid.get("pokemon_id") == 854 and raid.get("form") in [2478, 2481]:
        matching_raids.append(raid)

if matching_raids:
    print("Raids con pokemon_id igual a 854 y form igual a 2478 o 2481:")
    for raid in matching_raids:
        print(raid)
        print() 
else:
    print("No se encontró ningún raid con pokemon_id igual a 854 y form igual a 2478 o 2481.")
