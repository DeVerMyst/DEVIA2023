import numpy as np
import matplotlib.pyplot as plt

#%% Tracer un graphe linéaire des points (x, y) où x = [0, 1, 2, 3, 4] et y = [1, 4, 3, 8, 5].

x = [0, 1, 2, 3, 4]
y = [1, 4, 3, 8, 5]

plt.figure()
plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graphe linéaire')
plt.show()


#%% Tracer un histogramme à partir de données aléatoires générées par NumPy.

# Générer des données aléatoires
data = np.random.normal(loc=0, scale=1, size=100)

plt.figure()
plt.hist(data, bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Valeurs')
plt.ylabel('Fréquence')
plt.title('Histogramme')
plt.show()


#%% Tracer un diagramme à barres à partir des données suivantes : 

categories = ['A', 'B', 'C', 'D', 'E']
valeurs = [25, 30, 15, 20, 10]

plt.figure()
plt.bar(categories, valeurs, color='lightgreen')
plt.xlabel('Catégories')
plt.ylabel('Valeurs')
plt.title('Diagramme à barres')
plt.show()


#%% Tracer un nuage de points à partir de données aléatoires générées par NumPy.

# Générer des données aléatoires
x = np.random.normal(loc=0, scale=1, size=50)
y = np.random.normal(loc=0, scale=1, size=50)

plt.figure()
plt.scatter(x, y, color='orange', marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Nuage de points')
plt.show()


#%% Tracer une courbe sinusoïdale en utilisant NumPy.

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.figure()
plt.plot(x, y, color='purple')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Courbe sinusoïdale')
plt.show()


#%% Tracer deux courbes sur le même graphe à partir des données suivantes :

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure()
plt.plot(x, y1, color='blue', label='Sin(x)')
plt.plot(x, y2, color='red', label='Cos(x)')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Courbes Sin(x) et Cos(x)')
plt.legend()
plt.show()


#%% Tracer un diagramme en secteurs (camembert) à partir des données suivantes :

categories = ['A', 'B', 'C', 'D']
valeurs = [30, 25, 15, 20]

plt.figure()
plt.pie(valeurs, labels=categories, autopct='%1.1f%%', colors=['blue', 'green', 'purple', 'orange'])
plt.title('Diagramme en secteurs')
plt.show()


#%% Tracer une courbe polynomiale à partir des données suivantes :

x = np.linspace(-5, 5, 100)
y = 3 * x**3 + 2 * x**2 - 8 * x + 5

plt.figure()
plt.plot(x, y, color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Courbe polynomiale')
plt.show()


#%% Tracer un diagramme en barres empilées à partir des données suivantes :

categories = ['A', 'B', 'C', 'D']
valeurs1 = [10, 15, 20, 25]
valeurs2 = [5, 10, 15, 20]

plt.figure()
plt.bar(categories, valeurs1, label='Valeurs 1', color='lightblue')
plt.bar(categories, valeurs2, bottom=valeurs1, label='Valeurs 2', color='orange')
plt.xlabel('Catégories')
plt.ylabel('Valeurs')
plt.title('Diagramme en barres empilées')
plt.legend()
plt.show()


#%% Tracer un graphique en boîte (boxplot) à partir des données suivantes :

data = [np.random.normal(0, 1, 100), np.random.normal(2, 1, 100), np.random.normal(-3, 2, 100)]

plt.figure()
plt.boxplot(data, labels=['Groupe 1', 'Groupe 2', 'Groupe 3'], notch=True, patch_artist=True)
plt.xlabel('Groupes')
plt.ylabel('Valeurs')
plt.title('Graphique en boîte')
plt.show()