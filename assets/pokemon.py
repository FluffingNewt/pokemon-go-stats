import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lib import formulas

pokemon = {
    1: {
        "name": "Bulbasaur",
        "type": ["Grass", "Poison"],
        "mega": [],
        "shadow": True,
        "stats": {"attack": 118, "defense": 111, "hp": 128},
        "max_cp": formulas.calc_max_cp(118, 111, 128),
        "fast_moves": ["Vine Whip"],
        "charged_moves": ["Power Whip", "Sludge Bomb"],
        "image": ".asstes/sprites/1.png"
    },
    2: {
        "name": "Ivysaur",
        "type": ["Grass", "Poison"],
        "mega": [],
        "shadow": True,
        "stats": {"attack": 151, "defense": 143, "hp": 155},
        "max_cp": formulas.calc_max_cp(151, 143, 155),
        "fast_moves": ["Vine Whip"],
        "charged_moves": ["Power Whip", "Sludge Bomb", "Solar Beam"],
        "image": ".asstes/sprites/2.png"
    },
    3: {
        "name": "Venusaur",
        "type": ["Grass", "Poison"],
        "mega": ["3-mega"],
        "shadow": True,
        "stats": {"attack": 198, "defense": 189, "hp": 190},
        "max_cp": formulas.calc_max_cp(198, 189, 190),
        "fast_moves": ["Vine Whip"],
        "charged_moves": ["Petal Blizzard", "Sludge Bomb", "Solar Beam"],
        "image": ".asstes/sprites/3.png"
    },
    "3-mega": {
        "name": "Mega Venusaur",
        "type": ["Grass", "Poison"],
        "stats": {"attack": 241, "defense": 246, "hp": 190},
        "max_cp": formulas.calc_max_cp(241, 246, 190),
        "fast_moves": ["Vine Whip"],
        "charged_moves": ["Petal Blizzard", "Sludge Bomb", "Solar Beam"],
        "image": ".asstes/sprites/3-mega.png"
    }
}



print(pokemon["3-mega"]["max_cp"])