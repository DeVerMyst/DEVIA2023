#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from os.path import join
#%% Exercice 1 - Visualisation des notes des étudiants

# Chargement du fichier "student_grades.csv" dans un DataFrame
columns = ['ID', 'salle', 'note']

grades_df = pd.read_csv( join("data","student_grades.csv"), names=columns, header=0)

# Utilisation de Seaborn pour créer un histogramme représentant la distribution des notes des étudiants
sns.histplot(grades_df['note'], bins=10, kde=True)
plt.title("Distribution des notes des étudiants")
plt.xlabel("Notes")
plt.ylabel("Fréquence")
plt.show()

#%% Exercice 2 - Comparaison des notes en fonction des salles

# Utilisation du DataFrame "grades_df" pour créer un graphique à barres montrant la moyenne des notes des étudiants pour chaque salle
sns.barplot(x='salle', y='note', data=grades_df)
plt.title("Moyenne des notes par salle")
plt.xlabel("Salle")
plt.ylabel("Note moyenne")
plt.show()

#%% Exercice 3 - Comparaison des notes en fonction du statut de réussite

# Ajouter une colonne "note_dec" contenant les notes de 0 à 17 (E- à A+)
grade_mapping = {
    'E-': 0, 'E': 1, 'E+': 2,
    'D-': 3, 'D': 4, 'D+': 5,
    'C-': 6, 'C': 7, 'C+': 8,
    'B-': 9, 'B': 10, 'B+': 11,
    'A-': 12, 'A': 13, 'A+': 14
}

grades_df['note_dec'] = grades_df['note'].map(grade_mapping)

# Convertir les notes pour qu'elles soient entre 0 et 20 en appliquant une fonction
def convert_to_20scale(grade):
    return grade * 20 / 14

grades_df['note_20scale'] = grades_df['note_dec'].apply(convert_to_20scale)

# Ajouter une colonne "result" qui contiendra "Réussite" pour les étudiants ayant une note supérieure ou égale à 10, sinon "Échec".
grades_df['result'] = grades_df['note_20scale'].apply(lambda x: "Réussite" if x >= 10 else "Échec")

# Utilisation du DataFrame "grades_df" pour créer un graphique à barres montrant le nombre d'étudiants ayant réussi et échoué
sns.countplot(x='result', data=grades_df)
plt.title("Nombre d'étudiants ayant réussi ou échoué")
plt.xlabel("Statut de réussite")
plt.ylabel("Nombre d'étudiants")
plt.show()

#%% Exercice 4 - Visualisation de la corrélation entre les variables

# Chargement du fichier "titanic.csv" dans un DataFrame
titanic_df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# Utilisation de Seaborn pour créer une matrice de corrélation pour les variables numériques du DataFrame "titanic_df"
correlation_matrix = titanic_df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Matrice de corrélation")
plt.show()

#%% Exercice 5 - Comparaison des tarifs en fonction du statut de survie

# Utilisation du DataFrame "titanic_df" pour créer un graphique en boîte (boxplot) montrant la distribution des tarifs payés par les passagers en fonction de leur statut de survie
sns.boxplot(x='Survived', y='Fare', data=titanic_df)
plt.xticks([0, 1], ['Non survécu', 'Survécu'])
plt.title("Distribution des tarifs en fonction du statut de survie")
plt.xlabel("Statut de survie")
plt.ylabel("Tarif payé")
plt.show()

#%% Exercice 6 - Visualisation des âges des passagers

# Utilisation du DataFrame "titanic_df" pour créer un histogramme représentant la distribution des âges des passagers
sns.histplot(titanic_df['Age'].dropna(), bins=20, kde=True)
plt.title("Distribution des âges des passagers")
plt.xlabel("Âge")
plt.ylabel("Fréquence")
plt.show()

#%% Exercice 7 - Comparaison des âges en fonction du statut de survie

# Utilisation du DataFrame "titanic_df" pour créer un graphique en boîte montrant la distribution des âges des passagers en fonction de leur statut de survie
sns.boxplot(x='Survived', y='Age', data=titanic_df)
plt.xticks([0, 1], ['Non survécu', 'Survécu'])
plt.title("Distribution des âges en fonction du statut de survie")
plt.xlabel("Statut de survie")
plt.ylabel("Âge")
plt.show()

#%% Exercice 8 - Visualisation de la répartition des tarifs

# Utilisation du DataFrame "titanic_df" pour créer un histogramme représentant la répartition des tarifs payés par les passagers
sns.histplot(titanic_df['Fare'], bins=20, kde=True)
plt.title("Répartition des tarifs des passagers")
plt.xlabel("Tarif payé")
plt.ylabel("Fréquence")
plt.show()

#%% Exercice 9 - Comparaison des tarifs en fonction de la classe

# Utilisation du DataFrame "titanic_df" pour créer un graphique en boîte montrant la distribution des tarifs payés par les passagers en fonction de leur classe
sns.boxplot(x='Pclass', y='Fare', data=titanic_df)
plt.title("Distribution des tarifs en fonction de la classe")
plt.xlabel("Classe")
plt.ylabel("Tarif payé")
plt.show()

#%% Exercice 10 - Visualisation de la répartition du genre des passagers

