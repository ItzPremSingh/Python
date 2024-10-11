class Patient:
    _list: list[tuple[str, int, str, str]] = []

    @classmethod
    def add(cls, name: str, age: int, gender: str, condition: str) -> None:
        cls._list.append((name, age, gender, condition))

    @classmethod
    def list(cls) -> list[tuple[str, int, str, str]]:
        return cls._list

    @classmethod
    def discharge(cls, name: str) -> None:
        for i in cls._list:
            if i[0] == name:
                return cls._list.remove(i)

        raise ValueError("Patient not found")
