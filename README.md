# Pokémon Raid Finder

This project is a script designed to find and filter Pokémon raid data from two different APIs (`nycpokemap.com` and `sgpokemap.com`). The script identifies raids featuring specific Pokémon with given forms and displays relevant information.

---

## Features

- **Fetch Raid Data**: Pulls raid data from New York and Singapore Pokémon Map APIs.
- **Filter by Pokémon ID and Form**: Filters raids based on a specified Pokémon ID and a list of target forms.
- **Consolidate Results**: Combines results from both sources and displays matching raids.

---

## Requirements

To run this project, you need the following:

- Python 3.7 or later
- `requests` library for making HTTP requests

Install dependencies using:

```bash
pip install requests
```

---

## Usage

### 1. Clone the Repository

```bash
git clone https://github.com/raul-anton-2005/pokemon-raids
cd pokemon-raids
```

### 2. Run the Script

Run the script with:

```bash
python raids.py
```

### 3. Modify Parameters

To search for specific Pokémon or forms, update the following variables in the script:

```python
pokemon_lf = 854  # Pokémon ID to search for
forms_lf = [2478, 2481]  # List of form IDs to filter
```

---

## Output

- If matching raids are found:
  ```plaintext
  Raids con pokemon_id igual a 854 y form [2478, 2481]:
  {raid details...}
  ```
- If no matches are found:
  ```plaintext
  No se encontraron raids con pokemon_id igual a 854 y form [2478, 2481].
  ```

---

## JSON Reference

The script uses Pokémon and form IDs. Here's an example structure of the mappings used to interpret form IDs:

```json
{
  "2478": "Antique",
  "2481": "Antique",
  "854": "Specific Pokémon Name"
}
```

You can customize or expand the mapping in your local implementation.

---

## Future Enhancements

- Add support for more Pokémon Maps or APIs.
- Provide a user-friendly interface for specifying Pokémon IDs and forms.
- Localize output messages into multiple languages.
- Optimize API calls to handle large-scale data efficiently.

---

## Contributing

Contributions are welcome! Please fork the repository, create a new branch for your feature or bug fix, and submit a pull request.

---

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it.