import psycopg2

hostname = 'localhost'
database = 'op'
username = 'postgres'
pwd = '1237'
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
    cur = conn.cursor()
    
    cur.execute("""
        create table if not exists employees (
            emp_id serial primary key,
            fname varchar(50),
            lname varchar(50),
            city varchar(100),
            email varchar(100),
            dept_id int,
            salary numeric(10, 2),
            joining_date date default current_date
        );
    """)
    conn.commit()


    while True:
        print("\n--- employee table menu ---")
        print("1. add new employee")
        print("2. view all employees")
        print("3. update employee city")
        print("4. delete an employee")
        print("5. exit")

        choice = input("enter your choice (1-5): ")

        if choice == '1':
            fname = input("enter first name: ")
            lname = input("enter last name: ")
            city = input("enter city: ")
            email = input("enter email: ")
            dept_id = int(input("enter department id: "))
            salary = float(input("enter salary: "))
            cur.execute("""
                insert into employees (fname, lname, city, email, dept_id, salary)
                values (%s, %s, %s, %s, %s, %s)
            """, (fname, lname, city, email, dept_id, salary))
            conn.commit()
            print("employee added successfully")

        elif choice == '2':
            cur.execute("select * from employees")
            print("\n--- all employees ---")
            for i in cur.fetchall():
                print(i)

        elif choice == '3':
            emp_id = int(input("enter employee id to update: "))
            new_city = input("enter new city: ")
            cur.execute("update employees set city = %s where emp_id = %s", (new_city, emp_id))
            conn.commit()
            print("city updated successfully")

        elif choice == '4':
            emp_id = int(input("enter employee id to delete: "))
            cur.execute("delete from employee_project where emp_id = %s", (emp_id,))
            cur.execute("delete from employees where emp_id = %s", (emp_id,))
            conn.commit()
            print("employee deleted successfully")

        elif choice == '5':
            print("exiting...")
            break

        else:
            print("invalid choice, try again")

except Exception as error:
    print("error:", error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
