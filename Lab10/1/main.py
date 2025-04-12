import csv

import psycopg2

file_name = "list.csv"

conn = psycopg2.connect(
    host="localhost",
    database="lab10",
    user="postgres",
    password="123456789",
    port="5432",
)


def create_table():
    command = """
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            sur_name VARCHAR(50) NOT NULL,
            phone VARCHAR(15) NOT NULL
        )
    """
    with conn.cursor() as cursor:
        cursor.execute(command)
        conn.commit()


def insert_data(csv_file):
    command = "INSERT INTO contacts (name, sur_name, phone) VALUES (%s, %s, %s)"

    with conn.cursor() as cursor:
        with open(csv_file, mode="r", newline="") as file:
            csvreader = csv.reader(file, delimiter=",")
            next(csvreader)  # Skip the header row
            for row in csvreader:
                name, sur_name, phone = row
                print(name, sur_name, phone)
                cursor.execute(command, (name, sur_name, phone))
        conn.commit()


def select_data():
    command = "SELECT * FROM contacts"
    with conn.cursor() as cursor:
        cursor.execute(command)
        rows = cursor.fetchall()
        for row in rows:
            print(row)


create_table()

# insert_data(file_name)

menu = [
    "1. Create table",
    "2. Insert data",
    "3. Select data",
    "4. Delete user",
    "5. Exit",
]
select_data_menu = [
    "1. Select data in descending order by id",
    "2. Select data in ascending order by id",
    "3. Select data by name",
    "4. Select data by sur_name",
    "5. Select data by phone",
]

delete_data_menu = [
    "1. Delete data by id",
    "2. Delete data by name",
    "3. Delete data by phone",
]

while True:
    print("\nMenu:")
    for item in menu:
        print(item)
    choice = input("Enter your choice: ")

    if choice == "1":
        create_table()

    elif choice == "2":
        entering_str = input("Enter name, sur_name, phone separated by space: ").split()
        if len(entering_str) != 3:
            print("Invalid input.")
            continue
        name, sur_name, phone = entering_str
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO contacts (name, sur_name, phone) VALUES (%s, %s, %s)",
                (name, sur_name, phone),
            )
            conn.commit()
            print("Data inserted successfully.")

    elif choice == "3":
        print("Select data menu:")
        for item in select_data_menu:
            print(item)
        sub_choice = input("Enter your choice: ")

        if sub_choice == "1":
            command = "SELECT * FROM contacts ORDER BY id DESC"
            params = ()

        elif sub_choice == "2":
            command = "SELECT * FROM contacts ORDER BY id ASC"
            params = ()

        elif sub_choice == "3":
            name = input("Enter name: ")
            command = "SELECT * FROM contacts WHERE name = %s"
            params = (name,)

        elif sub_choice == "4":
            sur_name = input("Enter sur_name: ")
            command = "SELECT * FROM contacts WHERE sur_name = %s"
            params = (sur_name,)

        elif sub_choice == "5":
            phone = input("Enter phone: ")
            command = "SELECT * FROM contacts WHERE phone = %s"
            params = (phone,)

        else:
            print("Invalid choice. Please try again.")
            continue

        with conn.cursor() as cursor:
            cursor.execute(command, params)
            rows = cursor.fetchall()
            for row in rows:
                print(row)

    elif choice == "4":
        print("Delete data menu:")
        for item in delete_data_menu:
            print(item)
        sub_choice = input("Enter your choice: ")

        if sub_choice == "1":
            id = input("Enter id: ")
            command = "DELETE FROM contacts WHERE id = %s"
            params = (id,)

        elif sub_choice == "2":
            name = input("Enter name: ")
            command = "DELETE FROM contacts WHERE name = %s"
            params = (name,)

        elif sub_choice == "3":
            phone = input("Enter phone: ")
            command = "DELETE FROM contacts WHERE phone = %s"
            params = (phone,)

        else:
            print("Invalid choice. Please try again.")
            continue

        with conn.cursor() as cursor:
            cursor.execute(command, params)
            conn.commit()
            print("Data deleted successfully.")
    elif choice == "5":
        break

    else:
        print("Invalid choice. Please try again.")

conn.close()
