import requests

def search_recipes_by_ingredients(ingredients):
    # Base URL de l'API
    base_url = "https://www.themealdb.com/api/json/v1/1/filter.php"

    # Liste pour stocker les identifiants de recettes
    meal_ids = []

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
                if meal_id:
                    meal_ids.append(meal_id)

    return meal_ids

# Ingrédients de recherche
ingredients = ["chicken", "onion", "broccoli"]

# Rechercher les recettes par ingrédients
result = search_recipes_by_ingredients(ingredients)

# Afficher les identifiants de recettes trouvées
print("Identifiants de recettes trouvées:", result)
