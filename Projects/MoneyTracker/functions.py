from datetime import datetime
from sqlite3 import Cursor

"""Provide some important function"""


def insertRecord(
    _cursor: Cursor, amount: int, description: str, transactionType: str, balance: int
) -> None:
    _cursor.execute(
        """
        INSERT INTO Money (
            transactionDate, description, amount, transactionType, balance
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            datetime.now().date(),
            description,
            amount,
            transactionType,
            balance,
        ),
    )


def lastBalance(_cursor: Cursor) -> int:
    _cursor.execute(
        """
        SELECT balance
        FROM Money
        ORDER BY transactionID DESC
        LIMIT 1
        """
    )

    result = _cursor.fetchone()
    return result[0] if result else 0


def fetchRecord(_cursor: Cursor, _range: int) -> list:
    _cursor.execute(
        f"""
            SELECT transactionID, transactionDate, description, amount, transactionType, balance
            FROM Money
            ORDER BY transactionID DESC LIMIT {_range}
        """
    )
    return _cursor.fetchall()


def listRecord(_cursor: Cursor, _range: int) -> None:
    allRecord = fetchRecord(_cursor, _range)[::-1]
    lastDate = ""

    if allRecord:
        lastDate = allRecord[0][1]

    else:
        print("No transaction done")
        return

    for _, issuedDate, reason, amount, _type, balance in allRecord:
        dateObj = datetime.strptime(issuedDate, "%Y-%m-%d")
        date = f"{dateObj.day}-{dateObj.month}-{dateObj.year}"
        if date != lastDate:
            lastDate = date
            print(f"Date: \033[96m{date}\33[m\n")

        colorCode = "\033[92m" if _type == "credit" else "\033[91m"

        print(f"Amount  -> {amount} ({colorCode}{_type.title()}\033[0m)")
        print(f"Reason  -> {reason}")
        print(f"Balance -> {balance}")

        print()


def updateRecord(_cursor: Cursor, _id: int, update: dict[str, str | int]) -> None:
    updateColumn = [f"{column} = ?" for column in update.keys()]
    updateValue = tuple(update.values())

    _cursor.execute(
        f"""
        UPDATE Money
        SET {", ".join(updateColumn)}
        WHERE transactionID = {_id}
        """,
        updateValue,
    )
