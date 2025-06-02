create table employee (
emp_id serial primary key,
fname varchar (100) not null,
lname varchar (100) not null,
email varchar (100) not null unique,
dept varchar (100),
salary decimal (7,2) default 30000.00,
hire_date date not null default current_date
);

delete from employee;
select * from employee;
alter table employee
alter column salary
set data type decimal (7,2);
rename email to gmail;
add column email varchar (100);

INSERT INTO employee (emp_id, fname, lname, dept, salary, hire_date, gmail)  
VALUES

(1, 'Raj', 'Sharma', 'IT', 50000.00, '2020-01-15', 'raj.sharma@example.com'),
(2, 'Priya', 'Singh', 'HR', 45000.00, '2019-03-22', 'priya.singh@example.com'),
(3, 'Arjun', 'Verma', 'IT', 55000.00, '2021-06-01', 'arjun.verma@example.com'),
(4, 'Suman', 'Patel', 'Finance', 60000.00, '2018-07-30', 'suman.patel@example.com'),
(5, 'Kavita', 'Rao', 'HR', 47000.00, '2020-11-10', 'kavita.rao@example.com'),
(6, 'Amit', 'Gupta', 'Marketing', 52000.00, '2020-09-25', 'amit.gupta@example.com'),
(7, 'Neha', 'Desai', 'IT', 48000.00, '2019-05-18', 'neha.desai@example.com'),
(8, 'Rahul', 'Kumar', 'IT', 53000.00, '2021-02-14', 'rahul.kumar@example.com'),
(9, 'Anjali', 'Mehta', 'Finance', 61000.00, '2018-12-03', 'anjali.mehta@example.com'),
(10, 'Vijay', 'Nair', 'Marketing', 50000.00, '2020-04-19', 'vijay.nair@example.com');