import psycopg2

hostname = 'localhost'
database = 'op'
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
        print("\n--- Employee table menu ---")
        print("1. Add new employee")
        print("2. View all employees")
        print("3. Update employee city")
        print("4. Delete an employee")
        print("5. Exit")

        choice = input("enter your choice (1-5): ")

        if choice == '1':
            fname = input("Enter first name: ")
            lname = input("Enter last name: ")
            city = input("Enter city: ")
            email = input("Enter email: ")
            dept_id = int(input("Enter department id: "))
            salary = float(input("Enter salary: "))
            cur.execute("""
                insert into employees (fname, lname, city, email, dept_id, salary)
                values (%s, %s, %s, %s, %s, %s)
            """, (fname, lname, city, email, dept_id, salary))
            conn.commit()
            print("Employee added successfully! ")

        elif choice == '2':
            cur.execute("select * from employees")
            print("\n--- All employees ---")
            for i in cur.fetchall():
                print(i)

        elif choice == '3':
            emp_id = int(input("Enter employee id to update: "))
            new_city = input("Enter new city: ")
            cur.execute("Update employees set city = %s where emp_id = %s", (new_city, emp_id))
            conn.commit()
            print("City updated successfully")

        elif choice == '4':
            emp_id = int(input("Enter employee id to delete: "))
            cur.execute("Delete from employees where emp_id = %s", (emp_id,))
            conn.commit()
            print("Employee deleted successfully")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice, try again")

except Exception as error:
    print("error:", error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
