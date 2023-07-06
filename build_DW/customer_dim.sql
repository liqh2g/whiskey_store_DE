USE dwh_whiskey_shop;
DROP TABLE IF EXISTS dwh_customers;

CREATE TABLE dwh_customers as
SELECT
    c1.customer_id,
    c1.first_name,
    c1.full_name,
    c2.Country_Code
FROM whiskey_shop.customers as c1 
JOIN whiskey_shop.countries as c2
ON c1.country_id = c2.country_id   
ORDER BY customer_id;

alter TABLE dwh_customers
modify column customer_id int primary key;