from function import patientManagement, staffManagement


def main() -> None:
    print("Hospital Simulator")

    while True:
        print("1. Patient Management")
        print("2. Staff Management")
        print("3. Resource Management")
        print("4. Patient Treatment")
        print("5. Emergency Response")
        print("6. Reporting and Analytics")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            patientManagement()

        elif choice == "2":
            staffManagement()

        elif choice == "3":
            resourceManagement()

        elif choice == "4":
            patient_treatment()

        elif choice == "5":
            emergency_response()

        elif choice == "6":
            reporting_and_analytics()

        elif choice == "7":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()