import requests
import json
import math


regions = {"ALOLA" : "alolan", "GALARIAN" : "galarian", "HISUIAN" : "hisuian", "PALDEA" : "paldean"}
url = "https://pokemon-go-api.github.io/pokemon-go-api/api/pokedex.json"

# Calculates the max cp per pokemon based on level 40 or level 50.
def calc_max_cp(pokemon, level50):
    cpm = 0.84029999 if level50 else 0.7903
    
    attack = pokemon['stats']['attack'] + 15
    defense = math.sqrt(pokemon['stats']['defense'] + 15)
    hp = math.sqrt(pokemon['stats']['hp'] + 15)
    
    cp = ((attack * defense * hp * (cpm ** 2)) / 10)
    
    return math.floor(max(10, cp))


class Pokemon:
    def __init__(self, pokemon_dict, parent=None):

        if "formId" in pokemon_dict and not "NIDORAN" in pokemon_dict["id"]:
            nameArr = pokemon_dict["formId"].split("_")
            self.id = pokemon_dict["formId"]

        else:
            nameArr = pokemon_dict["id"].split("_")
            self.id = pokemon_dict["id"]

        tag = ""
        if "MEGA" in nameArr:
            if len(nameArr) == 3:
                poke_name = nameArr[1].capitalize() + " " + nameArr[0].capitalize() + " " + nameArr[2].capitalize()
                tag       = poke_name.split()[0] + "-" + poke_name.split()[2]
            
            else:
                poke_name = nameArr[1].capitalize() + " " + nameArr[0].capitalize()
                tag       = poke_name.split()[0]

        elif len(nameArr) == 2 and nameArr[1] in regions:
            poke_name = regions[nameArr[1]]  + " " +  nameArr[0].capitalize()
            tag = poke_name[0]

        else:
            poke_name = pokemon_dict["names"]["English"]

        self.name   = poke_name

        if "formId" in pokemon_dict and not "NIDORAN" in pokemon_dict["id"] : self.id = pokemon_dict["formId"]
        else                                                                : self.id = pokemon_dict["id"]

        if "MALE" in self.name:
            self.id +="_M"
            tag = "m"

        elif "FEMALE" in self.name:
            self.id += "_F"
            tag = "f"

        self.number = pokemon_dict["dexNr"] if not parent else parent.number 
        self.type1  = pokemon_dict["primaryType"]["names"]["English"]
        self.type2  = pokemon_dict["secondaryType"]["names"]["English"] if pokemon_dict["secondaryType"] else "none"
        self.stats  = pokemon_dict["stats"]

        if "quickMoves" in pokemon_dict:
            fast_moves = {}
            for move in pokemon_dict["quickMoves"]:
                name         = pokemon_dict["quickMoves"][move]["names"]["English"]
                move_type    = pokemon_dict["quickMoves"][move]["type"]["names"]["English"]
                power        = pokemon_dict["quickMoves"][move]["power"]
                energy_delta = pokemon_dict["quickMoves"][move]["energy"]
                duration     = pokemon_dict["quickMoves"][move]["durationMs"]

                fast_moves[name] = {
                    "type": move_type,
                    "power": power,
                    "energy delta": energy_delta,
                    "duration": duration,
                    "isLegacy": False,
                    "image": f"./assets/img/types/{move_type.lower()}.png"
                }

            for move in pokemon_dict["eliteQuickMoves"]:
                name         = pokemon_dict["eliteQuickMoves"][move]["names"]["English"]
                move_type    = pokemon_dict["eliteQuickMoves"][move]["type"]["names"]["English"]
                power        = pokemon_dict["eliteQuickMoves"][move]["power"]
                energy_delta = pokemon_dict["eliteQuickMoves"][move]["energy"]
                duration     = pokemon_dict["eliteQuickMoves"][move]["durationMs"]

                fast_moves[name] = {
                    "type": move_type,
                    "power": power,
                    "energy delta": energy_delta,
                    "duration": duration,
                    "isLegacy": True,
                    "image": f"./assets/img/types/{move_type.lower()}.png"
                }

            self.fast_moves = json.dumps(fast_moves)
        
        else:
            self.fast_moves = parent.fast_moves

        ####################################################################################

        if "quickMoves" in pokemon_dict:
            charged_moves = {}
            for move in pokemon_dict["cinematicMoves"]:
                name         = pokemon_dict["cinematicMoves"][move]["names"]["English"]
                move_type    = pokemon_dict["cinematicMoves"][move]["type"]["names"]["English"]
                power        = pokemon_dict["cinematicMoves"][move]["power"]
                energy_delta = pokemon_dict["cinematicMoves"][move]["energy"]
                duration     = pokemon_dict["cinematicMoves"][move]["durationMs"]

                charged_moves[name] = {
                    "type": move_type,
                    "power": power,
                    "energy delta": energy_delta,
                    "duration": duration,
                    "isLegacy": False,
                    "image": f"./assets/img/types/{move_type.lower()}.png"
                }

            for move in pokemon_dict["eliteCinematicMoves"]:
                name         = pokemon_dict["eliteCinematicMoves"][move]["names"]["English"]
                move_type    = pokemon_dict["eliteCinematicMoves"][move]["type"]["names"]["English"]
                power        = pokemon_dict["eliteCinematicMoves"][move]["power"]
                energy_delta = pokemon_dict["eliteCinematicMoves"][move]["energy"]
                duration     = pokemon_dict["eliteCinematicMoves"][move]["durationMs"]

                charged_moves[name] = {
                    "type": move_type,
                    "power": power,
                    "energy delta": energy_delta,
                    "duration": duration,
                    "isLegacy": True,
                    "image": f"./assets/img/types/{move_type.lower()}.png"
                }
            
            self.charged_moves = json.dumps(charged_moves)
        else:
            self.charged_moves = parent.charged_moves

        ####################################################################################

        pve = {}
        pvp = {}

        ####################################################################################

        

        ####################################################################################

        url = f"{self.number}-{tag.lower()}" if tag != "" else str(self.number)
        self.image = f'"./assets/img/sprites/{url}.png"'


