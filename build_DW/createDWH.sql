DROP SCHEMA IF EXISTS dwh_whiskey_shop;

CREATE SCHEMA dwh_whiskey_shop;

USE dwh_whiskey_shop;

--- customer dimension table
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

--- products dimension table
drop table if exists dwh_products;

create table dwh_products as
select *
from whiskey_shop.products 
order by product_id;

alter table dwh_products
modify column product_id int not null primary key;

--- employees dimension table
drop table if exists dwh_employees;

create table dwh_employees as
select 
	e.employee_id,
    e.first_name,
    e.last_name,
    e.full_name,
    d.department
from whiskey_shop.employees as e
join whiskey_shop.departments as d
on e.department_id = d.department_id
order by employee_id;

alter table dwh_employees
modify column employee_id int not null primary key;

--- fact table
drop table if exists dwh_fact;

CREATE TABLE dwh_fact AS 
SELECT c1.customer_id,
    e1.employee_id,
    p2.product_id,
    p2.Alcohol_Capcity,
    p2.Alcohol_Percent,
    p2.Alcohol_Price,
    p2.Product_Name,
    c1.four_digits,
    c2.Country,
    c3.credit_provider,
    d.dateId,
    p1.date 
FROM
    whiskey_shop.payments AS p1
        JOIN
    whiskey_shop.customers AS c1 ON p1.customer_id = c1.customer_id
        JOIN
    whiskey_shop.employees AS e1 ON p1.employee_id = e1.employee_id
        JOIN
    whiskey_shop.products AS p2 ON p1.product_id = p2.product_id
        JOIN
    whiskey_shop.countries AS c2 ON c1.country_id = c2.country_id
        JOIN
    whiskey_shop.customer_cc AS c3 ON c1.credit_provider_id = c3.credit_provider_id
        JOIN
    dwh_date AS d ON p1.date = d.Dates
ORDER BY d.Dates;

alter table dwh_fact
add foreign key (customer_id)  references dwh_customers ( customer_id);

alter table dwh_fact
add foreign key (employee_id)  references dwh_employees ( employee_id);

alter table dwh_fact
add foreign key (product_id)  references dwh_products ( product_id);

alter table dwh_fact
add foreign key (dateId)  references dwh_date ( dateId);