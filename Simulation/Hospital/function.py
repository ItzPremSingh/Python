from staff import Staff
from patient import Patient


def patientManagement() -> None:
    while True:
        print("1. Add Patient")
        print("2. List Patients")
        print("3. Discharge Patient")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Enter patient details:")
            Patient.add(
                input("Name: "),
                int(input("Age: ")),
                input("Gender: "),
                input("Medical Condition: "),
            )

            print("Patient added successfully!")

        elif choice == "2":
            print("List of Patients:")
            for i in Patient.list():
                print(
                    f"\nName: {i[0]}\nAge: {i[1]}\nGender: {i[2]}\nMedical Condition: {i[3]}"
                )

        elif choice == "3":
            print("Discharge Patient")
            Patient.discharge(input("Name: "))

            print("Patient discharged successfully!")

        elif choice == "4":
            return

        else:
            print("Invalid choice")


def staffManagement() -> None:
    while True:
        print("1. Add Staff")
        print("2. List Staff")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Enter staff details:")
            Staff.add(
                input("Name: "),
                input("Role: "),
            )

            print("Staff added successfully!")

        elif choice == "2":
            print("List of Staff:")
            for i in Staff.list():
                print(f"\nName: {i[0]}\nRole: {i[1]}")

        elif choice == "3":
            return

        else:
            print("Invalid choice")
