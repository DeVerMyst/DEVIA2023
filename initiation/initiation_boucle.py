#%% Écrivez un programme qui demande à l'utilisateur de saisir un nombre entier positif et affiche tous les nombres de 1 jusqu'à ce nombre (inclus).
def serie():
    n = int(input("Entrez un nombre entier positif : "))
    if n >= 0:
        for num in range(1, n + 1):
            print(num)
    else:
        print("Le nombre doit être positif.")

serie()


#%% Écrivez une fonction qui prend une liste de nombres en entrée et renvoie une nouvelle liste contenant uniquement les nombres positifs.
def positive_numbers(numbers):
    positive_nums = []
    for num in numbers:
        if num > 0:
            positive_nums.append(num)
    return positive_nums

# Exemple d'utilisation de la fonction :
numbers = [-2, 5, -8, 10, -3, 15]
print("Nombres positifs de la liste :", positive_numbers(numbers))


#%% Écrivez une fonction qui prend une liste de mots en entrée et renvoie une nouvelle liste contenant les mots dont la première lettre est une voyelle (a, e, i, o, u).
def filter_vowel_words(words):
    vowels = "aeiou"
    vowel_words = []
    for word in words:
        if word[0].lower() in vowels:
            vowel_words.append(word)
    return vowel_words

# Exemple d'utilisation de la fonction :
words = ["apple", "banana", "orange", "cherry", "umbrella"]
print("Mots commençant par une voyelle :", filter_vowel_words(words))


#%% Écrivez une fonction qui prend un nombre entier en entrée et affiche si ce nombre est positif, négatif ou nul.
def check_number_sign(number):
    if number > 0:
        print("Le nombre est positif.")
    elif number < 0:
        print("Le nombre est négatif.")
    else:
        print("Le nombre est nul.")

# Exemple d'utilisation de la fonction :
num = int(input("Entrez un nombre entier : "))
check_number_sign(num)


#%% Écrivez un programme qui demande à l'utilisateur de saisir un mot et affiche si ce mot contient plus de 5 caractères.
def signe():
    word = input("Entrez un mot : ")
    if len(word) > 5:
        print("Le mot contient plus de 5 caractères.")
    else:
        print("Le mot ne contient pas plus de 5 caractères.")

signe()
