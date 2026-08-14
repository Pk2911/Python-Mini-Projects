import sqlite3
from database import get_connection


def add_patient():
    try:
        name = input("Enter patient name: ")
        age = int(input("Enter age: "))
        gender = input("Enter gender: ")
        phone = input("Enter phone: ")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Patients(name, age, gender, phone)
            VALUES (?, ?, ?, ?)
        """, (name, age, gender, phone))

        conn.commit()
        conn.close()

        print("Patient added successfully.")

    except ValueError:
        print("Age must be a number.")

    except sqlite3.Error as e:
        print("Database error:", e)


def view_patients():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Patients")

        patients = cursor.fetchall()

        conn.close()

        print("\n----- Patients -----")

        if len(patients) == 0:
            print("No patients found.")
            return

        for patient in patients:
            print(
                "ID:", patient[0],
                "| Name:", patient[1],
                "| Age:", patient[2],
                "| Gender:", patient[3],
                "| Phone:", patient[4]
            )

    except sqlite3.Error as e:
        print("Database error:", e)


def update_patient():
    try:
        patient_id = int(input("Enter patient ID: "))

        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        gender = input("Enter new gender: ")
        phone = input("Enter new phone: ")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE Patients
            SET name = ?, age = ?, gender = ?, phone = ?
            WHERE patient_id = ?
        """, (name, age, gender, phone, patient_id))

        conn.commit()

        if cursor.rowcount > 0:
            print("Patient updated successfully.")
        else:
            print("Patient not found.")

        conn.close()

    except ValueError:
        print("Please enter valid values.")

    except sqlite3.Error as e:
        print("Database error:", e)


def delete_patient():
    try:
        patient_id = int(input("Enter patient ID: "))

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM Patients
            WHERE patient_id = ?
        """, (patient_id,))

        conn.commit()

        if cursor.rowcount > 0:
            print("Patient deleted successfully.")
        else:
            print("Patient not found.")

        conn.close()

    except ValueError:
        print("Patient ID must be a number.")

    except sqlite3.Error as e:
        print("Database error:", e)