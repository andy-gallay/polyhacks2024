import requests
from collections import Counter

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
            if meals[0]:
                recipe_details = {
                    "Nom": meals[0]["strMeal"],
                    "Catégorie": meals[0]["strCategory"],
                    "Région": meals[0]["strArea"],
                    "Instructions": meals[0]["strInstructions"],
                    "Ingrédients": []
                }
                for i in range(1, 21):
                    ingredient_key = f"strIngredient{i}"
                    measure_key = f"strMeasure{i}"
                    ingredient = meals[0].get(ingredient_key)
                    measure = meals[0].get(measure_key)
                    if ingredient and measure:
                        recipe_details["Ingrédients"].append(f"- {measure.strip()} {ingredient.strip()}")
                recipe_details["Image de la recette"] = meals[0]["strMealThumb"]
                recipe_details["Source"] = meals[0]["strSource"]
                return recipe_details
    return None
def elements_plus_redondants(liste):
    occurrences = Counter(liste)
    max_occurrences = max(occurrences.values())
    redondants = [element for element, occurrence in occurrences.items() if occurrence == max_occurrences]

    return redondants
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
        nbing=0
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
                        nbing+=1
                        if "½" in measure:
                            measure = measure.replace("½", "0.5")
                        if (ing.lower() in ingredient.lower()) :
                            if premier_float_avant_non_entier(measure) == "":
                                test=True
                                continue
                            elif (float(premier_float_avant_non_entier(measure)))<=mes:
                                test = True
    return test,nbing

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
            data = response.json()
            meals = data.get("meals", [])
            for meal in meals:
                meal_id = meal.get("idMeal")
                if meal_id and valid_ing(meal_id,ingredient,measures[i])[0] :
                    meal_ids.append(meal_id)
                    print(meal_id)
                    if len(meal_ids) >= 30:
                        break
        i+=1
    return meal_ids

# Ingrédients et mesures de recherche
ingredients = ["chicken", "onion", "garlic", "tomato"]
measures=[1,2,3,2]
result = search_recipes_by_ingredients(ingredients,measures)
list=[]
for i in elements_plus_redondants(result):
    list.append(get_recipe_by_id(i))
print(list)


