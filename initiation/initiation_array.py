import numpy as np

#%%  Créez un tableau NumPy contenant les entiers de 1 à 10 (inclus).

arr = np.arange(1, 11)
print(arr)


#%%  Créez un tableau NumPy contenant 5 valeurs flottantes générées aléatoirement entre 0 et 1.

arr = np.random.rand(5)
print(arr)

#%%  Créez une fonction qui prend un tableau NumPy en entrée et renvoie la somme de ses éléments.

def sum_array(arr):
    return np.sum(arr)

arr = np.array([1, 2, 3, 4, 5])
print("Somme des éléments :", sum_array(arr))


#%%  Créez une fonction qui prend deux tableaux NumPy en entrée et renvoie le produit scalaire de ces deux tableaux (dot product).

def dot_product(arr1, arr2):
    return np.dot(arr1, arr2)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("Produit scalaire :", dot_product(arr1, arr2))


#%%  Créez une fonction qui prend un tableau NumPy en entrée et renvoie un nouveau tableau contenant uniquement les éléments uniques du tableau d'origine.

def unique_elements(arr):
    return np.unique(arr)

arr = np.array([1, 2, 2, 3, 3, 4, 5, 5])
print("Éléments uniques :", unique_elements(arr))


#%%  Créez une fonction qui prend un tableau NumPy en entrée et renvoie un nouveau tableau contenant les éléments triés par ordre croissant.

def sort_array(arr):
    return np.sort(arr)

arr = np.array([3, 1, 4, 2, 5])
print("Tableau trié :", sort_array(arr))


#%%  Créez une fonction qui prend un tableau NumPy en entrée et renvoie la moyenne, la médiane et l'écart type de ses éléments.

def array_stats(arr):
    mean = np.mean(arr)
    median = np.median(arr)
    std = np.std(arr)
    return mean, median, std

arr = np.array([1, 2, 3, 4, 5])
mean, median, std = array_stats(arr)
print("Moyenne :", mean)
print("Médiane :", median)
print("Écart type :", std)


#%%  Créez une fonction qui prend un tableau NumPy en entrée et renvoie un nouveau tableau où tous les éléments inférieurs à 5 sont remplacés par 0 et tous les éléments supérieurs ou égaux à 5 sont remplacés par 1.

def replace_values(arr):
    arr[arr < 5] = 0
    arr[arr >= 5] = 1
    return arr

arr = np.array([1, 6, 3, 8, 2, 4, 7, 9, 5])
print("Nouveau tableau :", replace_values(arr))


#%%  Créez une fonction qui prend un tableau NumPy de nombres entiers en entrée et renvoie un nouveau tableau contenant uniquement les nombres premiers du tableau d'origine.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(np.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers(arr):
    return arr[np.vectorize(is_prime)(arr)]

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Nombres premiers :", prime_numbers(arr))


#%%  Créez un tableau NumPy 2D de taille 3x3 contenant des valeurs entières générées aléatoirement entre 1 et 10.

arr = np.random.randint(1, 11, (3, 3))
print(arr)

