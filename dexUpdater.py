import requests
from lib import formulas

regions = ["ALOLA", "GALARIAN", "HISUIAN", "PALDEA"]

base_url = "https://pokemon-go-api.github.io/pokemon-go-api/api/pokedex"

# Megas
def gen_mega_dict():
    url = base_url + "/mega.json"
    response = requests.get(url)
    data = response.json()

    with open("./assets/pokemon-mega.py", "w") as file:
        file.write("megas = {\n")
        prev_entry = ""

        for pokemon in data:
            number = pokemon["dexNr"]
            if prev_entry == pokemon["names"]["English"]:
                continue

            for mega in pokemon["megaEvolutions"].values():
                name  = mega["names"]["English"]
                type1 = mega["primaryType"]["names"]["English"]
                type2 = mega["secondaryType"]["names"]["English"] if mega["secondaryType"] else "null"
                stats = mega["stats"]

                image = f"{number}-mega"
                if name[-1] in {"X", "Y"}: image += f"-{name[-1].lower()}"

                fast_moves = [
                    pokemon["quickMoves"][move]["names"]["English"]
                    for move in pokemon["quickMoves"]
                ] + [
                    pokemon["eliteQuickMoves"][move]["names"]["English"]
                    for move in pokemon["eliteQuickMoves"]
                ]

                charged_moves = [
                    pokemon["cinematicMoves"][move]["names"]["English"]
                    for move in pokemon["cinematicMoves"]
                ] + [
                    pokemon["eliteCinematicMoves"][move]["names"]["English"]
                    for move in pokemon["eliteCinematicMoves"]
                ]

                file.write(f'\t"{name}": {{\n')
                file.write(f'\t\t"number": "{number}",\n')
                file.write(f'\t\t"type": ["{type1}", "{type2}"],\n')
                file.write(f'\t\t"stats": {{"attack": {stats["attack"]}, "defense": {stats["defense"]}, "hp": {stats["stamina"]}}},\n')
                file.write(f'\t\t"max_cp": {formulas.calc_max_cp(stats["attack"], stats["defense"], stats["stamina"])},\n')
                file.write(f'\t\t"fast_moves": {fast_moves},\n')
                file.write(f'\t\t"charged_moves": {charged_moves},\n')
                file.write(f'\t\t"image": "./assets/sprites/{image}.png"\n')
                file.write('\t},\n')

            prev_entry = pokemon["names"]["English"]

        file.write("}\n")



# Pokedex
def gen_dex_dict():
    url = base_url + ".json"
    response = requests.get(url)
    data = response.json()

    with open("./assets/pokemon-reg.py", "w") as file:
        file.write("pokemon = {\n")

        for pokemon in data:
            if pokemon["stats"]:
                name   = pokemon["names"]["English"]
                number = pokemon["dexNr"]
                type1  = pokemon["primaryType"]["names"]["English"]
                type2  = pokemon["secondaryType"]["names"]["English"] if pokemon["secondaryType"] else "null"
                stats  = pokemon["stats"]

                fast_moves = [
                    pokemon["quickMoves"][move]["names"]["English"]
                    for move in pokemon["quickMoves"]
                ] + [
                    pokemon["eliteQuickMoves"][move]["names"]["English"]
                    for move in pokemon["eliteQuickMoves"]
                ]

                charged_moves = [
                    pokemon["cinematicMoves"][move]["names"]["English"]
                    for move in pokemon["cinematicMoves"]
                ] + [
                    pokemon["eliteCinematicMoves"][move]["names"]["English"]
                    for move in pokemon["eliteCinematicMoves"]
                ]


                file.write(f'\t"{name}": {{\n')
                file.write(f'\t\t"number": "{number}",\n')
                file.write(f'\t\t"type": ["{type1}", "{type2}"],\n')
                file.write(f'\t\t"stats": {{"attack": {stats["attack"]}, "defense": {stats["defense"]}, "hp": {stats["stamina"]}}},\n')
                file.write(f'\t\t"max_cp": {formulas.calc_max_cp(stats["attack"], stats["defense"], stats["stamina"])},\n')
                file.write(f'\t\t"fast_moves": {fast_moves},\n')
                file.write(f'\t\t"charged_moves": {charged_moves},\n')
                file.write(f'\t\t"image": "./assets/sprites/{number}.png"\n')
                file.write('\t},\n')

                for regional in pokemon["regionForms"]:
                    for region in regions:
                        if region in regional:
                            name   = pokemon["regionForms"][regional]["names"]["English"]
                            type1  = pokemon["regionForms"][regional]["primaryType"]["names"]["English"]
                            type2  = pokemon["regionForms"][regional]["secondaryType"]["names"]["English"] if pokemon["regionForms"][regional]["secondaryType"] else "null"
                            stats  = pokemon["regionForms"][regional]["stats"]

                            fast_moves = [
                                pokemon["regionForms"][regional]["quickMoves"][move]["names"]["English"]
                                for move in pokemon["regionForms"][regional]["quickMoves"]
                            ] + [
                                pokemon["regionForms"][regional]["eliteQuickMoves"][move]["names"]["English"]
                                for move in pokemon["regionForms"][regional]["eliteQuickMoves"]
                            ]

                            charged_moves = [
                                pokemon["regionForms"][regional]["cinematicMoves"][move]["names"]["English"]
                                for move in pokemon["regionForms"][regional]["cinematicMoves"]
                            ] + [
                                pokemon["regionForms"][regional]["eliteCinematicMoves"][move]["names"]["English"]
                                for move in pokemon["regionForms"][regional]["eliteCinematicMoves"]
                            ]

                            

                            file.write(f'\t"{name}": {{\n')
                            file.write(f'\t\t"number": "{number}",\n')
                            file.write(f'\t\t"type": ["{type1}", "{type2}"],\n')
                            file.write(f'\t\t"stats": {{"attack": {stats["attack"]}, "defense": {stats["defense"]}, "hp": {stats["stamina"]}}},\n')
                            file.write(f'\t\t"max_cp": {formulas.calc_max_cp(stats["attack"], stats["defense"], stats["stamina"])},\n')
                            file.write(f'\t\t"fast_moves": {fast_moves},\n')
                            file.write(f'\t\t"charged_moves": {charged_moves},\n')
                            file.write(f'\t\t"image": "./assets/sprites/{number}-{region.lower()}.png"\n')
                            file.write('\t},\n')


        file.write("}\n")



# gen_mega_dict()
gen_dex_dict()
