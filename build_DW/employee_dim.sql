USE dwh_whiskey_shop;

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