import os
import pypokedex

# Dictionary containing Pokémon names and their respective dex numbers

def rename_pokemon_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            try:
                name_parts = os.path.splitext(filename)[0].split('-')
                pokemon_name = name_parts[0].lower()
                print(pokemon_name)
                suffix = None

                # Check for suffixes to preserve
                for part in name_parts[1:]:
                    if part in ["gmax", "mega", "mega-x", "mega-y", "alola", "hisui", "galar", "galar-zen",
                                "eternamax", "therian", "burn", "chill", "douse", "shock", "origin",
                                "primal", "unbound", "resolute", "black", "white", "piroutte", "dawn",
                                "dusk", "n-f", "n-m", "pau", "pom-pom", "sensu", "sky", "rapid-strike-gmax",
                                "school", "crowned", "complete"]:
                        suffix = part

                # Get dex number
                dex_number = pypokedex.get(name=pokemon_name).dex
                if dex_number is not None:
                    new_filename = f"{dex_number}"
                    if suffix:
                        new_filename += f"-{suffix}"
                    new_filename += '.png'

                    # Rename file
                    os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
                    print(f"Renamed {filename} to {new_filename}")
                else:
                    print(f"Could not find dex number for {pokemon_name}")
            except:
                continue

# Replace 'directory_path' with the path to your directory containing PNG files
directory_path = '/Users/davisguest/Desktop/this_directory_here'
rename_pokemon_files(directory_path)