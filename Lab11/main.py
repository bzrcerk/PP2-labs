import json

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="lab11",
    user="postgres",
    password="123456789",
    port="5432",
)

cursor = conn.cursor()


def call_search_contacts():
    pattern = input("Enter search pattern: ")
    cursor.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    for row in cursor.fetchall():
        print(row)


def call_insert_or_update():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    phone = input("Enter phone: ")
    cursor.execute("CALL insert_or_update_user(%s, %s, %s)", (name, surname, phone))
    conn.commit()
    print("Inserted/Updated.")


def call_insert_many():
    count = int(input("How many users do you want to insert? "))
    data = []
    for _ in range(count):
        name = input("Name: ")
        surname = input("Surname: ")
        phone = input("Phone: ")
        data.append([name, surname, phone])

    json_data = json.dumps(data)
    cursor.execute("CALL insert_many_users(%s::json)", (json_data,))
    conn.commit()
    print("Inserted. Check insert_errors if needed.")


def call_get_paginated():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))
    cursor.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
    for row in cursor.fetchall():
        print(row)


def call_delete_user():
    name = input("Name (or blank): ")
    phone = input("Phone (or blank): ")
    cursor.execute("CALL delete_user(%s, %s)", (name or None, phone or None))
    conn.commit()
    print("Deleted.")


menu = {
    "1": ("Search contacts", call_search_contacts),
    "2": ("Insert or update 1 user", call_insert_or_update),
    "3": ("Insert many users", call_insert_many),
    "4": ("Paginate contacts", call_get_paginated),
    "5": ("Delete user by name/phone", call_delete_user),
    "6": ("Exit", exit),
}

while True:
    print("\nPhoneBook Menu:")
    for key, (desc, _) in menu.items():
        print(f"{key}. {desc}")
    choice = input("Choose option: ").strip()
    if choice in menu:
        menu[choice][1]()
    else:
        print("Invalid choice.")

cursor.close()
conn.close()
