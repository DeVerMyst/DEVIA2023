-- Etape 3 , remplir les tableaux 
-- idemn de l'exterieur vers l'intérieur. 
INSERT INTO loc_pays (country)
SELECT DISTINCT Country FROM sales_data;

INSERT INTO loc_region (country_id, state)
SELECT DISTINCT pays.country_id, ini.state
FROM loc_pays as pays
JOIN sales_data as ini on ini.Country = pays.country;

INSERT INTO age_group (age_group)
SELECT DISTINCT Age_Group FROM sales_data;

INSERT INTO clients (age, genre, age_group_id, region_id)
SELECT ini.Customer_age, ini.Customer_Gender , age_group.age_group_id, loc_region.region_id
FROM sales_data as ini
JOIN age_group on ini.Age_Group=age_group.age_group
JOIN loc_region on loc_region.state = ini.State;

INSERT INTO category (cat)
SELECT DISTINCT Product_Category FROM sales_data;

INSERT INTO subcat (subcat, cat_id)
SELECT DISTINCT ini.Sub_Category, category.cat_id
FROM sales_data as ini 
JOIN category on ini.Product_Category=category.cat;

INSERT INTO produits (produit, unit_cost, unit_price)
SELECT DISTINCT ini.Product, ini.Unit_Cost, ini.Unit_Price
FROM sales_data as ini;

/* Bon chance pour celle-ci
Il a fallut se tortiller un peu pour lier l'ID de la sous-catégorie
en utilisant le nom du produit comme repère.
Il y a problablement plus élégant comme query, mais ça marche. 
*/
UPDATE produits as p
INNER JOIN sales_data as d
ON d.Product = p.produit
SET p.subcat_id = 
(SELECT s.subcat_id FROM subcat as s where s.subcat = d.Sub_Category)
;

INSERT INTO principal (`date`, order_quantity, profit, cost, revenue, produit_id)
SELECT ini.`Date`, ini.Order_Quantity , ini.Profit, ini.Cost, ini.Revenue, produits.produit_id
FROM sales_data as ini 
JOIN produits on ini.Product=produits.produit;

-- pour remplir la dernière colonne client_id , 
-- on va faire une hypothèse absurde mais inhérente à notre entrée : 
-- une commande = un client différent 
-- c'est moche, mais ça marche. 

UPDATE principal 
SET client_id = order_id 
WHERE client_id IS NULL;

