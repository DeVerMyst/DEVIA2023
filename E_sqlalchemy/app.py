# import basics
import os
import pandas as pd
from os.path import join

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from models.model import Utilisateur, Genre, Pays, Base

from sqlalchemy_utils import database_exists, create_database, drop_database

import config

# Importation des informations de connexion
DATABASE_HOST = config.DATABASE_HOST
DATABASE_NAME = config.DATABASE_NAME
DATABASE_USERNAME = config.DATABASE_USERNAME
DATABASE_PASSWORD = config.DATABASE_PASSWORD

# Création du moteur de base de données
engine = create_engine(f"mysql+pymysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}")


# Définir le nom de la base de données
def bk():
    return print("\n",79*'=','\n')

file_path = join(join("E_sqlalchemy","data","data.csv"))

if os.path.exists(file_path):
    data = pd.read_csv(file_path)
    # Ouvrir le fichier CSV
    data = pd.read_csv(file_path)
else:
    bk()
    print(file_path)
    bk()
    print("The file 'data.csv' does not exist in the directory 'data'")
    print("pwd", os.getcwd())
    bk()

# Création de la connexion à la base de données
# engine = create_engine("mysql+pymysql://root:root@localhost/my_database_tmp")
if database_exists(engine.url):
    drop_database(engine.url)    

create_database(engine.url)
print("is database existing?: ", database_exists(engine.url))

# Création des tables
Base.metadata.create_all(engine)

# Création d'une session
Session = sessionmaker(bind=engine)
session = Session()

# Remplissage des tables Genre et Pays
genres = data['genre'].unique()
pays = data['pays'].unique()

for genre in genres:
    genre_obj = Genre(nom=genre)
    session.add(genre_obj)

for pays_nom in pays:
    pays_obj = Pays(nom=pays_nom)
    session.add(pays_obj)

# Validation des modifications pour les tables Genre et Pays
session.commit()

# Lecture du CSV pour créer les utilisateurs
for index, row in data.iterrows():
    utilisateur = Utilisateur(
        nom=row['nom'],
        prenom=row['prenom'],
        mail=row['mail'],
    )

    genre_obj = session.query(Genre).filter_by(nom=row['genre']).first()
    pays_obj = session.query(Pays).filter_by(nom=row['pays']).first()

    if genre_obj:
        utilisateur.genre_id = genre_obj.id

    if pays_obj:
        utilisateur.pays_id = pays_obj.id

    session.add(utilisateur)

# Validation des modifications
session.commit()

# Récupérez tous les utilisateurs
import pandas as pd 

result = session.query(Utilisateur).all()
print(result[0])

# Utilisez la fonction pd.DataFrame pour convertir la liste d'objets en DataFrame
df = pd.DataFrame([utilisateur.__dict__ for utilisateur in result])

# Supprimez la colonne '_sa_instance_state' qui est spécifique à SQLAlchemy
df = df.drop('_sa_instance_state', axis=1)

bk()
print("SQL QUERY")
bk()
print( df )
bk()
print("DATA CSV")
bk()
print( data )
bk()

# Utilisez SQLAlchemy pour obtenir les données avec les valeurs de genre et pays
result = session.query(
    Utilisateur.nom,
    Utilisateur.prenom,
    Utilisateur.mail,
    Genre.nom.label('genre'),  # Utilisez label pour renommer la colonne
    Pays.nom.label('pays')
).join(Genre, Utilisateur.genre_id == Genre.id).join(Pays, Utilisateur.pays_id == Pays.id).all()



df = pd.DataFrame(result, columns=data.columns)

print("JOINTURES")
bk()
print( df ) 
bk()



