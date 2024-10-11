from datetime import datetime

from common.helper import onlyNumber
from common.setting import adminPassword
from .db.room import Room

from ...Package.myorm.comparison import gte, lte


def inroom(number: int):
    while True:
        print("1. Check Out")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Check Out")

            checkInDateTime = datetime.strptime(
                Room.get(number=number)["checkInDateTime"], "%Y-%m-%d %H:%M:%S"  # type: ignore
            )
            curentDateTime = datetime.now()

            price = Room.get(number=number)["price"]
            Room.update(("number", number), checkInDateTime=None, isAvailable=1)

            print("Invoice:")
            print(f"Check In Time: {checkInDateTime}")
            print(f"Check Out Time: {curentDateTime}")
            print(
                f"Total Amount: {((curentDateTime - checkInDateTime).seconds * price)}"
            )

            return

        else:
            print("Invalid choice. Please try again.")


def user():
    while True:
        print("1. View Rooms")
        print("2. Book Room")
        print("3. Cancel Booking")
        print("4. Check In")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("View Rooms")

            numberOfpeople = int(input("Enter number of people: "))
            prefType = str(input("Enter preferred type: "))
            priceRange = float(input("Enter price range: "))

            rooms = Room.filter(capacity=gte(numberOfpeople), type=prefType, price=lte(priceRange), isAvailable=1)  # type: ignore

            for room in rooms:
                print(f"Number: {room['number']}")
                print(f"Type: {room['type']}")
                print(f"Capacity: {room['capacity']}")
                print(f"Price: {room['price']}")

        if choice == 2:
            print("Book Room")

            number = int(input("Enter room number: "))

            Room.update(("number", number), isAvailable=0)

        elif choice == 3:
            print("Cancel Booking")

            number = int(input("Enter room number: "))
            
            Room.update(("number", number), isAvailable=1)

        elif choice == 4:
            print("Check In")

            number = int(input("Enter room number: "))

            cursor.execute(
                """
                UPDATE Room SET checkInDateTime = CURRENT_TIMESTAMP WHERE number = ?
            """,
                (number,),
            )
            connection.commit()

            inroom(number)

        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")


def admin():
    while True:
        print("1. Add Room")
        print("2. Update Room")
        print("3. Delete Room")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Add Room")
            type = input("Enter room type: ")
            capacity = int(input("Enter room capacity: "))
            price = float(input("Enter room price: "))

            cursor.execute(
                """
                INSERT INTO Room (type, capacity, price) VALUES (?, ?, ?)
            """,
                (type, capacity, price),
            )
            connection.commit()

        elif choice == 2:
            print("Update Room")
            number = int(input("Enter room number: "))
            price = float(input("Enter new price: "))

            cursor.execute(
                """
                UPDATE Room SET price = ? WHERE number = ?
            """,
                (price, number),
            )
            connection.commit()

        elif choice == 3:
            print("Delete Room")
            number = int(input("Enter room number: "))

            cursor.execute(
                """
                DELETE FROM Room WHERE number = ?
            """,
                (number,),
            )
            connection.commit()

        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")


def guest():
    while True:
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Sign Up")
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            phone = int(input("Enter your phone number: "))
            password = input("Enter your password: ")

            cursor.execute(
                """
                INSERT INTO User (name, email, phone, password) VALUES (?, ?, ?, ?)
            """,
                (name, email, phone, password),
            )
            connection.commit()

            user()

        elif choice == 2:
            print("Log In")
            email = input("Enter your email: ")
            password = input("Enter your password: ")

            cursor.execute(
                """
                SELECT * FROM User WHERE email = ? AND password = ?
            """,
                (email, password),
            )

            user()

        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    while True:
        print("1. Admin")
        print("2. Guest")
        print("3. Exit")

        choice = onlyNumber()

        if choice == 1:
            password = input("Enter admin password: ")
            if password == adminPassword:
                admin()

            else:
                print("password is wrong")

        elif choice == 2:
            guest()

        elif choice == 3:
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    from db.room import createTable

    createTable()

    from db.user import createTable

    createTable()

    main()
