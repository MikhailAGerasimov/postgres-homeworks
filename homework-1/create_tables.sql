-- SQL-команды для создания таблиц
CREATE TABLE customer_data
(
	customer_id varchar(6) PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name varchar(100) NOT NULL
);

CREATE TABLE employees_data
(
	employee_id int PRIMARY KEY,
	first_name varchar(20) NOT NULL,
	last_name varchar(20) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date date NOT NULL,
	notes varchar(500) NOT NULL
);

CREATE TABLE order_data
(
	order_id int PRIMARY KEY,
	customer_id varchar(6) REFERENCES customer_data(customer_id),
	employee_id int REFERENCES employees_data(employee_id),
	order_date date NOT NULL,
	ship_city varchar(30) NOT NULL
);
