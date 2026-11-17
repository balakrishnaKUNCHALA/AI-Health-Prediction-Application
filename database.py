import sqlite3

DB_NAME = "health_records.db"


def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            date_of_birth TEXT NOT NULL,
            email TEXT NOT NULL,
            glucose REAL NOT NULL,
            haemoglobin REAL NOT NULL,
            cholesterol REAL NOT NULL,
            remarks TEXT
        )
    """)

    conn.commit()
    conn.close()


def add_patient(full_name, date_of_birth, email, glucose,
                haemoglobin, cholesterol, remarks):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO patients
        (full_name, date_of_birth, email, glucose,
         haemoglobin, cholesterol, remarks)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        full_name,
        date_of_birth,
        email,
        glucose,
        haemoglobin,
        cholesterol,
        remarks
    ))

    conn.commit()
    conn.close()


def get_all_patients():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients ORDER BY id DESC")
    records = cursor.fetchall()

    conn.close()
    return records


def update_patient_email(patient_id, new_email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE patients
        SET email = ?
        WHERE id = ?
    """, (new_email, patient_id))

    conn.commit()
    conn.close()


def delete_patient(patient_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM patients WHERE id = ?",
        (patient_id,)
    )

    conn.commit()
    conn.close()