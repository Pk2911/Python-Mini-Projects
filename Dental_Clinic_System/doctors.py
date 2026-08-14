import sqlite3
from database import get_connection


def add_doctor():
    try:
        name = input("Enter doctor name: ")
        specialization = input("Enter specialization: ")
        phone = input("Enter phone: ")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Doctors(name, specialization, phone)
            VALUES (?, ?, ?)
        """, (name, specialization, phone))

        conn.commit()
        conn.close()

        print("Doctor added successfully.")

    except sqlite3.Error as e:
        print("Database error:", e)


def view_doctors():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Doctors")

        doctors = cursor.fetchall()

        conn.close()

        print("\n----- Doctors -----")

        if len(doctors) == 0:
            print("No doctors found.")
            return

        for doctor in doctors:
            print(
                "ID:", doctor[0],
                "| Name:", doctor[1],
                "| Specialization:", doctor[2],
                "| Phone:", doctor[3]
            )

    except sqlite3.Error as e:
        print("Database error:", e)


def update_doctor():
    try:
        doctor_id = int(input("Enter doctor ID: "))

        name = input("Enter new name: ")
        specialization = input("Enter new specialization: ")
        phone = input("Enter new phone: ")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE Doctors
            SET name = ?, specialization = ?, phone = ?
            WHERE doctor_id = ?
        """, (name, specialization, phone, doctor_id))

        conn.commit()

        if cursor.rowcount > 0:
            print("Doctor updated successfully.")
        else:
            print("Doctor not found.")

        conn.close()

    except ValueError:
        print("Doctor ID must be a number.")

    except sqlite3.Error as e:
        print("Database error:", e)


def delete_doctor():
    try:
        doctor_id = int(input("Enter doctor ID: "))

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM Doctors
            WHERE doctor_id = ?
        """, (doctor_id,))

        conn.commit()

        if cursor.rowcount > 0:
            print("Doctor deleted successfully.")
        else:
            print("Doctor not found.")

        conn.close()

    except ValueError:
        print("Doctor ID must be a number.")

    except sqlite3.Error as e:
        print("Database error:", e)