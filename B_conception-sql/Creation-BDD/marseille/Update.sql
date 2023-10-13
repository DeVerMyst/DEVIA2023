USE FoodDistribution;

-- INSERT INTO Famille (famille) VALUES ("titi");
-- INSERT INTO Famille (famille) VALUES ("tata");

INSERT INTO Famille (famille) VALUES ("qsd"),("sdf"),("ert");

INSERT INTO Conditionnement (conditionnement) VALUES ("qsd"),("sdf"),("ert");

INSERT INTO Principale (Code_article,Libelle,Famille_ID,Conditionnement_ID,PU_HT)
VALUES 
(1010,"poulpe",1,1,45.54),
(1010,"fdsfds",2,1,45.54),
(1010,"dgdfgd",2,1,45.54),
(1010,"ytughu",1,1,45.54);
