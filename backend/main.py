import requests
def valid_ing(meal_id,ing,mes):
    # URL de l'API
    url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}"

    # Faire la requête GET
    response = requests.get(url)

    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Extraire les données JSON de la réponse
        data = response.json()

        # Extraire les détails de la recette de la réponse
        meals = data.get("meals", [])
        if meals:
            if meals[0]:
                test=False
                for i in range(1, 21):
                    ingredient_key = f"strIngredient{i}"
                    measure_key = f"strMeasure{i}"
                    ingredient = meals[0].get(ingredient_key)
                    measure = meals[0].get(measure_key)
                    print(measure)
                    if ((ing.lower() in ingredient.lower()) and (int(measure[0:measure.find(" ")]))<=mes) :
                        test = True
    return test


def search_recipes_by_ingredients(ingredients,measures):
    # Base URL de l'API
    base_url = "https://www.themealdb.com/api/json/v1/1/filter.php"

    # Liste pour stocker les identifiants de recettes
    meal_ids = []
    i=0
    # Parcourir chaque ingrédient
    for ingredient in ingredients:
        # Paramètres de la requête
        params = {"i": ingredient}

        # Faire la requête GET
        response = requests.get(base_url, params=params)

        # Vérifier si la requête a réussi
        if response.status_code == 200:
            # Extraire les données JSON de la réponse
            data = response.json()

            # Extraire les identifiants de recettes de la réponse
            meals = data.get("meals", [])
            for meal in meals:
                meal_id = meal.get("idMeal")
                if meal_id and valid_ing(meal_id,ingredient,measures[i]) :
                    meal_ids.append(meal_id)
                    print(meal_ids)
    i+=1
    return meal_ids

# Ingrédients de recherche
ingredients = ["chicken", "onion", "broccoli"]
measures=[1,2,3]

# Rechercher les recettes par ingrédients
result = search_recipes_by_ingredients(ingredients,measures)


# Afficher les identifiants de recettes trouvées
print("Identifiants de recettes trouvées:", result)

