import sqlite3
from database import get_connection


def add_treatment():
    try:
        name = input("Enter treatment name: ")
        cost = float(input("Enter treatment cost: "))

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Treatments(treatment_name, cost)
            VALUES (?, ?)
        """, (name, cost))

        conn.commit()
        conn.close()

        print("Treatment added successfully.")

    except ValueError:
        print("Cost must be a number.")

    except sqlite3.Error as e:
        print("Database error:", e)


def view_treatments():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Treatments")

        treatments = cursor.fetchall()

        conn.close()

        print("\n----- Treatments -----")

        if len(treatments) == 0:
            print("No treatments found.")
            return

        for treatment in treatments:
            print(
                "ID:", treatment[0],
                "| Treatment:", treatment[1],
                "| Cost:", treatment[2]
            )

    except sqlite3.Error as e:
        print("Database error:", e)


def update_treatment():
    try:
        treatment_id = int(input("Enter treatment ID: "))

        name = input("Enter new treatment name: ")
        cost = float(input("Enter new cost: "))

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE Treatments
            SET treatment_name = ?, cost = ?
            WHERE treatment_id = ?
        """, (name, cost, treatment_id))

        conn.commit()

        if cursor.rowcount > 0:
            print("Treatment updated successfully.")
        else:
            print("Treatment not found.")

        conn.close()

    except ValueError:
        print("Please enter valid values.")

    except sqlite3.Error as e:
        print("Database error:", e)


def delete_treatment():
    try:
        treatment_id = int(input("Enter treatment ID: "))

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM Treatments
            WHERE treatment_id = ?
        """, (treatment_id,))

        conn.commit()

        if cursor.rowcount > 0:
            print("Treatment deleted successfully.")
        else:
            print("Treatment not found.")

        conn.close()

    except ValueError:
        print("Treatment ID must be a number.")

    except sqlite3.Error as e:
        print("Database error:", e)