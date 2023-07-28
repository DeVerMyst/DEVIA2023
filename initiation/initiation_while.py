#%% Écrivez un programme qui demande à l'utilisateur de deviner un nombre secret (par exemple 42). Le programme indique à l'utilisateur si le nombre à deviner est plus grand ou plus petit que sa proposition et continue de demander un nombre tant que l'utilisateur ne trouve pas le nombre secret. Une fois que l'utilisateur trouve le nombre secret, affichez un message de félicitations.
def guess():
    secret_number = 42
    guessed = False

    while not guessed:
        guess = int(input("Devinez le nombre secret : "))
        if guess == secret_number:
            print("Félicitations ! Vous avez trouvé le nombre secret.")
            guessed = True
        elif guess < secret_number:
            print("Le nombre secret est plus grand.")
        else:
            print("Le nombre secret est plus petit.")

guess()

#%% Écrivez une fonction qui prend un nombre entier en entrée et affiche tous les nombres de 1 jusqu'à ce nombre (inclus) en utilisant une boucle "while".
def print_numbers(n):
    i = 1
    while i <= n:
        print(i)
        i += 1

# Exemple d'utilisation de la fonction :
num = int(input("Entrez un nombre entier : "))
print_numbers(num)

#%% Écrivez une fonction qui prend une liste de nombres en entrée et renvoie une nouvelle liste contenant uniquement les nombres positifs en utilisant une boucle "while".
def positive_numbers(numbers):
    positive_nums = []
    i = 0
    while i < len(numbers):
        if numbers[i] > 0:
            positive_nums.append(numbers[i])
        i += 1
    return positive_nums

# Exemple d'utilisation de la fonction :
numbers = [-2, 5, -8, 10, -3, 15]
print("Nombres positifs de la liste :", positive_numbers(numbers))

#%% Écrivez une fonction qui prend une liste de mots en entrée et renvoie une nouvelle liste contenant les mots dont la première lettre est une voyelle (a, e, i, o, u) en utilisant une boucle "while".
def filter_vowel_words(words):
    vowels = "aeiou"
    vowel_words = []
    i = 0
    while i < len(words):
        if words[i][0].lower() in vowels:
            vowel_words.append(words[i])
        i += 1
    return vowel_words

# Exemple d'utilisation de la fonction :
words = ["apple", "banana", "orange", "cherry", "umbrella"]
print("Mots commençant par une voyelle :", filter_vowel_words(words))

#%% Écrivez un programme qui demande à l'utilisateur de saisir un mot et affiche si ce mot contient plus de 5 caractères en utilisant une boucle "while".
def longueur():
    word = input("Entrez un mot : ")
    i = 0
    while i < len(word) and len(word) <= 5:
        print("Le mot ne contient pas plus de 5 caractères.")
        word = input("Entrez un autre mot : ")
    else:
        print("Le mot contient plus de 5 caractères.")

longueur()
