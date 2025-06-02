-- creating the table for departments
create table departments (
dept_id serial primary key,
dept_name varchar (100) unique not null
);

-- inserting the data into the table created
insert into departments(dept_name)
values
('IT'), ('HR'), ('Finance'), ('Marketing'), ('Operations');
select * from departments;

-- creating the table for employees
create table employees (
emp_id serial primary key,
fname varchar (100) not null,
lname varchar (100),
city varchar (100),
email varchar (100) unique not null,
dept_id int references departments(dept_id),
joining_date date not null default current_date,
salary decimal (7,2) default 30000.00
);

-- inserting the data into the table created
insert into employees (fname, lname, city, email, dept_id, joining_date, salary)
values
('Raj', 'Sharma', 'Delhi', 'raj.sharma@example.com', 1, '2020-01-15', 50000.00),
('Priya', 'Singh', 'Mumbai', 'priya.singh@example.com', 2, '2019-03-22', 45000.00),
('Arjun', 'Verma', 'Delhi', 'arjun.verma@example.com', 1, '2021-06-01', 55000.00),
('Suman', 'Patel', 'Chennai', 'suman.patel@example.com', 3, '2018-07-30', 60000.00),
('Kavita', 'Rao', 'Pune', 'kavita.rao@example.com', 2, '2020-11-10', 47000.00);
select * from employees;


-- creating the table for projects
create table projects(
project_id serial primary key,
project_name varchar (100),
dept_id int references departments(dept_id)
);

-- inserting the data into the table created
insert into projects (project_name, dept_id)
values
('Website Revamp', 1),
('Recruitment Drive', 2),
('Budget Planning', 3),
('Marketing Blitz', 4);
select * from projects;


-- creating the table for employee_project
create table employee_project (
emp_id int references employees(emp_id),
project_id int references projects(project_id),
assigned_date date default current_date,
primary key(emp_id, project_id)
);

-- inserting the data into the table created
insert into employee_project (emp_id, project_id)
values
(1,1), (2,2), (3,1), (4,3), (5,2);
select * from employee_project;


----------------------------------------------

-- Performing queries 

-- 1. Adding new employee 
insert into employees (fname, lname, city, email, dept_id, joining_date, salary)
values 
('Rohan','Mehra', 'Bengaluru', 'rohan.mehra@example.com', 2, current_date, 52000.00);
select * from employees;

-- 2. Updating the city of an Employee
update employees
set city = 'Jaipur'
where fname = 'Rohan'; 
select * from employees;

-- 3. Deleting employee where fname = 'Suman' 
delete from employee_project 
where emp_id = 4;
delete from employees 
where emp_id = 4;
select * from employees;
select * from employee_project;

-- 4. Showing employees where city contains 'i' 
select * from employees
where city like '%i%';

-- 5. Employees with salary between 45k and 50k
select * from employees 
where salary between 45000 and 50000;

-- 6. Departments in alphabetical order 
select * from departments 
order by dept_name;

-- 7. Distinct city names from employees
select distinct city from employees;

-- 8. Average salary of all employees
select avg(salary) as average_salary from employees;

-- 9. Uppercasing fnames of all the employees 
select upper(fname) as upper_fname from employees;

-- 10. Extracting domain from the emails 
select email, substring (email from position ('@' in email)+1) as domain from employees;

-- 11. Adding column 'Gender' to employees
alter table employees 
add column gender varchar (10);
select * from employees;

-- 12. Changing the size of column 'city'
alter table employees 
alter column city
set data type varchar (150);
select * from employees;

-- 13. Showing top 3 highest paid employees
select * from employees 
order by salary desc limit 3;