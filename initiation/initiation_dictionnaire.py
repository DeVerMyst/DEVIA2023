#%% Écrivez un programme qui demande à l'utilisateur de saisir le nom et l'âge de cinq personnes, puis stocke ces informations dans un dictionnaire où le nom est la clé et l'âge est la valeur. Ensuite, affichez le dictionnaire complet.
def nom_age():
    people = {}
    for i in range(5):
        name = input("Entrez le nom de la personne : ")
        age = int(input("Entrez l'âge de la personne : "))
        people[name] = age

    print("Dictionnaire des personnes :", people)

nom_age()


#%% Écrivez une fonction qui prend une liste de mots en entrée et renvoie un dictionnaire où chaque mot est la clé et la valeur est le nombre de fois où le mot apparaît dans la liste.
def word_frequency(words):
    freq_dict = {}
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    return freq_dict

# Exemple d'utilisation de la fonction :
word_list = ["apple", "banana", "cherry", "apple", "banana", "apple"]
print("Fréquence des mots :", word_frequency(word_list))


#%% Écrivez une fonction qui prend un dictionnaire en entrée (où les clés sont des noms et les valeurs sont des âges) et renvoie le nom de la personne la plus âgée.
def oldest_person(people):
    if not people:
        return None

    max_age = max(people.values())
    oldest_persons = [name for name, age in people.items() if age == max_age]
    return oldest_persons

# Exemple d'utilisation de la fonction :
people = {"Alice": 30, "Bob": 25, "Charlie": 30, "David": 28}
print("Personnes les plus âgées :", oldest_person(people))


#%% Écrivez une fonction qui prend une liste de dictionnaires (chaque dictionnaire représente une personne avec des clés "nom" et "âge") et renvoie une nouvelle liste contenant les noms des personnes dont l'âge est supérieur à 25.
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

