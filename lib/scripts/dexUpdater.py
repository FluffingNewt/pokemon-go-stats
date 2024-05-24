import requests
from lib import formulas


regions = ["ALOLA", "GALARIAN", "HISUIAN", "PALDEA"]
base_url = "https://pokemon-go-api.github.io/pokemon-go-api/api/pokedex"


class Pokemon:
    def __init__(self, pokemon_dict, region):
        self.name   = pokemon_dict["names"]["English"]
        self.number = pokemon_dict["dexNr"]
        self.type1  = pokemon_dict["primaryType"]["names"]["English"]
        self.type2  = pokemon_dict["secondaryType"]["names"]["English"] if pokemon_dict["secondaryType"] else "none"
        self.stats  = pokemon_dict["stats"]
        self.fast_moves = [
            pokemon_dict["quickMoves"][move]["names"]["English"]
            for move in pokemon_dict["quickMoves"]
            ] + [
            pokemon_dict["eliteQuickMoves"][move]["names"]["English"]
            for move in pokemon_dict["eliteQuickMoves"]
        ]
        self.charged_moves = [
            pokemon_dict["cinematicMoves"][move]["names"]["English"]
            for move in pokemon_dict["cinematicMoves"]
            ] + [
            pokemon_dict["eliteCinematicMoves"][move]["names"]["English"]
            for move in pokemon_dict["eliteCinematicMoves"]
        ]
        
        self.image = f"./assets/sprites/{str}.png" if region == "" else f"./assets/sprites/{self.number}-{region.lower()}.png"

        self.max_cp = formulas.calc_max_cp(self.stats["attack"], self.stats["defense"], self.stats["stamina"])



class Mega:
    def __init__(self, pokemon_dict, mega_dict):
        self.name   = mega_dict["names"]["English"]
        self.number = pokemon_dict["dexNr"]
        self.type1  = mega_dict["primaryType"]["names"]["English"]
        self.type2  = mega_dict["secondaryType"]["names"]["English"] if mega_dict["secondaryType"] else "none"
        self.stats  = mega_dict["stats"]
        self.fast_moves = [
            pokemon_dict["quickMoves"][move]["names"]["English"]
            for move in pokemon_dict["quickMoves"]
            ] + [
            pokemon_dict["eliteQuickMoves"][move]["names"]["English"]
            for move in pokemon_dict["eliteQuickMoves"]
        ]
        self.charged_moves = [
            pokemon_dict["cinematicMoves"][move]["names"]["English"]
            for move in pokemon_dict["cinematicMoves"]
            ] + [
            pokemon_dict["eliteCinematicMoves"][move]["names"]["English"]
            for move in pokemon_dict["eliteCinematicMoves"]
        ]
        
        url = f"{self.number}-mega"
        if self.name[-1] in {"X", "Y"}:
                url += f"-{self.name[-1].lower()}"

        self.image = f"./assets/sprites/{url}.png"

        self.max_cp = formulas.calc_max_cp(self.stats["attack"], self.stats["defense"], self.stats["stamina"])



# Writes the input pokemon's data to the file
def write_pokemon_data(file, pokemon):
    text = (
        f'\t"{pokemon.name}": {{\n'
        f'\t\t"number": {pokemon.number},\n'
        f'\t\t"type": ["{pokemon.type1}", "{pokemon.type2}"],\n'
        f'\t\t"stats": {{"attack": {pokemon.stats["attack"]}, "defense": {pokemon.stats["defense"]}, "hp": {pokemon.stats["stamina"]}}},\n'
        f'\t\t"max_cp": {pokemon.max_cp},\n'
        f'\t\t"fast_moves": {pokemon.fast_moves},\n'
        f'\t\t"charged_moves": {pokemon.charged_moves},\n'
        f'\t\t"image": "{pokemon.image}"\n'
        f'\t}},\n'
    )
    file.write(text)



# Genereates the regular pokedex dictionary
def gen_dex_dict():
    url = f"{base_url}.json"

    # Checks to see if there API is up before overwriting files
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return

    with open("./assets/pokemon-reg.py", "w") as file:
        file.write("pokemon = {\n")

        for pokemon in data:
            if pokemon["stats"]:
                # Create and write the main Pokemon object
                pokemon_obj = Pokemon(pokemon, "")
                write_pokemon_data(file, pokemon_obj)

                # Create and write regional forms
                for regional in pokemon["regionForms"]:
                    for region in regions:
                        if region in regional:
                            regionalObj = Pokemon(pokemon["regionForms"][regional], region)
                            write_pokemon_data(file, regionalObj)
                            
        file.write("}\n")



# Generates the mega evolution pokedex dictionary
def gen_mega_dict():
    url = f"{base_url}/mega.json"
    
    # Checks to see if there API is up before overwriting files
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return

    with open("./assets/pokemon-mega.py", "w") as file:
        file.write("megas = {\n")
        prev_entry = ""
        for pokemon in data:
            if prev_entry != pokemon["names"]["English"]:
                for mega in pokemon["megaEvolutions"]:
                    mega_obj = Mega(pokemon, pokemon["megaEvolutions"][mega])
                    write_pokemon_data(file, mega_obj)

            prev_entry = pokemon["names"]["English"]

        file.write("}\n")