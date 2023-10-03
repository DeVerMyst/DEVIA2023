-- on jette on créé
DROP DATABASE IF EXISTS FoodDistribution;
CREATE DATABASE FoodDistribution;

-- on utilise 
USE FoodDistribution;

-- on va créer nos tables 

-- table famille
CREATE TABLE Famille
(
	ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    famille VARCHAR(80) UNIQUE,
    PRIMARY KEY (ID)
);

-- conditionnement
CREATE TABLE Conditionnement
(
	ID SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    conditionnement VARCHAR(80) UNIQUE,
    PRIMARY KEY (ID)
);

-- table principale 
CREATE TABLE Principale
(
	ID INT NOT NULL AUTO_INCREMENT,
    Code_article MEDIUMINT UNSIGNED,
    Libelle VARCHAR(80),
    Famille_ID SMALLINT UNSIGNED,
    Conditionnement_ID SMALLINT UNSIGNED,
	PU_HT DECIMAL(10,2),
    PRIMARY KEY (ID),
    FOREIGN KEY (Famille_ID) REFERENCES Famille(ID) ON DELETE CASCADE,
    FOREIGN KEY (Conditionnement_ID) REFERENCES Conditionnement(ID)
);

-- creation d'une vue 
CREATE VIEW select_all AS
select Code_article as "Code article", Libelle, Conditionnement, famille, PU_HT as "prix unitaire" from conditionnement
left join principale on Conditionnement.id = conditionnement_id
left join famille on famille_id = famille.id;





