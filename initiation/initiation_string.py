#%% Écrivez un programme qui demande à l'utilisateur de saisir une phrase et affiche le nombre de caractères de cette phrase (en comptant les espaces).
def nombre_caract():
    phrase = input("Entrez une phrase : ")
    char_count = len(phrase)
    print("Nombre de caractères dans la phrase :", char_count)

nombre_caract()


#%% Écrivez une fonction qui prend une chaîne de caractères en entrée et renvoie cette chaîne inversée.
def reverse_string(input_str):
    return input_str[::-1]

# Exemple d'utilisation de la fonction :
string = "Hello, World!"
print("Chaîne inversée :", reverse_string(string))


#%% Écrivez une fonction qui prend une chaîne de caractères en entrée et renvoie le nombre de mots dans cette chaîne (un mot est séparé par un espace).
def count_words(input_str):
    words = input_str.split()
    return len(words)

# Exemple d'utilisation de la fonction :
string = "Bonjour tout le monde"
print("Nombre de mots :", count_words(string))


#%% Écrivez une fonction qui prend une chaîne de caractères en entrée et renvoie une nouvelle chaîne où chaque mot est en majuscules.
def capitalize_words(input_str):
    words = input_str.split()
    capitalized_words = [word.upper() for word in words]
    return ' '.join(capitalized_words)

# Exemple d'utilisation de la fonction :
string = "bienvenue dans le monde Python"
print("Mots en majuscules :", capitalize_words(string))

#%% Écrivez une fonction qui prend une chaîne de caractères en entrée et renvoie True si cette chaîne est un palindrome (c'est-à-dire qu'elle se lit de la même manière de gauche à droite et de droite à gauche), sinon renvoie False.
def is_palindrome(input_str):
    cleaned_str = ''.join(c.lower() for c in input_str if c.isalnum())
    return cleaned_str == cleaned_str[::-1]

# Exemple d'utilisation de la fonction :
string = "radar"
print("Est-ce un palindrome ?", is_palindrome(string))