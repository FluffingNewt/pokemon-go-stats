import requests
import json
from lib import formulas


regions = ["ALOLA", "GALARIAN", "HISUIAN", "PALDEA"]
base_url = "https://pokemon-go-api.github.io/pokemon-go-api/api/pokedex"


class Pokemon:
    def __init__(self, pokemon, region):
        self.name   = pokemon["names"]["English"]
        self.number = pokemon["dexNr"]
        self.type1  = pokemon["primaryType"]["names"]["English"]
        self.type2  = pokemon["secondaryType"]["names"]["English"] if pokemon["secondaryType"] else "null"
        self.stats  = pokemon["stats"]
        self.fast_moves = [
            pokemon["quickMoves"][move]["names"]["English"]
            for move in pokemon["quickMoves"]
            ] + [
            pokemon["eliteQuickMoves"][move]["names"]["English"]
            for move in pokemon["eliteQuickMoves"]
        ]
        self.charged_moves = [
            pokemon["cinematicMoves"][move]["names"]["English"]
            for move in pokemon["cinematicMoves"]
            ] + [
            pokemon["eliteCinematicMoves"][move]["names"]["English"]
            for move in pokemon["eliteCinematicMoves"]
        ]
        
        self.image = f"./assets/sprites/{str}.png" if region == "" else f"./assets/sprites/{self.number}-{region.lower()}.png"

        self.max_cp = formulas.calc_max_cp(self.stats["attack"], self.stats["defense"], self.stats["stamina"])



class Mega:
    def __init__(self, pokemon, mega):
        self.name   = mega["names"]["English"]
        self.number = pokemon["dexNr"]
        self.type1  = mega["primaryType"]["names"]["English"]
        self.type2  = mega["secondaryType"]["names"]["English"] if mega["secondaryType"] else "null"
        self.stats  = mega["stats"]
        self.fast_moves = [
            pokemon["quickMoves"][move]["names"]["English"]
            for move in pokemon["quickMoves"]
            ] + [
            pokemon["eliteQuickMoves"][move]["names"]["English"]
            for move in pokemon["eliteQuickMoves"]
        ]
        self.charged_moves = [
            pokemon["cinematicMoves"][move]["names"]["English"]
            for move in pokemon["cinematicMoves"]
            ] + [
            pokemon["eliteCinematicMoves"][move]["names"]["English"]
            for move in pokemon["eliteCinematicMoves"]
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
    response = requests.get(url)
    data = response.json()

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
    response = requests.get(url)
    data = response.json()

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




gen_dex_dict()
gen_mega_dict()