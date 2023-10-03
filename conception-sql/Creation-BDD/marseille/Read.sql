USE FoodDistribution;

SELECT * FROM Famille;

SELECT * FROM Conditionnement;

SELECT * FROM Principale;

select Code_article as "Code article", Libelle, Conditionnement, famille, PU_HT as "prix unitaire" from conditionnement
left join principale on Conditionnement.id = conditionnement_id
left join famille on famille_id = famille.id;

SELECT * FROM select_all;
