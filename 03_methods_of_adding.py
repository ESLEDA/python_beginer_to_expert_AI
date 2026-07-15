list_of_water_pokemons = [
    "Greninja",
    "Kyogre",
    "Gyarados",
    "Suicune",
    "Kingdra"
]

list_of_fire_pokemons = [
    "Ponyta",
    "Torkoal",
    "Magcargo",
    "Arcanine",
    "Charizard"
]

pokemon_list = []


print(list_of_fire_pokemons)


#append
list_of_fire_pokemons.append("Cyndaquil")

#insert
list_of_fire_pokemons.insert(1, "Moltres")

print(list_of_fire_pokemons)


#extend
pokemon_list.extend(list_of_water_pokemons + list_of_fire_pokemons)

print(pokemon_list)