# Utilisation du DataFrame "titanic_df" pour créer un histogramme représentant la répartition des genres
sns.histplot(titanic_df['Sex'], bins=20, kde=True)
plt.title("Répartition du genre des passagers")
plt.xlabel("Genre")
plt.ylabel("Fréquence")
plt.show()

#%% Exercice 11 - Comparaison des âges des étudiants en fonction du statut de réussite

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# a) Chargement du fichier "sales_data.csv" dans un DataFrame
sales_df = pd.read_csv("data/sales_data.csv")
print( sales_df.columns)

# b) Affichage des 10 premières lignes du DataFrame
print(sales_df.head(10))

# c) Calcul du chiffre d'affaires total réalisé sur l'ensemble des transactions
chiffre_affaires_total = (sales_df['Unit_Price'] * sales_df['Order_Quantity']).sum()
print("Chiffre d'affaires total :", chiffre_affaires_total)

# d) Tracé du graphique à barres pour les 5 produits les plus vendus
top_5_products = sales_df.groupby('Product')['Order_Quantity'].sum().nlargest(5)
sns.barplot(x=top_5_products.index, y=top_5_products.values)
plt.title("Les 5 produits les plus vendus")
plt.xlabel("Produit")
plt.ylabel("Quantité vendue")
plt.xticks(rotation=45)
plt.show()




#%% Exercice 12 - Visualisation de la répartition des notes des étudiants

# Utilisation du DataFrame "grades_df" pour créer un histogramme représentant la répartition des notes des étudiants
sns.histplot(grades_df['note'], bins=10, kde=True)
plt.title("Répartition des notes des étudiants")
plt.xlabel("Notes")
plt.ylabel("Fréquence")
plt.show()

#%% Exercice 13 - Comparaison des notes des étudiants en fonction de la salle

# Utilisation du DataFrame "grades_df" pour créer un graphique en boîte montrant la distribution des notes des étudiants en fonction de la salle
sns.boxplot(x='salle', y='note', data=grades_df)
plt.title("Distribution des notes des étudiants en fonction de la salle")
plt.xlabel("Salle")
plt.ylabel("Note")
plt.show()

#%% Exercice 14 - Visualisation des tarifs des passagers en fonction de la classe

# Utilisation du DataFrame "titanic_df" pour créer un graphique en boîte montrant la distribution des tarifs payés par les passagers en fonction de leur classe
sns.boxplot(x='Pclass', y='Fare', data=titanic_df)
plt.title("Distribution des tarifs en fonction de la classe")
plt.xlabel("Classe")
plt.ylabel("Tarif payé")
plt.show()

#%% Exercice 15 - Comparaison des tarifs des passagers en fonction du port d'embarquement

# Utilisation du DataFrame "titanic_df" pour créer un graphique en boîte montrant la distribution des tarifs payés par les passagers en fonction du port d'embarquement
sns.boxplot(x='Embarked', y='Fare', data=titanic_df)
plt.title("Distribution des tarifs en fonction du port d'embarquement")
plt.xlabel("Port d'embarquement")
plt.ylabel("Tarif payé")
plt.show()

#%% Exercice 16 - Visualisation de la répartition des tarifs des passagers

# Utilisation du DataFrame "titanic_df" pour créer un histogramme représentant la répartition des tarifs payés par les passagers
sns.histplot(titanic_df['Fare'], bins=20, kde=True)
plt.title("Répartition des tarifs des passagers")
plt.xlabel("Tarif payé")
plt.ylabel("Fréquence")
plt.show()

#%% Exercice 17 - Comparaison des tarifs des passagers en fonction du sexe

# Utilisation du DataFrame "titanic_df" pour créer un graphique en boîte montrant la distribution des tarifs payés par les passagers en fonction du sexe
sns.boxplot(x='Sex', y='Fare', data=titanic_df)
plt.title("Distribution des tarifs en fonction du sexe")
plt.xlabel("Sexe")
plt.ylabel("Tarif payé")
plt.show()

#%% Exercice 18 - Visualisation des tarifs des passagers en fonction du statut de survie

# Utilisation du DataFrame "titanic_df" pour créer un graphique en boîte montrant la distribution des tarifs payés par les passagers en fonction de leur statut de survie
sns.boxplot(x='Survived', y='Fare', data=titanic_df)
plt.xticks([0, 1], ['Non survécu', 'Survécu'])
plt.title("Distribution des tarifs en fonction du statut de survie")
plt.xlabel("Statut de survie")
plt.ylabel("Tarif payé")
plt.show()

#%% Exercice 19 - Comparaison des âges des passagers en fonction du port d'embarquement

# Utilisation du DataFrame "titanic_df" pour créer un graphique en boîte montrant la distribution des âges des passagers en fonction du port d'embarquement
sns.boxplot(x='Embarked', y='Age', data=titanic_df)
plt.title("Distribution des âges en fonction du port d'embarquement")
plt.xlabel("Port d'embarquement")
plt.ylabel("Âge")
plt.show()

#%% Exercice 20 - Visualisation de la répartition des âges des passagers

# Utilisation du DataFrame "titanic_df" pour créer un histogramme représentant la répartition des âges des passagers
sns.histplot(titanic_df['Age'].dropna(), bins=20, kde=True)
plt.title("Répartition des âges des passagers")
plt.xlabel("Âge")
plt.ylabel("Fréquence")
plt.show()
