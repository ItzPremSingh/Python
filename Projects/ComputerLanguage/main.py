from typing import Literal

hexa = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}


def pair(data: str, of: int) -> list[str]:
    data = data[::-1]
    _pair: list[str] = []

    n = len(data) // of + (1 if len(data) % of else 0)
    for i in range(n):
        _pair.append((data[i * of : (i * of) + of])[::-1].zfill(of))

    return _pair[::-1]


class Binary:
    def __init__(self, binary: str) -> None:
        self.binary = binary
        self.parse()

    @property
    def base(self) -> Literal[2]:
        return 2

    def toDecmial(self) -> int:
        _decmial = 0
        base = self.base
        for power, binary in enumerate(self.binary[::-1]):
            _decmial += int(binary) * pow(base, power)

        return _decmial

    def toOctal(self) -> int:
        _octal = ""
        for binary in pair(self.binary, 3):
            _octal += str(Binary(binary).toDecmial())

        return int(_octal)

    def toHexdecmial(self) -> str:
        _hex = ""
        for binary in pair(self.binary, 4):
            hex = Binary(binary).toDecmial()
            _hex += str(hex) if hex < 10 else str(hexa[hex])

        return _hex

    def parse(self) -> None:
        for n in self.binary:
            if n not in {"0", "1"}:
                raise


class Decmial:
    def __init__(self, decmial: int) -> None:
        self.decmial = decmial
        self.parse()

    def parse(self) -> None:
        if not str(self.decmial).isdigit():
            raise

    def toBinary(self) -> str:
        _binary: list[str] = []

        while True:
            _binary.append(str(self.decmial % 2))
            self.decmial //= 2
            if self.decmial <= 1:
                _binary.append(str(self.decmial))
                break

        return "".join(_binary[::-1])

    def toOctal(self) -> str:
        _octal: list[str] = []

        while True:
            _octal.append(str(self.decmial % 8))
            self.decmial //= 8
            if self.decmial <= 1:
                _octal.append(str(self.decmial))
                break

        return "".join(_octal[::-1])

    def toHexdecmial(self) -> str:
        _hexa: list[str] = []

        while True:
            _hexa.append(str(self.decmial % 16))
            self.decmial //= 16
            if self.decmial <= 1:
                _hexa.append(
                    str(hexa[self.decmial] if self.decmial > 9 else self.decmial)
                )
                break

        return "".join(_hexa[::-1])


binary = Decmial(466)
print(binary.toHexdecmial())

print(hex(466))
