DROP DATABASE IF EXISTS MELHOUSE;
CREATE DATABASE MELHOUSE;
USE MELHOUSE;

SELECT * FROM location;
SELECT * FROM property;
SELECT * FROM house_details;
SELECT * FROM seller;
SELECT * FROM sale;



DROP DATABASE IF EXISTS MELHOUSE_DDL;
CREATE DATABASE MELHOUSE_DDL;
USE MELHOUSE_DDL;
select * from fact_dim;
select * from seller_dim;
select * FROM property_dim;
select * from location_dim;
select * from sale_info_dim;
select * from house_details_dim;
DELETE FROM house_details_dim WHERE house_details_tk = 0;
DELETE FROM location_dim WHERE location_tk = 0;
DELETE FROM property_dim WHERE property_tk = 0;
DELETE FROM sale_info_dim WHERE sale_info_tk = 0;
DELETE FROM seller_dim WHERE seller_tk = 0;