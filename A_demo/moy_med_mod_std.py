import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import statistics as st
def plot_stats(data, text, ax):

    # Création de l'histogramme des données
    n, bins, _ = ax.hist(data, bins=10, density=True, alpha=0.7, color='skyblue', label='Données')

    # Calcul des statistiques
    mean_value = np.mean(data)
    mode_value = bins[np.argmax(n)]  # Pour l'échantillon aléatoire, mode ≈ médiane
    median_value = np.median(data)
    std_value = np.std(data)
    variance_value = np.var(data)

    # Calcul des valeurs pour les lignes verticales des statistiques
    lines_x = [mean_value, mode_value, median_value]
    colors = ['blue', 'red', 'black']
    labels = ['Moyenne', 'Mode', 'Médiane']
    for x, color, label in zip(lines_x, colors, labels):
        ax.axvline(x=x, color=color, linestyle='--', linewidth=2, label=label)

    # Calcul des valeurs pour les lignes en pointillés pour l'écart type
    std_values = [std_value, 3 * std_value, 5 * std_value]
    colors = ['orange', 'green', 'purple']    
    std_labels = ['1 Sigma', '3 Sigma', '5 Sigma']
    for std, color, label in zip(std_values, colors, std_labels):
        ax.axvline(x=mean_value + std, color=color, linestyle=':', linewidth=2)
        ax.axvline(x=mean_value - std, color=color, linestyle=':', linewidth=2)
        ax.text(mean_value + std, 0.02, label, color=color, fontsize=12, ha='center')

    # Ajouter des flèches avec des textes pour indiquer les statistiques
    # arrow_props = {'arrowstyle': '->'}
    # ax.annotate('Moyenne', xy=(mean_value, 0.008), xytext=(mean_value + 20, 0.02), arrowprops=arrow_props, fontsize=12, color='orange')
    # ax.annotate('Mode', xy=(mode_value, 0.01), xytext=(mode_value + 30, 0.03), arrowprops=arrow_props, fontsize=12, color='green')
    # ax.annotate('Médiane', xy=(median_value, 0.015), xytext=(median_value + 20, 0.04), arrowprops=arrow_props, fontsize=12, color='purple')

    # Ajouter une légende
    ax.legend()

    # Ajouter des labels et un titre
    ax.set_xlabel('Valeurs')
    ax.set_ylabel('Densité')
    ax.set_title(text)



# Générer un échantillon aléatoire de données
np.random.seed(42)

# Création des trois plots côte à côte
fig, axes = plt.subplots(1, 3, figsize=(20, 5))

fig.suptitle('Différence entre Moyenne, Mode, Médiane, Écart Type (1 Sigma, 3 Sigma, 5 Sigma) et Variance')

# Exemple d'utilisation de la fonction avec trois distributions différentes
distribution1 = np.random.exponential(scale=2, size=2000)
distribution2 = np.random.normal(loc=0, scale=1, size=2000)
distribution3 = np.random.power(2, size=2000)

# Générer un échantillon aléatoire de la distribution Cauchy
cauchy_data = np.random.standard_cauchy(size=1000)

# Générer un échantillon aléatoire de la distribution Rayleigh
rayleigh_data = np.random.rayleigh(scale=1, size=1000)

plot_stats(rayleigh_data, "rayleigh", axes[0])
plot_stats(distribution2, "normal", axes[1])
plot_stats(distribution3, "power", axes[2])
plt.show()