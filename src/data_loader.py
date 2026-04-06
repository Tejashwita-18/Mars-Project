import json

def load_planet_date():
    with open("../data/planets.json", "r") as file:
        data = json.load(file)

    return data
