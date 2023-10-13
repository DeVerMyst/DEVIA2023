#### Exercices 

>1. rappel import des données
>2. trucs et astuces

1. rappel import des données
   
```python
from sklearn.datasets import fetch_openml
# Charge les données
data = fetch_openml(name="nom-du-dataset") 
X = data["data"] 
y = data["target"]
```

2. trucs et astuces 

* Exploration des données : Commencez par effectuer une analyse exploratoire des données pour obtenir des informations sur l'ensemble de données. Visualisez les distributions des caractéristiques et de la variable cible.

* Prétraitement des données : Recherchez les valeurs manquantes dans l'ensemble de données et décidez d'une stratégie appropriée pour les gérer. Vous pouvez également normaliser ou standardiser les caractéristiques.

* Pour du supervisé, divisez en apprentissage et en test : Divisez l'ensemble de données en ensembles d'apprentissage et de test. Vous pouvez utiliser une division typique, par exemple 70 % pour l'apprentissage et 30 % pour les tests.

* Sélection du modèle : Vous pouvez expérimenter avec différents algorithmes de classification.

* Performance : utilisez les bonnes métriques en fonction de votre cas (regression, classification, clustering)

* Évaluation du modèle : Utilisez des techniques de validation croisée pour évaluer les capacités de généralisation de votre modèle. Essayez différents hyperparamètres pour affiner les modèles.

* Interprétation du modèle : Après avoir formé un modèle, envisagez de visualiser les caractéristiques importantes et de comprendre leur impact sur la prédiction.

* Déséquilibre de classes : s'il s'agit d'un problème de classification binaire, vérifiez s'il y a un déséquilibre de classes. Si c'est le cas, vous devrez peut-être utiliser des techniques telles que la suréchantillonnage, la sous-échantillonnage ou la technique de sur-échantillonnage minoritaire synthétique (SMOTE) pour y remédier.

* Évaluation finale : Évaluez les performances du modèle final sur l'ensemble de test. Assurez-vous de rapporter vos résultats et toutes les observations ou informations que vous avez obtenues en travaillant avec cet ensemble de données.

>**Exercices génériques pour la classification**

> **Exercice 1**
Ensemble de données du Centre de services de transfusion sanguine

**Description :**

Cet ensemble de données provient de la base de données des donneurs du Centre de services de transfusion sanguine de la ville de Hsin-Chu, à Taïwan. L'objectif principal de cet ensemble de données est de prédire si un donneur fera un don de sang en mars 2007 en se basant sur le comportement passé du donneur.

**Attributs :**

