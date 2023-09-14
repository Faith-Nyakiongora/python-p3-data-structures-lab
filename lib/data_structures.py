spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    return [value["name"] for value in spicy_foods]


def get_spiciest_foods(spicy_foods):
    return [value for value in spicy_foods if value["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
    for value in spicy_foods:
        print(
            f'{value["name"]} ({value["cuisine"]}) | Heat Level: {"🌶" * value["heat_level"]}'
        )


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for value in spicy_foods:
        if value["cuisine"] == cuisine:
            return value


def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)


def get_average_heat_level(spicy_foods):
    return sum([value["heat_level"] for value in spicy_foods]) / len(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
