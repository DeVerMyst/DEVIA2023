-- Etape 1 : Creation des tables

DROP DATABASE IF EXISTS sales_2;

CREATE DATABASE sales_2;
USE sales_2;

-- On commence par les dimensions extérieures
CREATE TABLE loc_pays (
			country_id INT UNSIGNED auto_increment,
			country varchar(25) UNIQUE,
            PRIMARY KEY (country_id)
            );
            
CREATE TABLE loc_region (
			region_id INT UNSIGNED auto_increment,
			country_id INT UNSIGNED,
            state VARCHAR(40) UNIQUE,
            PRIMARY KEY (region_id),
            FOREIGN KEY (country_id) REFERENCES loc_pays(country_id)
            );
            
CREATE TABLE age_group (
			age_group_id TINYINT UNSIGNED auto_increment,
            age_group VARCHAR(25) UNIQUE,
            PRIMARY KEY (age_group_id)
            );
            
CREATE TABLE clients (
			client_id INT unsigned auto_increment,
            age TINYINT UNSIGNED,
            genre VARCHAR(1),
            age_group_id TINYINT UNSIGNED,
            region_id INT UNSIGNED,
            PRIMARY KEY (client_id),
            FOREIGN KEY (age_group_id) REFERENCES age_group(age_group_id),
            FOREIGN KEY (region_id) REFERENCES loc_region(region_id)
            );
            
CREATE TABLE category ( 
					cat_id INT UNSIGNED auto_increment,
                    cat VARCHAR(20) UNIQUE, 
                    PRIMARY KEY (cat_id)
                    );
                    
CREATE TABLE subcat (
					subcat_id INT UNSIGNED auto_increment,
                    subcat VARCHAR(40),
                    cat_id INT UNSIGNED,
                    primary key (subcat_id),
                    FOREIGN KEY (cat_id) REFERENCES category(cat_id)
);

CREATE TABLE produits ( 
					produit_id INT UNSIGNED AUTO_INCREMENT,
                    produit VARCHAR(40) UNIQUE, 
                    unit_cost SMALLINT UNSIGNED,
                    unit_price SMALLINT UNSIGNED,
                    subcat_id INT UNSIGNED,
                    PRIMARY KEY (produit_id),
                    FOREIGN KEY (subcat_id) REFERENCES subcat(subcat_id)
);
            
CREATE TABLE principal ( 
					order_id INT UNSigNED AUTO_INCREMENT,
                    `date` DATE,
                    order_quantity TINYINT UNSIGNED,
                    profit SMALLINT,
                    cost SMALLINT UNSIGNED,
                    revenue SMALLINT UNSIGNED,
                    client_id INT UNSIGNED,
                    produit_id INT UNSIGNED,
                    PRIMARY KEY (order_id),
                    FOREIGN KEY (client_id) REFERENCES clients(client_id),
                    FOREIGN KEY (produit_id) REFERENCES produits(produit_id)
				
);