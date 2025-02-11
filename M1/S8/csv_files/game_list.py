import csv


def input_game():
    games_list = []
    try:
        number_games = int(input("Ingrese la cantidad de juegos: "))
        if number_games <= 0:
            raise ValueError
        for i in range(number_games):
            game_diccionary = {}
            #Input name
            game_name = input("Ingrese el nombre del juego: ")
            game_diccionary['name'] = game_name
            #Input gender
            game_gender = input("Ingrese el genero del juego: ")
            game_diccionary['gender'] = game_gender
            #Input developer
            game_developer = input("Ingrese la desarrolladora del juego: ")
            game_diccionary['developer'] = game_developer
            #Input ESRB
            game_esrb = input("Ingrese la clasificacion ESRB del juego: ")
            game_diccionary['esrb'] = game_esrb
            games_list.append(game_diccionary)
        return games_list
    except ValueError as error:
        print(f"Error inesperado en input_game: {error}")


def write_csv(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)


def main():
    try:
        games_list = input_game()
        
        write_csv("data_games.csv", games_list, games_list[0].keys())
        
    except Exception as error:
        print(f"Error, ha ocurrido un error inesperado: {error}")


if __name__ == "__main__":
    main()