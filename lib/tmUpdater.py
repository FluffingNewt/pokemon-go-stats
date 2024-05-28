import requests
#from lib import formulas

base_url = "https://pogoapi.net/api/v1/"

class Move:
    def __init__(self, move_dict):
        self.name         = move_dict["name"]
        self.type         = move_dict["type"]
        self.pwr          = move_dict["power"]
        self.duration     = move_dict["duration"]
        self.energy_delta = move_dict["energy_delta"]
        self.image        = f'"./assets/types/{self.type}.png"'



def write_move_data(file, move):
    text = (
        f'\t"{move.name}": {{\n'
        f'\t\t"type": "{move.type}",\n'
        f'\t\t"pwr": {move.pwr},\n'
        f'\t\t"energy_delta": {move.energy_delta},\n'
        f'\t\t"duration": {move.duration},\n'
        f'\t\t"image": {move.image}\n'
    )
    file.write(text)



def gen_pve_move_dict():
    # Checks to see if there API is up before overwriting files
    try:
        url = f"{base_url}fast_moves.json"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return


    with open("./assets/fast_moves_pve.json", "w",encoding='utf-8') as file:
        file.write("{\n")
        index = 0
        for fast_move in data:
            fast_obj = Move(fast_move)
            write_move_data(file, fast_obj)
            if index != len(data) - 1: file.write(f'\t}},\n')
            else: file.write(f'\t}}\n')
            index += 1
        file.write("}\n")

    with open("./assets/charged_moves_pve.json", "w",encoding='utf-8') as file:
        url = f"{base_url}charged_moves.json"
        response = requests.get(url)
        data = response.json()
        
        file.write("{\n")
        index = 0
        for charged_move in data:
            charged_obj = Move(charged_move)
            write_move_data(file, charged_obj)
            if index != len(data) - 1: file.write(f'\t}},\n')
            else: file.write(f'\t}}\n')
            index += 1
        file.write("}\n")


gen_pve_move_dict()