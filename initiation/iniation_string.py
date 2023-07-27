Bien sûr! Voici une série d'exercices sur les chaînes de caractères en Python, accompagnés de leurs corrections :

Exercice 1:
Écrivez un programme qui demande à l'utilisateur de saisir une phrase et affiche le nombre de caractères de cette phrase (en comptant les espaces).

```python
def main():
    phrase = input("Entrez une phrase : ")
    char_count = len(phrase)
    print("Nombre de caractères dans la phrase :", char_count)

if __name__ == "__main__":
    main()
```

Exercice 2:
Écrivez une fonction qui prend une chaîne de caractères en entrée et renvoie cette chaîne inversée.

```python
def reverse_string(input_str):
    return input_str[::-1]

# Exemple d'utilisation de la fonction :
string = "Hello, World!"
print("Chaîne inversée :", reverse_string(string))
```

Exercice 3:
Écrivez une fonction qui prend une chaîne de caractères en entrée et renvoie le nombre de mots dans cette chaîne (un mot est séparé par un espace).

```python
def count_words(input_str):
    words = input_str.split()
    return len(words)

# Exemple d'utilisation de la fonction :
string = "Bonjour tout le monde"
print("Nombre de mots :", count_words(string))
```

Exercice 4:
Écrivez une fonction qui prend une chaîne de caractères en entrée et renvoie une nouvelle chaîne où chaque mot est en majuscules.

```python
def capitalize_words(input_str):
    words = input_str.split()
    capitalized_words = [word.upper() for word in words]
    return ' '.join(capitalized_words)

# Exemple d'utilisation de la fonction :
string = "bienvenue dans le monde Python"
print("Mots en majuscules :", capitalize_words(string))
```

Exercice 5:
Écrivez une fonction qui prend une chaîne de caractères en entrée et renvoie True si cette chaîne est un palindrome (c'est-à-dire qu'elle se lit de la même manière de gauche à droite et de droite à gauche), sinon renvoie False.

```python
def is_palindrome(input_str):
    cleaned_str = ''.join(c.lower() for c in input_str if c.isalnum())
    return cleaned_str == cleaned_str[::-1]

# Exemple d'utilisation de la fonction :
string = "radar"
print("Est-ce un palindrome ?", is_palindrome(string))
```

Ces exercices sur les chaînes de caractères permettront aux apprenants de se familiariser avec les manipulations basiques des chaînes en Python et de renforcer leur compréhension de ce type de données. Les corrections sont fournies pour chaque exercice, ce qui permettra aux apprenants de vérifier leurs réponses et d'apprendre de nouvelles techniques.