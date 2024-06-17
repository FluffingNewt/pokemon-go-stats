import requests
import json
import math


regions = {"ALOLA" : "Alolan", "GALARIAN" : "Galarian", "HISUIAN" : "Hisuian", "PALDEA" : "Paldean"}
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
                tag       = poke_name.split()[0].lower() + "-" + poke_name.split()[2].lower()
            
            else:
                poke_name = nameArr[1].capitalize() + " " + nameArr[0].capitalize()
                tag       = poke_name.split()[0].lower()

        elif len(nameArr) == 2 and nameArr[1] in regions:
            poke_name = regions[nameArr[1]]  + " " +  nameArr[0].capitalize()
            tag = poke_name[0].lower()

        else:
            poke_name = pokemon_dict["names"]["English"]

        self.name   = poke_name

        if "formId" in pokemon_dict and not "NIDORAN" in pokemon_dict["id"] : self.id = pokemon_dict["formId"]
        else                                                                : self.id = pokemon_dict["id"]

        if "MALE" in self.name:
            self.id +="_MALE"
            tag = "m"

        elif "FEMALE" in self.name:
            self.id += "_FEMALE"
            tag = "f"

        if "MEWTWO_A" == self.id:
            self.id="MEWTWO_ARMORED"
            self.name="Armored Mewtwo"

        if "DARMANITAN_GALARIAN_STANDARD" == self.id:
            self.id="DARMANITAN_GALARIAN"
            self.name="Galarian Darmanitan"

        if "DARMANITAN_GALARIAN_ZEN" == self.id:
            self.id="DARMANITAN_GALARIAN_ZEN"
            self.name="Galarian Darmanitan (Zen Mode)"

        if "MEOWSTIC" == self.id:
            self.id="MEOWSTIC_MALE"
            tag = "m"
        
        if "MEOWSTIC_FEMALE" == self.id:
            tag = "f"

        self.number = pokemon_dict["dexNr"] if not parent else parent.number 
        self.type1  = pokemon_dict["primaryType"]["names"]["English"]
        self.type2  = pokemon_dict["secondaryType"]["names"]["English"] if pokemon_dict["secondaryType"] else "none"
        self.stats  = pokemon_dict["stats"]
        self.available = False

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
        f'\t\t"available": {str(pokemon.available).lower()},\n'
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
    with open("./lib/pokemon.json", "w",encoding='utf-8') as file:
        file.write("{\n")
        for pokemon in data:
            if pokemon["stats"]:                
                # Create and write the main Pokemon object
                pokemonObj = Pokemon(pokemon)
                if pokemonObj.name not in ["Giratina", "Shaymin", "Tornadus", "Thundurus",
                                           "Landorus", "Meloetta", "Hoopa", "Lycanroc",
                                           "Wishiwashi", "Toxtricity", "Eiscue", "Indeedee",
                                           "Urshifu", "Enamorus"]:
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
                    if pokemonObj.name not in ["Pikachu", "Eevee", "Espeon", "Umbreon", "Entei", "Raikou",
                                               "Suicune", "Lugia", "Ho-Oh", "Latios", "Latias", "Burmy",
                                               "Wormadam", "Cherrim", "Shellos", "Gastrodon", "Basculin",
                                               "Deerling", "Sawsbuck", "Frillish", "Jellicent", "Scatterbug",
                                               "Spewpa", "Vivillion", "Flabebe", "Floette", "Florges", "Furfrou",
                                               "Pumpkaboo", "Gourgeist", "Rockruff", "Minior", "Mimikyu", "Magearna",
                                               "Sinistea", "Polteageist", "Morpeko", "Eternatus", "Oikologne", "Maushold",
                                               "Squawkabilly", "Tatsugiri", "Dudunsparce", "Koraidon", "Miraidon"]:
                        regionalObj = Pokemon(pokemon["regionForms"][regional])
                        if regionalObj.id not in ["DARMANITAN_STANDARD", "KELDEO_ORDINARY", "ZACIAN_HERO", "ZAMAZENTA_HERO", "PALAFIN_ZERO"]:
                            write_pokemon_data(file, regionalObj)
                            file.write(f'\t}},\n')
        

    with open("./lib/pokemon.json", "r") as infile:
        data = infile.read()
        data = data.rstrip(",\n")

    with open("./lib/pokemon.json", "w") as outfile:
        outfile.write(data)
        outfile.write("\n}\n")


def updateAvailability():
    # Step 1: Read the JSON file
    with open("./lib/pokemon.json", 'r') as json_file:
        data = json.load(json_file)

    # Step 2: Read the config file line by line and update availability
    with open("./lib/avail_config.txt", 'r') as config_file:
        for line in config_file:
            line = line.strip()  # Remove newline characters and any leading/trailing whitespace
            if line:
                parts = line.split("=")
                key_part, value_part = parts
                key_parts = key_part.split("-")

                id = key_parts[1]
                availability = value_part.lower() == "true"

                if id in data: data[id]["available"] = availability

    # Step 3: Write back to the JSON file
    with open("./lib/pokemon.json", 'w') as json_file:
        json.dump(data, json_file)

# gen_dex_dict()

updateAvailability()

# with open("./lib/pokemon.json", 'r') as json_file:
#     json_data = json.load(json_file)

# with open("./lib/avail_config.txt", 'w') as config_file:
#     # Step 3: Loop through the keys in the dictionary
#     for value in json_data:
#         pokemon = json_data[value]

#         if pokemon in ["ROTOM_HEAT", "ROTOM_FAN", "DARMANITAN_ZEN", "DARMANITAN_GALARIAN_ZEN", "KYUREM_WHITE", "KYUREM_BLACK", "KELDEO_RESOLUTE", "MELOETTA_PIROUETTE", "NECROZMA_ULTRA",
#                        "ZACIAN_CROWNED_SWORD", "ZAMAZENTA_CROWNED_SHIELD", "ENAMORUS_THERIAN"]:
#             config_file.write(f"{pokemon["number"]}-{value}=false\n")

#         elif pokemon["number"] in [489, 490, 493, 679, 680, 681, 721, 746, 749, 750, 771, 772, 773, 774, 778, 781, 801, 807, 810, 811, 812, 813, 814, 815, 816, 817,
#                               821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849,
#                               850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 864, 868, 869, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882,
#                               883, 884, 885, 886, 887, 890, 891, 892, 896, 897, 898, 917, 918, 924, 925, 926, 927, 931, 932, 933, 934, 940, 941, 942, 943, 944, 945,
#                               946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 963, 964, 967, 968, 969, 970, 973, 976, 977, 978, 981, 982, 983,
#                               984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008]:
#             config_file.write(f"{pokemon["number"]}-{value}=false\n")

        

#         elif pokemon["name"] == "Camerupt":
#             config_file.write(f"{pokemon["number"]}-{value}_MEGA=false\n")

#         elif pokemon["name"] in ["Zorua", "Zoroark"]:
#             config_file.write(f"{pokemon["number"]}-{value}_HISUIAN=false\n")
        
#         else:
#             config_file.write(f"{pokemon["number"]}-{value}=true\n")