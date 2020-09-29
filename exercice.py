#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:

    if values is None:
        # TODO: demander les valeurs ici
        # values = input("Entrer 10 valeurs, séparer les valeurs par des virgules").split(",")
        values = []
        while len(values) < 10:
            values.append(input("Entrer une valeur\n"))
        pass

    return sorted(values)


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        values = []
        while len(values) < 2:
            values.append(input("Entrer un mot\n"))
        pass
        words = values

    if len(words[0]) != len(words[1]):
        return False

    for lettre in words[0]:
        if lettre not in words[1]:
            return False

    return True


def contains_doubles(items: list) -> bool:
    ensemble_items = {var for var in items}

    if len(ensemble_items) == len(items):
        return False
    return True


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne

    for nom, notes in student_grades.items():
        student_grades[nom] = int(sum(notes)/len(notes))

    # C'est avec cette méthode que je marche en C#
    meilleur_etudiant = max(student_grades, key=student_grades.get)

    return {meilleur_etudiant: student_grades[meilleur_etudiant]}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres

    dictionnaire_complet = {}

    for lettre in sentence:

        if lettre in dictionnaire_complet:
            dictionnaire_complet[lettre] = dictionnaire_complet[lettre] + 1
        else:
            dictionnaire_complet[lettre] = 1

        # Autre manière de le faire:
            # frequency[letter] = sentence.count(letter)

    plus_de_cinq = {}

    print(dictionnaire_complet)
    for lettre in dictionnaire_complet:
        if dictionnaire_complet[lettre] >= 5:
            plus_de_cinq[lettre] = dictionnaire_complet[lettre]

    # HAHAHAAHA DANS TA FACE LANGUAGE TYPÉ DYNAMIQUEMENT
    plus_de_cinq = sorted(plus_de_cinq, key=plus_de_cinq.get, reverse=True)

    for lettre in plus_de_cinq:
        print(lettre + " revient " + str(dictionnaire_complet[lettre]) + " fois.")

    return dictionnaire_complet


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    livre_de_recettes = {}
    nom_recette = input("Je veux ta recette. C'est quoi son nom?\n")

    if nom_recette not in livre_de_recettes:

        liste_ingredients = []
        dernier_ingredient = "De l'amour"

        while dernier_ingredient != "":
            dernier_ingredient = input("shoot un ingrédient! (Ou fais 'enter' si t'as fini)\n")

            if dernier_ingredient != "" :
                liste_ingredients.append(dernier_ingredient)

        livre_de_recettes[nom_recette] = liste_ingredients

    return livre_de_recettes


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    nom_recette = input("C'est quoi la recette que tu veux?\n")

    if nom_recette in ingredients :
        for elt in ingredients[nom_recette]:
            print(elt + "\n")

    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
