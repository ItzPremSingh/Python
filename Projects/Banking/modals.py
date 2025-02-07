from datetime import datetime
from hashlib import sha512
from sqlite3 import connect
from typing import Literal


class User:
    def __init__(self, username: str, password: str | None = None) -> None:
        self.conn = connect("database.db")
        self.cursor = self.conn.cursor()
        self.username = username
        self.password = password

    def __check_for_password(self) -> None:
        """
        Raises a ValueError if the password is None.
        """
        if self.password is None:
            raise ValueError("Password is required")

    def isRegistered(self) -> bool:
        """
        Returns True if the user is registered, False otherwise.
        """
        self.cursor.execute("SELECT * FROM users WHERE username = ?", (self.username,))
        return self.cursor.fetchone() is not None

    def isAuthenticated(self) -> bool:
        """
        Returns True if the user is authenticated, False otherwise.
        """
        self.__check_for_password()
        user = self.cursor.execute(
            "SELECT username FROM users WHERE username = ? AND password = ?",
            (
                self.username,
                sha512(self.password.encode()).hexdigest(),  # type: ignore
            ),
        )
        return user.fetchone() is not None

    def register(self) -> bool:
        """
        Registers the user in the database.
        Returns True if the user is registered, False otherwise.
        """
        self.__check_for_password()
        if not self.isRegistered():
            self.cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (
                    self.username,
                    sha512(self.password.encode()).hexdigest(),  # type: ignore
                ),
            )
            self.conn.commit()
            return True

        return False

    def increaseLoginAttempts(self) -> None:
        """
        Increases the login attempts for the user.
        """
        self.cursor.execute(
            "UPDATE users SET login_attempts = login_attempts + 1 WHERE username = ?",
            (self.username,),
        )
        self.conn.commit()

    def unlock(self) -> None:
        """
        Resets the login attempts and lockout for the user.
        """
        self.cursor.execute(
            "UPDATE users SET login_attempts = 0, login_lockout = NULL WHERE username = ?",
            (self.username,),
        )
        self.conn.commit()

    def lock(self) -> None:
        """
        Sets the login lockout for the user.
        """
        self.cursor.execute(
            "UPDATE users SET login_lockout = datetime('now', 'localtime', '+60 seconds') WHERE username = ?",
            (self.username,),
        )
        self.conn.commit()

    def getLoginAttempts(self) -> int:
        """
        Returns the login attempts for the user.
        """
        self.cursor.execute(
            "SELECT login_attempts FROM users WHERE username = ?", (self.username,)
        )
        return self.cursor.fetchone()[0]

    def getLoginLockout(self) -> datetime | None:
        """
        Returns the login lockout for the user.
        """
        loginLockout = self.cursor.execute(
            "SELECT login_lockout FROM users WHERE username = ?", (self.username,)
        ).fetchone()[0]

        if loginLockout is not None:
            return datetime.strptime(loginLockout, "%Y-%m-%d %H:%M:%S")

        return None

    def isUnlocked(self) -> bool:
        """
        Returns True if the user is unlocked, False otherwise.
        """
        self.cursor.execute(
            "SELECT login_lockout FROM users WHERE username = ?", (self.username,)
        )
        lockedTime = self.cursor.fetchone()[0]

        if lockedTime is None:
            return True

        return datetime.strptime(lockedTime, "%Y-%m-%d %H:%M:%S") < datetime.now()


class UserAccount:
    def __init__(self, username: str) -> None:
        self.conn = connect("database.db")
        self.cursor = self.conn.cursor()
        self.username = username

    def getBalance(self) -> float:
        """
        Returns the balance of the user.
        """
        self.cursor.execute(
            "SELECT balance FROM users WHERE username = ?", (self.username,)
        )
        return float(self.cursor.fetchone()[0])

    def deposit(self, amount: float) -> None:
        """
        Deposits the given amount into the user's account.
        """
        self.cursor.executescript(
            f"""
            UPDATE users SET balance = balance + {amount!r} WHERE username = {self.username!r};
            INSERT INTO transactions (username, amount, type) VALUES ({self.username!r}, {amount!r}, 'deposit');
            """
        )
        self.conn.commit()

    def withdraw(self, amount: float) -> bool:
        """
        Withdraws the given amount from the user's account.
        Returns True if the withdrawal is successful, False otherwise.
        """
        balance = self.cursor.execute(
            "SELECT balance FROM users WHERE username = ?", (self.username,)
        )

        if float(balance.fetchone()[0]) >= amount:
            self.cursor.executescript(
                f"""
                UPDATE users SET balance = balance - {amount!r} WHERE username = {self.username!r};
                INSERT INTO transactions (username, amount, type) VALUES ({self.username!r}, {amount!r}, 'withdrawal');
                """
            )
            self.conn.commit()

            return True

        return False

    def transfer(self, username: str, amount: float) -> bool:
        """
        Transfers the given amount from the user's account to another user.
        Returns True if the transfer is successful, False otherwise.
        """
        if self.getBalance() >= amount:
            self.cursor.executescript(
                f"""
                UPDATE users SET balance = balance + {amount!r} WHERE username = {username!r};
                UPDATE users SET balance = balance - {amount!r} WHERE username = {self.username!r};
                INSERT INTO transactions (username, amount, type) VALUES ({username!r}, {amount!r}, 'receive from {self.username!r}');
                INSERT INTO transactions (username, amount, type) VALUES ({self.username!r}, {amount!r}, 'transfer to {username!r}');
                """
            )
            self.conn.commit()

            return True

        return False

    def getTransactionHistory(
        self,
    ) -> list[
        tuple[int, Literal["deposit", "withdraw", "transfer", "receive"], datetime]
    ]:
        """
        Returns the transaction history for the user.
        """
        data = []
        self.cursor.execute(
            "SELECT amount, type, timestamp FROM transactions WHERE username = ?",
            (self.username,),
        )
        for row in self.cursor.fetchall():
            data.append(
                (row[0], row[1], datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S"))
            )

        return data
