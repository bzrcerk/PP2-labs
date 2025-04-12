import psycopg2

sql = r"""
CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    sur_name VARCHAR(50) NOT NULL,
    phone VARCHAR(15) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS insert_errors (
    id SERIAL PRIMARY KEY,
    entry TEXT,
    error_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Явное указание колонок вместо SELECT * для соответствия возвращаемому типу
CREATE OR REPLACE FUNCTION search_contacts(pattern TEXT)
RETURNS TABLE(id INT, name TEXT, sur_name TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.name::TEXT, c.sur_name::TEXT, c.phone::TEXT
    FROM contacts c
    WHERE c.name ILIKE '%' || pattern || '%'
       OR c.sur_name ILIKE '%' || pattern || '%'
       OR c.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name TEXT, p_surname TEXT, p_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name AND sur_name = p_surname) THEN
        UPDATE contacts SET phone = p_phone WHERE name = p_name AND sur_name = p_surname;
    ELSE
        INSERT INTO contacts(name, sur_name, phone) VALUES(p_name, p_surname, p_phone);
    END IF;
END;
$$;

-- Удаляем старую версию, чтобы избежать конфликта типов
DROP PROCEDURE IF EXISTS insert_many_users(TEXT[][]);
DROP PROCEDURE IF EXISTS insert_many_users(JSON);

-- Обновлённая версия: принимает JSON
CREATE OR REPLACE PROCEDURE insert_many_users(data JSON)
LANGUAGE plpgsql
AS $$
DECLARE
    item JSON;
    name TEXT;
    surname TEXT;
    phone TEXT;
BEGIN
    FOR item IN SELECT * FROM json_array_elements(data)
    LOOP
        name := item->>0;
        surname := item->>1;
        phone := item->>2;

        IF phone ~ '^\d{10,15}$' THEN
            BEGIN
                INSERT INTO contacts(name, sur_name, phone)
                VALUES(name, surname, phone);
            EXCEPTION WHEN OTHERS THEN
                INSERT INTO insert_errors(entry) VALUES (name || ' ' || surname || ' ' || phone);
            END;
        ELSE
            INSERT INTO insert_errors(entry) VALUES (name || ' ' || surname || ' ' || phone);
        END IF;
    END LOOP;
END;
$$;

CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, name TEXT, sur_name TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.name::TEXT, c.sur_name::TEXT, c.phone::TEXT
    FROM contacts c
    ORDER BY c.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE delete_user(p_username TEXT, p_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM contacts
    WHERE name = p_username OR phone = p_phone;
END;
$$;
"""

conn = psycopg2.connect(
    host="localhost",
    database="lab11",
    user="postgres",
    password="123456789",
    port="5432",
)

with conn.cursor() as cursor:
    cursor.execute(sql)
    conn.commit()

conn.close()
print("Database initialized successfully.")
