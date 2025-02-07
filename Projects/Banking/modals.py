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
        if self.password is None:
            raise ValueError("Password is required")

    def isRegistered(self) -> bool:
        self.cursor.execute("SELECT * FROM users WHERE username = ?", (self.username,))
        return self.cursor.fetchone() is not None

    def isAuthenticated(self) -> bool:
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
        self.cursor.execute(
            "UPDATE users SET login_attempts = login_attempts + 1 WHERE username = ?",
            (self.username,),
        )
        self.conn.commit()

    def unlock(self) -> None:
        self.cursor.execute(
            "UPDATE users SET login_attempts = 0, login_lockout = NULL WHERE username = ?",
            (self.username,),
        )
        self.conn.commit()

    def lock(self) -> None:
        self.cursor.execute(
            "UPDATE users SET login_lockout = datetime('now', 'localtime', '+60 seconds') WHERE username = ?",
            (self.username,),
        )
        self.conn.commit()

    def getLoginAttempts(self) -> int:
        self.cursor.execute(
            "SELECT login_attempts FROM users WHERE username = ?", (self.username,)
        )
        return self.cursor.fetchone()[0]

    def getLoginLockout(self) -> datetime | None:
        loginLockout = self.cursor.execute(
            "SELECT login_lockout FROM users WHERE username = ?", (self.username,)
        ).fetchone()[0]

        if loginLockout is not None:
            return datetime.strptime(loginLockout, "%Y-%m-%d %H:%M:%S")

        return None

    def isUnlocked(self) -> bool:
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
        self.cursor.execute(
            "SELECT balance FROM users WHERE username = ?", (self.username,)
        )
        return float(self.cursor.fetchone()[0])

    def deposit(self, amount: float) -> None:
        self.cursor.executescript(
            f"""
            UPDATE users SET balance = balance + {amount!r} WHERE username = {self.username!r};
            INSERT INTO transactions (username, amount, type) VALUES ({self.username!r}, {amount!r}, 'deposit');
            """
        )
        self.conn.commit()

    def withdraw(self, amount: float) -> bool:
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
