import numpy as np
import matplotlib.pyplot as plt

def tracer_spirale(a, b, theta_max):
    theta = np.linspace(0, theta_max, 1000)  # Créer des valeurs d'angle de 0 à theta_max
    r = a + b * theta  # Équation polaire pour une spirale
    x = r * np.cos(theta)  # Coordonnées x en fonction de r et de l'angle
    y = r * np.sin(theta)  # Coordonnées y en fonction de r et de l'angle
    
    plt.figure(figsize=(6, 6))  # Crée une figure
    plt.plot(x, y, label='Spirale')  # Trace la spirale
    plt.xlabel('X')  # Étiquette de l'axe des x
    plt.ylabel('Y')  # Étiquette de l'axe des y
    plt.title('Tracé d\'une Spirale')  # Titre du graphique
    plt.legend()  # Affiche la légende
    plt.grid(True)  # Affiche la grille
    plt.axis('equal')  # Pour que les échelles des axes x et y soient égales
    plt.show()  # Affiche le graphique

# Appel de la fonction pour tracer une spirale avec a=0.1, b=0.02 et theta_max=10
tracer_spirale(0, 0.02, 10)
