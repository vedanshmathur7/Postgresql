import psycopg2

hostname = 'localhost'
database = 'Employee Management and Payroll Reporting System'
username = 'postgres'
pwd = 1237
port_id = 5432

cur = None
conn = None

try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
    cur = conn.cursor() #creating cursor from the dtb conn

    # dropping tables if they exist to avoid "relation already exists" error during creation
    cur.execute("drop table if exists employee_project;")
    cur.execute("drop table if exists projects;")
    cur.execute("drop table if exists employees;")
    cur.execute("drop table if exists departments;")

    ## creating the table for departments
    cur.execute("""
        create table departments (
        dept_id serial primary key,
        dept_name varchar (100) unique not null
        );""")
    
    ## inserting the data into the table created
    cur.execute("""
        insert into departments(dept_name)
        values
        ('IT'), ('HR'), ('Finance'), ('Marketing'), ('Operations');
        """)
    cur.execute("select * from departments;")
    print ("The generated table 'departments' is : ")
    for i in cur.fetchall():
        print (i)
    print ()    
    
    ## creating the table for employees
    cur.execute("""
        create table employees (
        emp_id serial primary key,
        fname varchar (100) not null,
        lname varchar (100),
        city varchar (100),
        email varchar (100) unique not null,
        dept_id int references departments(dept_id),
        joining_date date not null default current_date,
        salary decimal (7,2) default 30000.00
        );""")
    
    ## inserting the data into the table created
    cur.execute("""
        insert into employees (fname, lname, city, email, dept_id, joining_date, salary)
        values
        ('Raj', 'Sharma', 'Delhi', 'raj.sharma@example.com', 1, '2020-01-15', 50000.00),
        ('Priya', 'Singh', 'Mumbai', 'priya.singh@example.com', 2, '2019-03-22', 45000.00),
        ('Arjun', 'Verma', 'Delhi', 'arjun.verma@example.com', 1, '2021-06-01', 55000.00),
        ('Suman', 'Patel', 'Chennai', 'suman.patel@example.com', 3, '2018-07-30', 60000.00),
        ('Kavita', 'Rao', 'Pune', 'kavita.rao@example.com', 2, '2020-11-10', 47000.00);""")
    
    cur.execute("select * from employees;")
    print ("The generated table 'employees' is : ")
    for i in cur.fetchall():
        print (i)
    print ()  
    
    ## creating the table for projects
    cur.execute("""
        create table projects(
        project_id serial primary key,
        project_name varchar (100),
        dept_id int references departments(dept_id)
        );""")
    
    ## inserting the data into the table created
    cur.execute("""
        insert into projects (project_name, dept_id)
        values
        ('Website Revamp', 1),
        ('Recruitment Drive', 2),
        ('Budget Planning', 3),
        ('Marketing Blitz', 4);""")
    
    cur.execute("select * from projects;")
    print ("The generated table 'projects' is : ")
    for i in cur.fetchall():
        print (i)
    print ()  
    
    ## creating the table for employee_project
    cur.execute("""
        create table employee_project (
        emp_id int references employees(emp_id),
        project_id int references projects(project_id),
        assigned_date date default current_date,
        primary key(emp_id, project_id)
        );""")
    
    ## inserting the data into the table created
    cur.execute("""
        insert into employee_project (emp_id, project_id)
        values
        (1,1), (2,2), (3,1), (4,3), (5,2);""")
    
    cur.execute("select * from employee_project;")
    print ("The generated table 'employee_project' is : ")
    for i in cur.fetchall():
        print (i)
    print ()  
    

    ## performing queries

    ## 1. Adding new employee
    cur.execute("""
        insert into employees (fname, lname, city, email, dept_id, joining_date, salary)
        values 
        ('Rohan','Mehra', 'Bengaluru', 'rohan.mehra@example.com', 2, current_date, 52000.00);""")
    cur.execute("select * from employees;")
    print ("Employees table after adding the new employee : ")
    for i in cur.fetchall():
        print (i)
    print ()  

    # 2. Updating the city of an Employee
    cur.execute("""
        update employees
        set city = 'Jaipur'
        where fname = 'Rohan';
    """)
    cur.execute("select * from employees;")
    print ("Changing the city to Jaipur : ")
    for i in cur.fetchall():
        print (i)
    print ()

    # 3. Deleting employee where fname = 'Suman'
    cur.execute("""
        delete from employee_project 
        where emp_id = 4;
    """)
    cur.execute("""
        delete from employees 
        where emp_id = 4;
    """)
    cur.execute("select * from employees;")
    print ("Generated table after deleting employee 'Suman': ")
    for i in cur.fetchall():
        print (i)
    print ()

    # 4. Showing employees where city contains 'i'
    cur.execute("""
        select * from employees
        where city like '%i%';
    """)
    print ("Employees where the city name contains 'i' in between : ")
    for i in cur.fetchall():
        print (i)
    print ()

    # 5. Employees with salary between 45k and 50k
    cur.execute("""
        select * from employees 
        where salary between 45000 and 50000;
    """)
    print ("Employees having salaries between 45k and 50k : ")
    for i in cur.fetchall():
        print (i)
    print ()

    # 6. Departments in alphabetical order
    cur.execute("""
        select * from departments 
        order by dept_name;
    """)
    print ("Arranging departments in alphabetical order : ")
    for i in cur.fetchall():
        print (i)
    print ()

    # 7. Distinct city names from employees
    cur.execute("""
        select distinct city from employees;
    """)
    print ("Distinct city names from the table 'employees' : ")
    for i in cur.fetchall():
        print (i)
    print ()

    # 8. Average salary of all employees
    cur.execute("""
        select avg(salary) as average_salary from employees;
    """)
    print ("Average salary of all employees : ")
    for i in cur.fetchall():
        print (i)
    print ()

    # 9. Uppercasing fnames of all the employees
    cur.execute("""
        select upper(fname) as upper_fname from employees;
    """)
    print ("Uppercasing fnames of all the employees : ")
    for i in cur.fetchall():
        print (i)
    print ()

    # 10. Extracting domain from the emails
    cur.execute("""
        select email, substring(email from position('@' in email)+1) as domain from employees;
    """)
    print ("Extracting domain from the emails : ")
    for i in cur.fetchall():
        print (i)
    print ()

    # 11. Adding column 'Gender' to employees
    cur.execute("""
        alter table employees 
        add column gender varchar (10);
    """)
    cur.execute("select * from employees;")
    print ("Adding column 'Gender' to employees : ")
    for i in cur.fetchall():
        print (i)
    print ()

    # 12. Changing the size of column 'city'
    cur.execute("""
        alter table employees 
        alter column city
        set data type varchar (150);
    """)
    cur.execute("select * from employees;")
    print ("Changing the size of column 'city' : ")
    for i in cur.fetchall():
        print (i)
    print ()

    # 13. Showing top 3 highest paid employees
    cur.execute("""
        select * from employees 
        order by salary desc limit 3;
    """)
    print ("Showing top 3 highest paid employees : ")
    for i in cur.fetchall():
        print (i)
    print ()


except Exception as error:
    print (error)

    
finally :
    if cur is not None:
        cur.close() 
    if conn is not None :
        conn.close()