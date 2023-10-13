-- insertion de données dans la DEVIA2023 

USE DEVIA2023;

-- INSERT INTO principale (ID, nom) VALUES (1,"mehdi");
INSERT INTO principale (nom) VALUES ("briac");
INSERT INTO principale (nom) VALUES ("Thomas");

UPDATE principale
SET nom = "Eli"
WHERE nom="briac";


-- genre et users 
INSERT INTO genre (genre) VALUES ("poulpe");
INSERT INTO genre (genre) VALUES ("canard");
INSERT INTO genre (genre) VALUES ("spaghetti");

INSERT INTO users (nom, genre) VALUES ("dark vador",1);
INSERT INTO users (nom, genre) VALUES ("R2D2",2);
INSERT INTO users (nom, genre) VALUES ("C3PO",3);