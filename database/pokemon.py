pokemon = {
    1: {
        "name": "Bulbasaur",
        "type": ["Grass", "Poison"],
        "evolutions": [2],
        "mega": [],
        "stats": {"hp": 45, "attack": 49, "defense": 49, "speed": 45, "special_attack": 65, "special_defense": 65},
        "fast_moves": ["Tackle", "Vine Whip"],
        "charged_moves": ["Power Whip", "Seed Bomb", "Sludge Bomb"],
        "image": "./sprites/1.png"
    },
    2: {
        "name": "Ivysaur",
        "type": ["Grass", "Poison"],
        "evolutions": [3],
        "mega": [],
        "stats": {"hp": 60, "attack": 62, "defense": 63, "speed": 60, "special_attack": 80, "special_defense": 80},
        "fast_moves": ["Razor Leaf", "Vine Whip"],
        "charged_moves": ["Solar Beam", "Sludge Bomb", "Power Whip"],
        "image": "./sprites/2.png"
    },
    3: {
        "name": "Venusaur",
        "type": ["Grass", "Poison"],
        "evolutions": [],
        "mega": ["3-mega"],
        "stats": {"hp": 80, "attack": 82, "defense": 83, "speed": 80, "special_attack": 100, "special_defense": 100},
        "fast_moves": ["Razor Leaf", "Vine Whip"],
        "charged_moves": ["Solar Beam", "Sludge Bomb", "Petal Blizzard"],
        "image": "./sprites/3.png"
    },
    "3-mega": {
        "name": "Mega Venusaur",
        "type": ["Grass", "Poison"],
        "stats": {"hp": 80, "attack": 100, "defense": 123, "speed": 80, "special_attack": 122, "special_defense": 120},
        "fast_moves": ["Razor Leaf", "Vine Whip"],
        "charged_moves": ["Solar Beam", "Sludge Bomb", "Petal Blizzard"],
        "image": "./sprites/3-mega.png"
    },
    4: {
        "name": "Charmander",
        "type": ["Fire"],
        "evolutions": [5],
        "mega": [],
        "stats": {"hp": 39, "attack": 52, "defense": 43, "speed": 65, "special_attack": 60, "special_defense": 50},
        "fast_moves": ["Scratch", "Ember"],
        "charged_moves": ["Flamethrower", "Dragon Claw", "Fire Punch"],
        "image": "./sprites/4.png"
    },
    5: {
        "name": "Charmeleon",
        "type": ["Fire"],
        "evolutions": [6],
        "mega": [],
        "stats": {"hp": 58, "attack": 64, "defense": 58, "speed": 80, "special_attack": 80, "special_defense": 65},
        "fast_moves": ["Scratch", "Ember"],
        "charged_moves": ["Flamethrower", "Fire Punch", "Dragon Claw"],
        "image": "./sprites/5.png"
    },
    6: {
        "name": "Charizard",
        "type": ["Fire", "Flying"],
        "evolutions": [],
        "mega": ["6-mega-x", "6-mega-y"],
        "stats": {"hp": 78, "attack": 84, "defense": 78, "speed": 100, "special_attack": 109, "special_defense": 85},
        "fast_moves": ["Fire Spin", "Air Slash"],
        "charged_moves": ["Blast Burn", "Dragon Claw", "Overheat"],
        "image": "./sprites/6.png"
    },
    "6-mega-x": {
        "name": "Mega Charizard X",
        "type": ["Fire", "Dragon"],
        "stats": {"hp": 78, "attack": 130, "defense": 111, "speed": 100, "special_attack": 130, "special_defense": 85},
        "fast_moves": ["Fire Spin", "Dragon Breath"],
        "charged_moves": ["Blast Burn", "Dragon Claw", "Overheat"],
        "image": "./sprites/6-mega-x.png"
    },
    "6-mega-y": {
        "name": "Mega Charizard Y",
        "type": ["Fire", "Flying"],
        "stats": {"hp": 78, "attack": 104, "defense": 78, "speed": 100, "special_attack": 159, "special_defense": 115},
        "fast_moves": ["Fire Spin", "Air Slash"],
        "charged_moves": ["Blast Burn", "Dragon Claw", "Overheat"],
        "image": "./sprites/6-mega-y.png"
    },
    7: {
        "name": "Squirtle",
        "type": ["Water"],
        "evolutions": [8],
        "mega": [],
        "stats": {"hp": 44, "attack": 48, "defense": 65, "speed": 43, "special_attack": 50, "special_defense": 64},
        "fast_moves": ["Tackle", "Bubble"],
        "charged_moves": ["Aqua Tail", "Water Pulse", "Hydro Pump"],
        "image": "./sprites/7.png"
    },
    8: {
        "name": "Wartortle",
        "type": ["Water"],
        "evolutions": [9],
        "mega": [],
        "stats": {"hp": 59, "attack": 63, "defense": 80, "speed": 58, "special_attack": 65, "special_defense": 80},
        "fast_moves": ["Water Gun", "Bubble"],
        "charged_moves": ["Aqua Tail", "Hydro Pump", "Ice Beam"],
        "image": "./sprites/8.png"
    },
    9: {
        "name": "Blastoise",
        "type": ["Water"],
        "evolutions": [],
        "mega": ["9-mega"],
        "stats": {"hp": 79, "attack": 83, "defense": 100, "speed": 78, "special_attack": 85, "special_defense": 105},
        "fast_moves": ["Water Gun", "Bite"],
        "charged_moves": ["Hydro Cannon", "Ice Beam", "Skull Bash"],
        "image": "./sprites/9.png"
    },
    "9-mega": {
        "name": "Mega Blastoise",
        "type": ["Water"],
        "stats": {"hp": 79, "attack": 103, "defense": 120, "speed": 78, "special_attack": 135, "special_defense": 115},
        "fast_moves": ["Water Gun", "Bite"],
        "charged_moves": ["Hydro Cannon", "Ice Beam", "Skull Bash"],
        "image": "./sprites/9-mega.png"
    },
    10: {
        "name": "Caterpie",
        "type": ["Bug"],
        "evolutions": [11],
        "mega": [],
        "stats": {"hp": 45, "attack": 30, "defense": 35, "speed": 45, "special_attack": 20, "special_defense": 20},
        "fast_moves": ["Tackle", "Bug Bite"],
        "charged_moves": ["Struggle"],
        "image": "./sprites/10.png"
    }
}




print(pokemon[1]["image"])