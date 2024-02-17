from collections import defaultdict
from operator import itemgetter

def cookbook(*recipes):
    cuisines = defaultdict(list)

    for recipe in recipes:
        name, cuisine, ingredients = recipe

        cuisines[cuisine].append((name, ingredients))

    sorted_cuisines = []

    for cuisine, recipes in cuisines.items():
        sorted_recipes = sorted(recipes, key=itemgetter(0))
        sorted_cuisines.append((cuisine, len(sorted_recipes), sorted_recipes))
    sorted_cuisines.sort(key=lambda x: (-x[1], x[0]))

    output = ""

    for cuisine, count, recipes in sorted_cuisines:
        output += f"{cuisine} cuisine contains {count} recipes:\n"

        for name, ingredients in recipes:
            output += f"  * {name} -> Ingredients: {', '.join(ingredients)}\n"

    return output

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))

