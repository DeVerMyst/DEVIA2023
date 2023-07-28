#%% Écrivez un programme qui demande à l'utilisateur de saisir 5 nombres entiers, les stocke dans une liste, puis affiche la liste.
def maliste():
    numbers = []
    for i in range(5):
        num = int(input("Entrez un nombre entier : "))
        numbers.append(num)

    print("Liste des nombres saisis :", numbers)
maliste()

#%% Écrivez une fonction qui prend une liste de nombres en entrée et renvoie la somme de tous les éléments de la liste.
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Exemple d'utilisation de la fonction :
numbers = [1, 2, 3, 4, 5]
print("Somme des éléments de la liste :", sum_list(numbers))

#%% Écrivez une fonction qui prend une liste de mots en entrée et renvoie une nouvelle liste contenant la longueur de chaque mot.
def word_lengths(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths

# Exemple d'utilisation de la fonction :
words = ["apple", "banana", "cherry"]
print("Longueurs des mots :", word_lengths(words))

#%% Écrivez une fonction qui prend une liste de nombres en entrée et renvoie une nouvelle liste contenant uniquement les nombres pairs de la liste initiale.
def even_numbers(numbers):
    even_nums = []
    for num in numbers:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums

# Exemple d'utilisation de la fonction :
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Nombres pairs de la liste :", even_numbers(numbers))

#%% Écrivez un programme qui prend une liste de noms en entrée, les trie par ordre alphabétique et affiche la liste triée.
def trienom():
    names = input("Entrez les noms séparés par des espaces : ").split()
    sorted_names = sorted(names)
    print("Liste triée par ordre alphabétique :", sorted_names)

trienom()
