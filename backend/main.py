import requests

def premier_float_avant_non_entier(chaine):
    partie_float_avant_non_entier = ""
    decimal_trouve = False

    for caractere in chaine:
        if caractere.isdigit() or caractere == '.':
            partie_float_avant_non_entier += caractere

            if caractere == '.':
                # Vérifier s'il y a déjà un point décimal dans la partie_float_avant_non_entier
                if decimal_trouve:
                    break  # Si oui, sortir de la boucle
                else:
                    decimal_trouve = True

        elif partie_float_avant_non_entier:
            break  # Sortir de la boucle dès qu'un non-entier est rencontré après la partie float

    # Convertir la chaîne en un nombre à virgule flottante
    nombre_float = partie_float_avant_non_entier

    return nombre_float
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
                    if ingredient and measure:
                        if "½" in measure:
                            measure = measure.replace("½", "0.5")
                        if (ing.lower() in ingredient.lower()) :
                            if premier_float_avant_non_entier(measure) == "":
                                test=True
                                continue
                            elif (float(premier_float_avant_non_entier(measure)))<=mes:
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
                    
    i+=1
    return meal_ids

# Ingrédients de recherche
ingredients = ["chicken", "onion", "broccoli"]
measures=[1,2,3]

# Rechercher les recettes par ingrédients
result = search_recipes_by_ingredients(ingredients,measures)


# Afficher les identifiants de recettes trouvées
print("Identifiants de recettes trouvées:", result)

