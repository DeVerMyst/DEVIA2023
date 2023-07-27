import numpy as np
import matplotlib.pyplot as plt

# Paramètres du signal (porte)
taille_porte = 100
signal = np.zeros(taille_porte)
signal[:20] = 1.0

# Paramètres du bruit et nombre de réalisations
nb_realisations = 49
ecart_type_bruit = 0.2

# Génération du bruit gaussien à moyenne nulle pour toutes les réalisations
bruit = np.random.normal(loc=0.0, scale=ecart_type_bruit, size=(nb_realisations, taille_porte))

# Tableau pour stocker les mesures pour chaque réalisation
mesures_realisations = np.zeros((nb_realisations, taille_porte))

# Tableau pour stocker les signaux estimés à chaque étape
signaux_estimes = np.zeros((nb_realisations, taille_porte))

# Tableau pour stocker les écarts types à chaque étape
ecarts_types_estimes = np.zeros((nb_realisations, taille_porte))

plt.figure(figsize=(12, 6))

# Boucle pour les réalisations
for r in range(nb_realisations):
    # Mesures du signal avec ajout du bruit correspondant à cette réalisation
    mesures = signal + bruit[r]
    mesures_realisations[r] = mesures
    
    # Mise à jour de la moyenne des signaux acquis jusqu'à cette réalisation
    moyenne_mesures = np.mean(mesures_realisations[:r+1], axis=0)
    signaux_estimes[r] = moyenne_mesures
    
    # Mise à jour de l'écart type des signaux acquis jusqu'à cette réalisation
    ecart_type_mesures = np.std(signaux_estimes[:r+1] - signal, axis=0)

# Tracé des résultats

    plt.subplot(2, 1, 1)

    plt.plot(mesures_realisations[r], label=f"Réalisation {r+1}")
    plt.plot(signal, 'k--', label="Signal d'origine")
    plt.xlabel('Temps')
    plt.ylabel('Amplitude')
    plt.title('Mesures pour chaque réalisation')
    plt.ylim([-.5,1.5])
    plt.grid()
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(signaux_estimes[r], label=f"Estimation {r+1}")
    plt.plot(signal, 'k--', label="Signal d'origine")
    plt.fill_between(range(taille_porte), signal - 3*ecart_type_mesures, signal + 3*ecart_type_mesures, alpha=0.3, label="Intervalle de +/- écart-type des signaux estimés")
    plt.xlabel('Temps')
    plt.ylabel('Amplitude')
    plt.title('Estimation du signal avec intervalle de +/- 3 écart-type')
    plt.ylim([-.5,1.5])
    plt.grid()
    plt.legend()

    plt.tight_layout()
    # plt.show()
    plt.pause(0.25)
    plt.clf()
plt.show()