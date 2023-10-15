import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from os.path import join
# Définir le nom de la base de données
def bk():
    return print("\n",79*'=','\n')

database_name = "my_database"
file_path = join("D:\[4] - GITHUB\DEVIA2023\E_sqlalchemy\data\data.csv")

if os.path.exists(file_path):
    data = pd.read_csv(file_path)
else:
    bk()
    print(file_path)
    print("The file 'data.csv' does not exist in the directory 'data'")
    bk()

# Drop la base de données si elle existe
if os.path.exists(database_name):
    engine = create_engine("mysql+pymysql://root:root@localhost:3306/")
    engine.execute("DROP DATABASE {}".format(database_name))

# Créer la base de données
engine = create_engine("mysql+pymysql://root:root@localhost:3306/{}".format(database_name))
# engine.execute("CREATE DATABASE {}".format(database_name))

# Charger les modèles
from models.model import Utilisateur, Genre, Pays

# Ouvrir le fichier CSV
data = pd.read_csv(file_path)

# Créer une session pour accéder à la base de données
session = Session(engine)

# Remplir les tables
for index, row in data.iterrows():
    # Créer un objet de la table
    if row[0] == "utilisateur":
        object = Utilisateur(id=row[1], nom=row[2], prenom=row[3], mail=row[4], genre_id=row[5], pays_id=row[6])
    elif row[0] == "genre":
        object = Genre(id=row[1], nom=row[2])
    elif row[0] == "pays":
        object = Pays(id=row[1], nom=row[2])

    # Ajouter l'objet à la table
    session.add(object)

# Exécuter les requêtes SQL
session.commit()

# Fermer la session
session.close()

# Afficher les données de la table
for table_name in ["utilisateur", "genre", "pays"]:
    # Créer une instance de la classe `Table`
    table = getattr(session.query, table_name)

    # Lire les données de la table
    results = table.all()

    # Afficher les résultats
    for row in results:
        print(row)
