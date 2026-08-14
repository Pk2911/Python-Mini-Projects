from database import create_tables

from auth import login, add_receptionist

from patients import (
    add_patient,
    view_patients,
    update_patient,
    delete_patient
)

from doctors import (
    add_doctor,
    view_doctors,
    update_doctor,
    delete_doctor
)

from treatments import (
    add_treatment,
    view_treatments,
    update_treatment,
    delete_treatment
)

from appointments import (
    book_appointment,
    view_appointments,
    update_appointment,
    cancel_appointment,
    view_patient_history
)


# ---------------- PATIENT MENU ----------------

def patient_menu():

    while True:

        print("\n===== PATIENT MENU =====")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            add_patient()

        elif choice == "2":
            view_patients()

        elif choice == "3":
            update_patient()

        elif choice == "4":
            delete_patient()

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


# ---------------- DOCTOR MENU ----------------

def doctor_menu():

    while True:

        print("\n===== DOCTOR MENU =====")
        print("1. Add Doctor")
        print("2. View Doctors")
        print("3. Update Doctor")
        print("4. Delete Doctor")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            add_doctor()

        elif choice == "2":
            view_doctors()

        elif choice == "3":
            update_doctor()

        elif choice == "4":
            delete_doctor()

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


# ---------------- TREATMENT MENU ----------------

def treatment_menu():

    while True:

        print("\n===== TREATMENT MENU =====")
        print("1. Add Treatment")
        print("2. View Treatments")
        print("3. Update Treatment")
        print("4. Delete Treatment")
        print("5. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            add_treatment()

        elif choice == "2":
            view_treatments()

        elif choice == "3":
            update_treatment()

        elif choice == "4":
            delete_treatment()

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


#

def appointment_menu():

    while True:

        print("\n===== APPOINTMENT MENU =====")
        print("1. Book Appointment")
        print("2. View Appointments")
        print("3. Update Appointment")
        print("4. Cancel Appointment")
        print("5. View Patient History")
        print("6. Back")

        choice = input("Enter choice: ")

        if choice == "1":
            book_appointment()

        elif choice == "2":
            view_appointments()

        elif choice == "3":
            update_appointment()

        elif choice == "4":
            cancel_appointment()

        elif choice == "5":
            view_patient_history()

        elif choice == "6":
            break

        else:
            print("Invalid choice.")


# ---------------- ADMIN MENU ----------------

def admin_menu():

    while True:

        print("\n========== ADMIN MENU ==========")
        print("1. Manage Doctors")
        print("2. Manage Patients")
        print("3. Manage Treatments")
        print("4. Manage Appointments")
        print("5. Add Receptionist")
        print("6. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            doctor_menu()

        elif choice == "2":
            patient_menu()

        elif choice == "3":
            treatment_menu()

        elif choice == "4":
            appointment_menu()

        elif choice == "5":
            add_receptionist()

        elif choice == "6":
            print("Logged out.")
            break

        else:
            print("Invalid choice.")


# ---------------- RECEPTIONIST MENU ----------------

def receptionist_menu():

    while True:

        print("\n====== RECEPTIONIST MENU ======")
        print("1. Manage Patients")
        print("2. Manage Appointments")
        print("3. View Patient History")
        print("4. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            patient_menu()

        elif choice == "2":
            appointment_menu()

        elif choice == "3":
            view_patient_history()

        elif choice == "4":
            print("Logged out.")
            break

        else:
            print("Invalid choice.")


# ---------------- MAIN PROGRAM ----------------

def main():

    create_tables()

    while True:

        print("\n==============================")
        print("   DENTAL CLINIC MANAGEMENT")
        print("==============================")
        print("1. Login")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            user = login()

            if user:

                # user[2] contains the role

                if user[2] == "Admin":
                    admin_menu()

                elif user[2] == "Receptionist":
                    receptionist_menu()

        elif choice == "2":

            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice.")


main()