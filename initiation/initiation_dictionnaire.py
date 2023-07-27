Bien sûr! Voici une série d'exercices sur les dictionnaires en Python, accompagnés de leurs corrections :

Exercice 1:
Écrivez un programme qui demande à l'utilisateur de saisir le nom et l'âge de cinq personnes, puis stocke ces informations dans un dictionnaire où le nom est la clé et l'âge est la valeur. Ensuite, affichez le dictionnaire complet.

```python
def main():
    people = {}
    for i in range(5):
        name = input("Entrez le nom de la personne : ")
        age = int(input("Entrez l'âge de la personne : "))
        people[name] = age

    print("Dictionnaire des personnes :", people)

if __name__ == "__main__":
    main()
```

Exercice 2:
Écrivez une fonction qui prend une liste de mots en entrée et renvoie un dictionnaire où chaque mot est la clé et la valeur est le nombre de fois où le mot apparaît dans la liste.

```python
def word_frequency(words):
    freq_dict = {}
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    return freq_dict

# Exemple d'utilisation de la fonction :
word_list = ["apple", "banana", "cherry", "apple", "banana", "apple"]
print("Fréquence des mots :", word_frequency(word_list))
```

Exercice 3:
Écrivez une fonction qui prend un dictionnaire en entrée (où les clés sont des noms et les valeurs sont des âges) et renvoie le nom de la personne la plus âgée.

```python
def oldest_person(people):
    if not people:
        return None

    max_age = max(people.values())
    oldest_persons = [name for name, age in people.items() if age == max_age]
    return oldest_persons

# Exemple d'utilisation de la fonction :
people = {"Alice": 30, "Bob": 25, "Charlie": 30, "David": 28}
print("Personnes les plus âgées :", oldest_person(people))
```

Exercice 4:
Écrivez une fonction qui prend une liste de dictionnaires (chaque dictionnaire représente une personne avec des clés "nom" et "âge") et renvoie une nouvelle liste contenant les noms des personnes dont l'âge est supérieur à 25.

```python
def filter_people_by_age(people_list, min_age):
    filtered_list = [person["nom"] for person in people_list if person["âge"] > min_age]
    return filtered_list

# Exemple d'utilisation de la fonction :
people_list = [
    {"nom": "Alice", "âge": 30},
    {"nom": "Bob", "âge": 25},
    {"nom": "Charlie", "âge": 28},
    {"nom": "David", "âge": 22}
]
print("Personnes dont l'âge est supérieur à 25 :", filter_people_by_age(people_list, 25))
```

Ces exercices sur les dictionnaires en Python permettront aux apprenants de se familiariser avec ce type de données et de renforcer leur compréhension des clés, des valeurs et des opérations courantes associées aux dictionnaires. Les corrections sont fournies pour chaque exercice, ce qui permettra aux apprenants de vérifier leurs résultats et de comprendre les solutions proposées.