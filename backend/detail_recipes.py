import requests
def get_recipe_by_id(meal_id):
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
            return meals[0]

    return None

# ID de la recette
meal_id = "52940"

# Obtenir les détails de la recette par ID
recipe = get_recipe_by_id(meal_id)

# Afficher les détails de la recette
if recipe:
    print("Détails de la recette:")
    print("Nom:", recipe["strMeal"])
    print("Catégorie:", recipe["strCategory"])
    print("Région:", recipe["strArea"])
    print("Instructions:", recipe["strInstructions"])
    print("Ingrédients:")
    for i in range(1, 21):
        ingredient_key = f"strIngredient{i}"
        measure_key = f"strMeasure{i}"
        ingredient = recipe.get(ingredient_key)
        measure = recipe.get(measure_key)
        if ingredient and measure:
            print(f"- {measure.strip()} {ingredient.strip()}")
    print("Image de la recette:", recipe["strMealThumb"])
    print("Source:", recipe["strSource"])
else:
    print("Aucune recette trouvée avec cet ID.")