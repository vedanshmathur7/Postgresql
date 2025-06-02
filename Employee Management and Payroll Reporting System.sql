create table departments (
dept_id serial primary key,
dept_name varchar (100) unique not null
);

insert into departments(dept_name)
values
('IT'), ('HR'), ('Finance'), ('Marketing'), ('Operations');