# Writes the input pokemon's data to the file
def write_pokemon_data(file, pokemon):
    text = (
        f'\t"{pokemon.id}": {{\n'
        f'\t\t"name": "{pokemon.name}",\n'
        f'\t\t"number": {pokemon.number},\n'
        f'\t\t"type": ["{pokemon.type1}", "{pokemon.type2}"],\n'
        f'\t\t"stats": {{"attack": {pokemon.stats["attack"]}, "defense": {pokemon.stats["defense"]}, "hp": {pokemon.stats["stamina"]}}},\n'
        f'\t\t"fast_moves": {pokemon.fast_moves},\n'
        f'\t\t"charged_moves": {pokemon.charged_moves},\n'
        f'\t\t"image": {pokemon.image}\n'
    )
    file.write(text)



# Genereates the regular pokedex dictionary
def gen_dex_dict():
    # Checks to see if there API is up before overwriting files
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return

    # Creates/opens pokemon-reg.json
    with open("./data/pokemon.json", "w",encoding='utf-8') as file:
        file.write("{\n")
        for pokemon in data:
            if pokemon["stats"]:                
                # Create and write the main Pokemon object
                pokemonObj = Pokemon(pokemon)
                write_pokemon_data(file, pokemonObj)
                file.write(f'\t}},\n')

                # Create and write regional forms
                if pokemon["hasMegaEvolution"]:
                    for mega in pokemon["megaEvolutions"]:
                        megaObj = Pokemon(pokemon["megaEvolutions"][mega], pokemonObj)
                        write_pokemon_data(file, megaObj)
                        file.write(f'\t}},\n')

                # Create and write regional forms
                for regional in pokemon["regionForms"]:
                    if pokemonObj.name not in ["pikachu",]:
                        regionalObj = Pokemon(pokemon["regionForms"][regional])
                        write_pokemon_data(file, regionalObj)
                        file.write(f'\t}},\n')
        

    with open("./data/pokemon.json", "r") as infile:
        data = infile.read()
        data = data.rstrip(",\n")

    with open("./data/pokemon.json", "w") as outfile:
        outfile.write(data)
        outfile.write("\n}\n")

gen_dex_dict()