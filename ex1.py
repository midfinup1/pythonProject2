import requests


def heroes(number_of_heroes: int):
    heroes_list = []
    for i in range(0, number_of_heroes):
        superhero = input('Введите имя супергероя: ')  # Thanos, Hulk, Captain America
        temp_list = []
        response = requests.get(
            f"https://superheroapi.com/api/2619421814940190/search/{superhero}",
            headers={"User-Agent": "Netology"})
        results = response.json()["results"]
        for result_list in results:
            if result_list['name'] == superhero:
                superhero_id = result_list['id']
        response = requests.get(f"https://superheroapi.com/api/2619421814940190/{superhero_id}/powerstats")
        results = response.json()["intelligence"]
        temp_list.append(superhero)
        temp_list.append(int(results))
        heroes_list.append(temp_list)
    intelligence = 0
    for hero in heroes_list:
        if hero[1] > intelligence:
            intelligence = hero[1]
            smartest_superhero = hero[0]
    return f'Самый умный герой: {smartest_superhero}'


print(heroes(3))
