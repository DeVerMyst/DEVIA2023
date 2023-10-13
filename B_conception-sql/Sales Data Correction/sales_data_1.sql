DROP SCHEMA IF EXISTS SALES;
CREATE SCHEMA SALES;
USE SALES;

-- Mois
CREATE TABLE Mois
(
	id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
    mois VARCHAR(10) UNIQUE,
    PRIMARY KEY (id)
);

-- Age_Group
CREATE TABLE Age_Group
(
	id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
    age_group VARCHAR(20) UNIQUE,
    PRIMARY KEY (id)
);

-- Customer_Gender
CREATE TABLE Customer_Gender
(
	id TINYINT(1) UNSIGNED NOT NULL AUTO_INCREMENT,
    customer_gender VARCHAR(10) UNIQUE,
    PRIMARY KEY (id)
);

-- Country
CREATE TABLE Country
(
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    country VARCHAR(20) UNIQUE,
    PRIMARY KEY (id)
);

-- State
CREATE TABLE State
(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    state VARCHAR(20) UNIQUE,
    country SMALLINT UNSIGNED NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (country) REFERENCES Country(id) 
);

-- Product_Category
CREATE TABLE Product_Category
(
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    product_category VARCHAR(50) UNIQUE,
    PRIMARY KEY (id)
);

-- Sub_Category
CREATE TABLE Sub_Category
(
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    sub_category VARCHAR(20) UNIQUE,
    product_category SMALLINT UNSIGNED NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (product_category) REFERENCES Product_Category(id) 
);

-- Product
CREATE TABLE Product
(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    product VARCHAR(20) UNIQUE,
    sub_category SMALLINT UNSIGNED NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (sub_category) REFERENCES Sub_Category(id) 
);


-- Product
CREATE TABLE Commande
(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    
    date_cmd DATE, 
    
    day_cmd TINYINT UNSIGNED NOT NULL,
    month_cmd TINYINT UNSIGNED NOT NULL,
    year_cmd INT UNSIGNED NOT NULL,
    
    customer_age TINYINT UNSIGNED NOT NULL,
    age_group TINYINT UNSIGNED NOT NULL,
    customer_gender TINYINT(1) UNSIGNED NOT NULL,

    state INT UNSIGNED NOT NULL,    
    
	product INT UNSIGNED NOT NULL,    
	order_quantity INT UNSIGNED NOT NULL,    
	unit_cost INT UNSIGNED NOT NULL,    
	unit_price INT UNSIGNED NOT NULL,    
	profit INT UNSIGNED NOT NULL,    
	cost INT UNSIGNED NOT NULL,    
	revenue INT UNSIGNED NOT NULL,    

    PRIMARY KEY (id),
    FOREIGN KEY (month_cmd) REFERENCES Mois(id), 
    FOREIGN KEY (age_group) REFERENCES Age_Group(id),
    FOREIGN KEY (customer_gender) REFERENCES Customer_Gender(id),
    FOREIGN KEY (state) REFERENCES State(id),
    FOREIGN KEY (product) REFERENCES Product(id) 
);


