import sqlite3

DB_NAME = "dental_clinic.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    #Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)

    #Doctors table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Doctors (
            doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            specialization TEXT NOT NULL,
            phone TEXT
        )
    """)

    #Patients table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Patients (
            patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    """)

    #Treatments table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Treatments (
            treatment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            treatment_name TEXT NOT NULL,
            cost REAL NOT NULL
        )
    """)

    #Appointments table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Appointments (
            appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            doctor_id INTEGER,
            treatment_id INTEGER,
            appointment_date TEXT,
            appointment_time TEXT,
            status TEXT,

            FOREIGN KEY (patient_id)
                REFERENCES Patients(patient_id),

            FOREIGN KEY (doctor_id)
                REFERENCES Doctors(doctor_id),

            FOREIGN KEY (treatment_id)
                REFERENCES Treatments(treatment_id)
        )
    """)

    #Create main admin
    cursor.execute("""
        SELECT * FROM Users
        WHERE username = 'pankaj'
    """)

    if cursor.fetchone() is None:
        cursor.execute("""
            INSERT INTO Users(username, password, role)
            VALUES ('pankaj', '12345678Pk*', 'Admin')
        """)

    conn.commit()
    conn.close()

    print("Database ready.")


if __name__ == "__main__":
    create_tables()