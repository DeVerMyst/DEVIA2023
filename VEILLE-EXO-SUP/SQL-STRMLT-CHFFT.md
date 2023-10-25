#### SUJET DE VEILLE 

**Chiffrement**
Il existe de nombreux algorithmes de chiffrement différents, chacun avec ses propres avantages et inconvénients. 
Les algorithmes de chiffrement les plus courants pour les applications Python sont AES, RSA et PGP.

**Session** 
Comment avoir des variables de session en Python pour gérer les utilisateurs (admin, membres) avec Streamlit et/ou flask?

**Sécurité**
Qu'est ce qu'une table de métadonnées, comment créer et limiter un utilisateur de base de donneés?

#### SUJET PRATIQUE
**Création d'une application de gestion d'étudiants :**
Créez une application Streamlit qui permet aux utilisateurs d'ajouter, de modifier et de supprimer des étudiants dans une base de données SQLite ou mySQL en utilisant SQLAlchemy. Utilisez Pandas (ou pyplot/bearborn) pour afficher les données des étudiants dans un tableau.
Tables: 
* utilisateur
* genre
* role
* ?

ex: utilisateur (nom, prenom, mail, taille, poids, couleur-cheveux, couleur-yeux, telephone, genre, role)

**Création d'un catalogue de produits :**
Concevez une application Streamlit qui affiche une liste de produits stockés dans une base de données SQLAlchemy. Permettez aux utilisateurs de trier, filtrer et rechercher des produits. Utilisez Pandas pour manipuler les données dans l'application et afficher des graphiques (pyplot/bearborn).
Tables: 
* produits
* catégorie 
* sous catégorie

ex: produit (nom, quantité, sous-catégorie) sous-catégorie (nom, catégorie) catégorie (nom)


**Création d'un suivi de finances personnelles :**
Développez une application Streamlit qui permet aux utilisateurs de saisir leurs transactions financières, qui sont ensuite stockées dans une base de données SQLAlchemy. Vous pouvez récupérer les données en utilisant une api tel que: 
* `yfinance`  

Utilisez Pandas (ou pyplot/bearborn) pour générer des graphiques et des rapports sur les transactions.

**Création d'un blog personnel :**
Concevez une application Streamlit qui permet à un utilisateur de rédiger, éditer et publier des articles de blog. Les articles sont stockés dans une base de données SQLAlchemy, et Pandas peut être utilisé pour gérer les commentaires des utilisateurs.

**SignInSignOut**
Concevez une application Streamlit qui permet à un futur utilisateur de créer un compte s'il n'en possède pas (sans mot de passe) et de se connecter s'il en possède un. Le compte sera composé d'un formulaire avec plusieurs informations qui pourront être modifiées.