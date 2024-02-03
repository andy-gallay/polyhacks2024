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
                    if ((ing.lower() in ingredient.lower()) and (int(measure[0:measure.find(" ")]))<=mes) :
                        test = True
    return test


# ID de la recette
meal_id = "52940"

# Obtenir les détails de la recette par ID
print(valid_ing(meal_id,"onion",2))
# Afficher les détails de la recette
