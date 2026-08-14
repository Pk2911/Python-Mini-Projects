import sqlite3
from database import get_connection


def book_appointment():
    try:
        patient_id = int(input("Enter patient ID: "))
        doctor_id = int(input("Enter doctor ID: "))
        treatment_id = int(input("Enter treatment ID: "))

        date = input("Enter appointment date (YYYY-MM-DD): ")
        time = input("Enter appointment time (HH:MM): ")

        conn = get_connection()
        cursor = conn.cursor()

        # Check if patient exists
        cursor.execute(
            "SELECT * FROM Patients WHERE patient_id = ?",
            (patient_id,)
        )

        if cursor.fetchone() is None:
            print("Patient not found.")
            conn.close()
            return

        # Check if doctor exists
        cursor.execute(
            "SELECT * FROM Doctors WHERE doctor_id = ?",
            (doctor_id,)
        )

        if cursor.fetchone() is None:
            print("Doctor not found.")
            conn.close()
            return

        # Check if treatment exists
        cursor.execute(
            "SELECT * FROM Treatments WHERE treatment_id = ?",
            (treatment_id,)
        )

        if cursor.fetchone() is None:
            print("Treatment not found.")
            conn.close()
            return

        # Insert appointment
        cursor.execute("""
            INSERT INTO Appointments
            (patient_id, doctor_id, treatment_id,
             appointment_date, appointment_time, status)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            patient_id,
            doctor_id,
            treatment_id,
            date,
            time,
            "Scheduled"
        ))

        conn.commit()
        conn.close()

        print("Appointment booked successfully.")

    except ValueError:
        print("IDs must be numbers.")

    except sqlite3.Error as e:
        print("Database error:", e)


def view_appointments():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                Appointments.appointment_id,
                Patients.name,
                Doctors.name,
                Treatments.treatment_name,
                Appointments.appointment_date,
                Appointments.appointment_time,
                Appointments.status

            FROM Appointments

            JOIN Patients
            ON Appointments.patient_id = Patients.patient_id

            JOIN Doctors
            ON Appointments.doctor_id = Doctors.doctor_id

            JOIN Treatments
            ON Appointments.treatment_id = Treatments.treatment_id
        """)

        appointments = cursor.fetchall()

        conn.close()

        print("\n----- Appointments -----")

        if len(appointments) == 0:
            print("No appointments found.")
            return

        for appointment in appointments:
            print(
                "ID:", appointment[0],
                "| Patient:", appointment[1],
                "| Doctor:", appointment[2],
                "| Treatment:", appointment[3],
                "| Date:", appointment[4],
                "| Time:", appointment[5],
                "| Status:", appointment[6]
            )

    except sqlite3.Error as e:
        print("Database error:", e)


def update_appointment():
    try:
        appointment_id = int(input("Enter appointment ID: "))

        date = input("Enter new date (YYYY-MM-DD): ")
        time = input("Enter new time (HH:MM): ")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE Appointments
            SET appointment_date = ?,
                appointment_time = ?
            WHERE appointment_id = ?
        """, (date, time, appointment_id))

        conn.commit()

        if cursor.rowcount > 0:
            print("Appointment updated successfully.")
        else:
            print("Appointment not found.")

        conn.close()

    except ValueError:
        print("Appointment ID must be a number.")

    except sqlite3.Error as e:
        print("Database error:", e)


def cancel_appointment():
    try:
        appointment_id = int(input("Enter appointment ID: "))

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE Appointments
            SET status = 'Cancelled'
            WHERE appointment_id = ?
        """, (appointment_id,))

        conn.commit()

        if cursor.rowcount > 0:
            print("Appointment cancelled.")
        else:
            print("Appointment not found.")

        conn.close()

    except ValueError:
        print("Appointment ID must be a number.")

    except sqlite3.Error as e:
        print("Database error:", e)


def view_patient_history():
    try:
        patient_id = int(input("Enter patient ID: "))

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                Patients.name,
                Appointments.appointment_date,
                Doctors.name,
                Treatments.treatment_name,
                Treatments.cost,
                Appointments.status

            FROM Appointments

            JOIN Patients
            ON Appointments.patient_id = Patients.patient_id

            JOIN Doctors
            ON Appointments.doctor_id = Doctors.doctor_id

            JOIN Treatments
            ON Appointments.treatment_id = Treatments.treatment_id

            WHERE Patients.patient_id = ?
        """, (patient_id,))

        history = cursor.fetchall()

        conn.close()

        print("\n----- Patient Treatment History -----")

        if len(history) == 0:
            print("No history found.")
            return

        for record in history:
            print(
                "Patient:", record[0],
                "| Date:", record[1],
                "| Doctor:", record[2],
                "| Treatment:", record[3],
                "| Cost:", record[4],
                "| Status:", record[5]
            )

    except ValueError:
        print("Patient ID must be a number.")

    except sqlite3.Error as e:
        print("Database error:", e)