Ancienneté (V1) : Mois depuis le dernier don du donneur.
Fréquence (V2) : Le nombre total de dons effectués par le donneur.
Montant (V3) : Le volume total de sang donné en centimètres cubes.
Temps (V4) : Mois depuis le premier don du donneur.
Don en mars 2007 (Variable cible) : Une variable binaire représentant si le donneur a donné du sang en mars 2007 (1 pour a donné, 0 pour n'a pas donné).
Tâche :

La principale tâche est de construire un modèle prédictif capable de déterminer si un donneur fera un don de sang en mars 2007. Il s'agit d'un problème de classification binaire où vous prévoyez la valeur de l'attribut "Don en mars 2007".

**Pratique**

Importez le dataset `blood-transfusion-service-center` (ID : 1464) depuis OpenML.

**Question**

**La classe à prédire est :** `Class`

>**Exercice 2**
Ensemble de données de la base de données sur le diabète des Indiens Pima

**Énoncé :**

Cet ensemble de données provient de l'étude sur le diabète des Indiens Pima menée par le National Institute of Diabetes and Digestive and Kidney Diseases. L'ensemble de données contient des informations sur les patients féminins âgés d'au moins 21 ans issus de la tribu des Indiens Pima vivant dans la région de Phoenix, en Arizona.

**Pratique**

Importez le dataset `diabetes` (ID : 37) depuis OpenML.

**Question**

**La variable à prédire est :** `Class`

>**Exercice 3**
Ensemble de données sur l'assurance

**Énoncé**

L'objectif principal de cet ensemble de données est de réaliser des tâches de classification. Vous devez prédire la valeur de l'attribut "class" en fonction des autres caractéristiques. Cela peut être un problème de classification binaire ou multiclasse en fonction du nombre de valeurs distinctes dans  l'attribut "class".

**Pratique**

Importez le dataset `Insurance` (ID : 45064) depuis OpenML.

**Question**

Cet ensemble de données concerne le secteur de l'assurance et est destiné à des tâches de classification. Il comprend une combinaison de variables continues et catégoriques.

**La variable à prédire est :** `Class`

> **Exercice 4**
Ensemble de données des compagnies aériennes

**Énoncé**

Cet ensemble de données des compagnies aériennes est inspiré du jeu de données de régression d'Elena Ikonomovska. La tâche consiste à prédire si un vol donné sera en retard en se basant sur les informations de départ programmé.

**Pratique**

Importez le dataset `airlines` (ID : 45072) depuis OpenML.

**Question**

**La variable à prédire est :** `Class`

> **Exercices génériques pour la regression**

> **Exercice 1**
Ensemble de données California Housing Prices

**Énoncé**

L'objectif principal de cet ensemble de données est de réaliser des tâches de régression. Vous devez prédire la valeur de l'attribut "price" (prix des logements en Californie) en fonction des autres caractéristiques. Il s'agit d'une tâche de régression où vous devrez prédire une valeur numérique continue.

**Pratique**

Importez le dataset `california` (ID : 44031) depuis OpenML.

**Question**

**La variable à prédire est :** `price`

> **Exercice 2**
Ensemble de données "Slump"

**Énoncé**

Cet ensemble de données "Slump" est un ensemble de données de régression multivariée provenant de l'article : The Concrete Slump dataset (Yeh 2007). Il porte sur la prédiction de trois propriétés du béton (retrait, écoulement et résistance à la compression) en fonction de la teneur en sept ingrédients du béton : ciment, cendres volantes, laitier de haut fourneau, eau, superplastifiant, granulats grossiers et granulats fins.
**Pratique**

Importez le dataset `slump` (ID : 41558) depuis OpenML.

**Question**

**Les variables à prédire sont :** `SLUMP_cm`, `FLOW_cm`, `Compressive_Strength_Mpa`

**astuces** votre vecteur `y` possède trois colonnes 

>**Exercice 3**
**Ensemble de données "Elevators"**

**Énoncé**

Cet ensemble de données appartient au benchmark "régression sur les caractéristiques numériques" et provient également de la tâche de contrôle d'un avion F16. Cependant, cette fois, la variable cible et les attributs sont différents de ceux du domaine des ailerons. Dans ce cas, la variable cible est liée à une action effectuée sur les élévateurs de l'aéronef.


**Pratique**

Importez le dataset `elevators` (ID : 44134) depuis OpenML.

**Question**

**La variable à prédire est :** `Goal`

>**Exercices génériques pour le clustering**

>**Exercice 1**
>Ensemble de données "Heart-Disease-patients" - Comprendre les Traitement des Maladies Cardiaques

**Énoncé**

Cet ensemble de données s'intéresse à un domaine médical crucial : les traitements des maladies cardiaques. Il existe de nombreuses situations où regrouper des données similaires est essentiel. Une manière de regrouper des objets similaires est d'utiliser des algorithmes de regroupement (clustering). Dans ce cas, nous allons explorer l'utilité des algorithmes de regroupement non supervisés pour aider les médecins à comprendre quels traitements pourraient fonctionner avec leurs patients.

**Pratique**

Importez le dataset `Heart-Disease-patients` (ID : 43562) depuis OpenML.

**Question**

Nous allons regrouper des données anonymisées de patients ayant été diagnostiqués avec une maladie cardiaque. Les patients ayant des caractéristiques similaires pourraient répondre aux mêmes traitements, et les médecins pourraient bénéficier d'informations sur les résultats des traitements des patients similaires à ceux qu'ils traitent. Les données analysées proviennent du Centre Médical V.A. de Long Beach, en Californie.

>**Exercice 2**
> Ensemble de données "Credit-Card-Dataset-for-Clustering" - Segmentation de la clientèle pour la stratégie marketing

**Énoncé**

Ce jeu de données vise à développer une segmentation des clients pour définir une stratégie marketing. L'échantillon de données résume le comportement d'utilisation d'environ 9 000 titulaires de cartes de crédit actifs au cours des 6 derniers mois. 

**Pratique**

Importez le dataset `Credit-Card-Dataset-for-Clustering` (ID : 43618) depuis OpenML.



