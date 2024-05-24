import math

# Calculates the max cp of a pokemon given its base stats, assumes lvl 50 and 100% ivs
def calc_max_cp(attack, defense, hp):
    cpm = 0.84029999 # lvl 50 cpm, at lvl 40 = 0.7903
    cp = ((attack + 15) * pow(defense + 15, 0.5) * pow(hp + 15, 0.5) * pow(cpm, 2)) / 10
    return math.floor(max(10, cp))



def calc_best_moveset():
    return



def calc_damage_values(pokemon):
    return




##print(calc_max_cp(198,189,190))