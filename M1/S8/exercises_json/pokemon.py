import json


def read_pokemons(path):
    pokemons_list = {}
    with open(path, "r", newline="") as file:
        pokemons_list = json.load(file)
    return pokemons_list


def input_pokemon():
    pokemon_skills = {
        "name":{},
        "base":{}
    }
    try:
        #Input name
        name_pokemon = input("Ingrese el pokemon: ")
        pokemon_skills["name"]["english"] = name_pokemon
        #Input type
        type_pokemon = input("Ingrese el tipo del pokemon: ")
        pokemon_skills["type"] = type_pokemon
        #Input hp
        hp_pokemon = int(input("Ingrese la vida del pokemon: "))
        pokemon_skills["base"]["HP"] = hp_pokemon
        #Input attack
        attack_pokemon = int(input("Ingrese el ataque del pokemon: "))
        pokemon_skills["base"]["Attack"] = attack_pokemon
        #Input defence
        defense_pokemon = int(input("Ingrese la defensa del pokemon: "))
        pokemon_skills["base"]["Defense"] = defense_pokemon
        #Input Sp. attack
        sp_attack_pokemon = int(input("Ingrese el Sp. ataque del pokemon: "))
        pokemon_skills["base"]["Sp. Attack"] = sp_attack_pokemon
        #Input Sp. defence
        sp_defense_pokemon = int(input("Ingrese el Sp. defensa del pokemon: "))
        pokemon_skills["base"]["Sp. Defense"] = sp_defense_pokemon
        #Input speed
        speed_pokemon = int(input("Ingrese la velocidad del pokemon: "))
        pokemon_skills["base"]["Speed"] = speed_pokemon
        return pokemon_skills
    except ValueError as error:
        print(f"Error, valor no valido: {error}")


def save_pokemons(path, pokemon_skills, pokemons_list): 
    pokemons_list.append(pokemon_skills)
    with open(path, "w", encoding="UTF-8") as file:
        json.dump(pokemons_list, file, indent=4)
    

def main():
    try:
        pokemons_list = read_pokemons("pokemons.json")
        pokemon_skills = input_pokemon()
        save_pokemons("pokemons.json", pokemon_skills, pokemons_list)
    except Exception as error:
        print(f"Ha ocurrido un error inesperado: {error}")


if __name__ == "__main__":
    main()