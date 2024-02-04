# Polyhacks Hackathon 2024 : Projet Ville de Développement Durable 

# Theme : Gaspillage Alimentaire

## Introduction

Ce projet vise à contribuer au développement durable en abordant le problème du gaspillage alimentaire. Nous avons développé une application web agissant comme un réfrigérateur virtuel, permettant aux utilisateurs de saisir les ingrédients dont ils disposent ainsi que leurs quantités. L'application renvoie ensuite une liste des meilleures recettes pouvant être préparées avec ces ingrédients, réduisant ainsi le besoin d'achats supplémentaires et favorisant l'utilisation des ressources existantes.

## Technologies Utilisées

### Backend

Le backend du projet est implémenté en Python avec une API qui est construite à partir de la base de données [TheMealDB](https://www.themealdb.com/api.php) pour récupérer les informations nécessaires sur les recettes.

#### Principales fonctionnalités :

- `get_recipe_by_id` : Récupère les détails d'une recette par son ID.
- `elements_plus_redondants` : Identifie et renvoie les éléments les plus fréquents dans une liste.
- `premier_float_avant_non_entier` : Extrait le premier nombre à virgule flottante d'une chaîne.
- `valid_ing` : Valide la compatibilité d'un ingrédient et de sa quantité pour une recette donnée.
- `search_recipes_by_ingredients` : Recherche des recettes en fonction d'une liste d'ingrédients et de leurs quantités.

### Frontend

Le frontend est construit avec HTML et CSS et React est utilisé comme bibliothèque principale pour la création de l'interface utilisateur.

#### Principaux composants :

- `IngredientsPicker` : Permet aux utilisateurs de saisir et de gérer les ingrédients.
- `RecipeFinder` : Lance la recherche de recettes en fonction des ingrédients saisis par l'utilisateur.

## Comment Utiliser

1. Clonez le dépôt : `git clone [url_du_dépôt]`
2. Installez les dépendances : `npm install` (pour le frontend) et `pip install -r requirements.txt` (pour le backend).
3. Lancez le backend : `python main.py`
4. Lancez le frontend : `npm start`
5. Accédez à l'application dans votre navigateur : `http://localhost:3000`

## Contributeurs

- Andy Gallay
- Louis Forrer
- Aziz Maaref
- Hazem Ben Amor
