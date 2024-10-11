from datetime import datetime


class Birthday:
    def __init__(self, birthday: datetime) -> None:
        self.birthday = birthday

    @property
    def next_birthday(self) -> datetime:
        """
        A property method to calculate the next birthday based on the current date and the stored birthday.
        Return:
            datetime: The next birthday date.
        """
        today = datetime.now()
        year = today.year
        month = self.birthday.month
        day = self.birthday.day
        if today.month > month or (today.month == month and today.day >= day):
            year += 1

        days = datetime(year, month, day) - today


if __name__ == "__main__":
    print("hello")
    print("hello, world")
    # birthday = Birthday(datetime(2008, 12, 1))
    # print(birthday.next_birthday)
