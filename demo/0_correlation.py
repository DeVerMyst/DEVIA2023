import numpy as np
import matplotlib.pyplot as plt



def plot_scatter_with_correlation(x, y, text):
    fig, axes = plt.subplots(1,2, figsize=(20, 5))

    # Tracer un plot avec les données x et y
    axes[0].plot(x, label="X")
    axes[0].plot(y, label="Y")
    axes[0].legend()

    # Tracer un scatter plot avec les données x et y et le texte donné
    axes[1].scatter(x, y, label=text)
    axes[1].set_xlabel('X')
    axes[1].set_ylabel('Y')
    axes[1].set_title(text)
    axes[1].legend()

    plt.show()
    

# Générer des données aléatoires pour x et y avec une corrélation positive forte
np.random.seed(42)
x = np.random.rand(100) * 10
y = x + np.random.rand(100) * 3
plot_scatter_with_correlation(x, y, 'Corrélation positive forte')

# Générer des données aléatoires pour x et y avec une corrélation négative forte
np.random.seed(42)
x = np.random.rand(100) * 10
y = -x + np.random.rand(100) * 3
plot_scatter_with_correlation(x, y, 'Corrélation négative forte')

# Générer des données aléatoires pour x et y avec une corrélation faible (proche de zéro)
np.random.seed(42)
x = np.random.rand(100) * 10
y = np.random.rand(100) * 10
plot_scatter_with_correlation(x, y, 'Corrélation faible (proche de zéro)')

# Générer des données aléatoires pour x et y avec une corrélation nulle
np.random.seed(42)
x = np.random.rand(100) * 10
y = np.random.rand(100) * 2
plot_scatter_with_correlation(x, y, 'Corrélation nulle')

# Générer des données aléatoires pour x et y avec une corrélation non linéaire
np.random.seed(42)
x = np.random.rand(100) * 10
y = x**2 + np.random.rand(100) * 10
plot_scatter_with_correlation(x, y, 'Corrélation non linéaire')
