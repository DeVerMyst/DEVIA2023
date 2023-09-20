import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Paramètres de la distribution normale
mu = 0    # Moyenne
sigma = 1 # Écart type

# Création des données pour la courbe de la distribution normale
x = np.linspace(-5, 5, 1000)
pdf = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-(x - mu)**2 / (2 * sigma**2))

# Nombre de points à générer à chaque itération
num_points_per_iter = 10

# Nombre total d'itérations
num_iterations = 100

# Initialisation des données
data = np.array([])

# Création de la figure et des sous-plots
fig, (ax_left, ax_center, ax_right) = plt.subplots(1, 3, figsize=(15, 5))

# Axe du centre pour les points aléatoires
ax_center.set_xlim(0, num_points_per_iter * num_iterations)
ax_center.set_ylim(-4, 4)
ax_center.set_title('Points aléatoires')

# Axe de gauche pour l'accumulation des points (histogramme vertical)
ax_left.set_xlim(0, num_iterations*num_points_per_iter/4)
ax_left.set_ylim(-4, 4)
ax_left.set_title('Accumulation des points')

# Axe de droite pour l'histogramme normalisé
ax_right.set_xlim(-4, 4)
ax_right.set_ylim(0, 0.4)
ax_right.set_title('Histogramme normalisé')
ax_right.set_xlabel('Valeurs')
ax_right.set_ylabel('Densité')

# Initialisation des éléments pour la mise à jour de l'animation
points_center, = ax_center.plot([], [], 'bo', alpha=0.5)

# Création des barres de l'histogramme à gauche
left_rects = [plt.Rectangle((0, 0), 0, 0.2, color='b', alpha=0.5) for _ in range(20)]
for rect in left_rects:
    ax_left.add_patch(rect)

hist_normalized, = ax_right.plot([], [], 'b-', alpha=0.75)
normal_curve, = ax_right.plot([], [], 'r-', alpha=0.75)
nb=0
def update(frame):
    global data, nb

    # Générer des points aléatoires selon la distribution normale
    new_points = np.random.normal(mu, sigma, num_points_per_iter)

    # Accumuler les nouveaux points
    data = np.concatenate((data, new_points))

    # Mise à jour des points aléatoires au centre
    points_center.set_data(np.arange(len(data)), data)

    # Mise à jour de l'accumulation des points à gauche (histogramme vertical)
    left_y, left_bins = np.histogram(data, bins=20, range=(-4, 4))
    left_rects_data = np.array([left_y, left_bins[:-1]])
    for rect, h, y in zip(left_rects, left_rects_data[0], left_rects_data[1]):
        rect.set_width(h)
        rect.set_y(y)

    # Mise à jour de l'histogramme normalisé à droite
    hist, bins = np.histogram(data, bins=20, range=(-4, 4), density=True)
    width = bins[1] - bins[0]
    right_x = bins[:-1] + width / 2
    hist_normalized.set_data(right_x, hist)

    # la courbe de la loi normale
    normal_curve.set_data(x, pdf)

    # Arrêter l'animation après un certain nombre d'itérations
    nb+=1
    if nb == num_iterations:
        ani.event_source.stop()

    return points_center, *left_rects, hist_normalized, normal_curve

# Création de l'animation
ani = animation.FuncAnimation(fig, update, frames=num_iterations, interval=100, blit=True)
plt.show()
