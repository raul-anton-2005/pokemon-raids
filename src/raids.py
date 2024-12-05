import json

with open('src/raids2.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

matching_raids = [
    raid for raid in data.get("raids", [])
    if raid.get("pokemon_id") == 854 and (raid.get("form") == 2478 or raid.get("form") == 2481)
]

if matching_raids:
    print("Raids con pokemon_id igual a 854 y form diferente de 2477:")
    for raid in matching_raids:
        print(raid)
        print()
else:
    print("No se encontró ningún raid con pokemon_id igual a 854 y form diferente de 2477.")
