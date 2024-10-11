class Staff:
    _list: list[tuple[str, str]] = []

    @classmethod
    def add(cls, name: str, role: str) -> None:
        cls._list.append((name, role))

    @classmethod
    def list(cls) -> list[tuple[str, str]]:
        return cls._list
