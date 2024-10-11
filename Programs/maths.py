def _fractionCal(*fractions):
    """Common the denominator"""
    numerator = []
    denominator = []

    for _fraction in fractions:
        if len(_fraction) == 2:
            if _fraction[1] < 0:
                numerator.append(_fraction[0] * -1)
                denominator.append(_fraction[1] * -1)

            else:
                numerator.append(_fraction[0])
                denominator.append(_fraction[1])

        elif len(_fraction) == 1:
            numerator.append(_fraction[0])
            denominator.append(1)

        else:
            pass

    newDenom = _lcm(*denominator)
    newNumer = []

    for _ in range(len(numerator)):
        multi = newDenom // denominator[_]
        newNumer.append(numerator[_] * multi)

    return newNumer, newDenom


def _common(_list):
    """Return list of common element"""
    _common = []
    for element in _list:
        if element not in _common:
            _common.append(element)

    return _common


def _seprater(_list, seprate=2):
    """Returns list of tuple"""
    sepList = []
    start = 0
    end = seprate

    for _ in range(len(_list) // seprate):
        sepList.append(tuple(_list[start:end]))
        start = end
        end = end + seprate

    return sepList


def _commonise(*numbers):
    """Retuns common from all number's factor"""
    _factors = []
    _divisor = 2
    _commonise = []

    for number in numbers:
        _factors.append(factor(abs(number)))

    runtime = _maxlen(_factors) * 3

    while True:
        _common = True
        for _factor in _factors:
            if _divisor not in _factor:
                _common = False
                break

        if _divisor == runtime:
            return _commonise, tuple(_factors)

        if not _common:
            _divisor += 1
            continue

        else:
            for _factor in _factors:
                _factor.remove(_divisor)

            _commonise.append(_divisor)


def _maxlen(*iterator):
    """Returns maximum len"""
    _maxlen = 0
    for number in iterator:
        if len(number) > _maxlen:
            _maxlen = len(number)

    return _maxlen


def _minlen(*iterator):
    """Returns minimum len"""
    _minlen = 0
    for number in iterator:
        if len(number) < _minlen:
            _minlen = len(number)

    return _minlen


def _lcm(*numbers):
    """Returns LCM of numbers"""
    if allprime(*numbers):
        return product(*numbers)

    _common = _commonise(*numbers)[1]
    _lcm = 1

    for _com in _common:
        _lcm *= product(*_com)

    return _lcm


def _combine(*numbers):
    """Return tuple contain repeatation of number"""
    _dict = dict()

    for number in numbers:
        if number not in _dict:
            _dict.setdefault(number, 1)

        else:
            total = _dict.get(number)
            _dict[number] = total + 1

    return tuple(_dict.items())


def fabonaci(time=10):
    """Returns the fabonaci series"""
    value = []
    start = 0
    end = 1
    temp = 0

    for _ in range(time):
        value.append(start)
        temp = start + end
        start = end
        end = temp

    return value


def fabonplace(place):
    """Return fabonaci number"""
    return fabonaci(place)[-1]


def isarmstrong(number):
    """Return true when the number is armstrong"""
    totalSum = 0
    numStr = str(number)
    numLen = len(numStr)
    for numbers in numStr:
        totalSum += int(numbers) ** numLen

    if totalSum == number:
        value = True
    else:
        value = False

    return value


def isprime(number):
    """Return number is prime or not"""
    if number % 2 == 0 or number != 2:
        return False

    for divider in range(2, number // 2 + 1):
        if number % divider == 0:
            return False

    return True


def allprime(*numbers):
    """Returns true when all the numbers are prime or Returns false"""
    for number in numbers:
        if not isprime(number):
            return False

    return True


def iseven(number):
    """Returns true when the number is even"""
    if number % 2 == 0:
        return True

    return False


def isodd(number):
    """Returns true when the number is odd"""
    return not iseven(number)


def coprime(*numbers):
    """Returns true when all number are prime"""
    return allprime(*numbers)


def twinprime(first, second):
    """Returns true when the numbers is twinprime"""
    if first + 2 == second:
        return allprime(first, second)

    return False


def greater(*numbers):
    """Returns greater number"""
    greatNum = 0

    for num in numbers:
        if num > greatNum:
            greatNum = num

    return greatNum


def lower(*numbers):
    """Returns lower number"""
    lowerNum = 0

    for num in numbers:
        if num < lowerNum:
            lowerNum = num

    return lowerNum


def factor(number):
    """Returns factor of number if is not prime"""
    _factor = []
    _divisor = 2

    if isprime(number) or number == 0:
        return [number]

    while True:
        if number % _divisor == 0:
            number = number / _divisor
            _factor.append(_divisor)

        else:
            _divisor += 1

        if number == 1:
            break

    return _factor


def product(*numbers):
    """Return product of all number"""
    result = 1
    for number in numbers:
        if number == 0:
            return 0
        result *= number

    return result


def plus(*numbers):
    """Return sum of numbers"""
    result = 0
    for number in numbers:
        result += number

    return result


def minus(*numbers):
    """Return substract of all number"""
    result = numbers[0]
    for number in numbers[1:]:
        result -= number

    return result


def divide(*numbers):
    """Return division of all number"""
    result = numbers[0]
    for number in numbers[1:]:
        if number == 0:
            return 0
        result /= number

    return result


def isperfect(number, _root=2):
    """Returns true if number is a perfect root"""
    factors = factor(number)

    if len(factors) % _root != 0:
        return False

    seprated = _seprater(factors, _root)
    for elements in seprated:
        lastElement = elements[0]
        for element in elements[1:]:
            if element != lastElement:
                return False

    return True


def root(number, _root=2):
    """Returns root of a number.\ndefault number 2"""
    factors = factor(number)
    _common = len(_common(factors))  # noqa: F823
    times = len(factors) / _common
    repeat = 1
    result = 1

    for element in factors:
        if repeat == times:
            result *= element
            repeat = 0

        repeat += 1

    return result


def simplest(numerator, denominator):
    """Returns simplest form of fraction"""
    _hcf = hcf(numerator, denominator)
    numerator = numerator / _hcf
    denominator = denominator / _hcf

    return Fraction(numerator, denominator)


def power(number, _power):
    """Returns a ** b"""
    return number**_power


def square(number):
    """Returns a ** 2"""
    return number**2


def cube(number):
    """Returns a ** 3"""
    return number**3


def hcf(*numbers):
    """Returns HCF of numbers"""
    if allprime(*numbers):
        return 1
    return product(*_commonise(*numbers)[0])


def lcm(*numbers):
    """Returns LCM of numbers"""
    factors = []
    degree = dict()
    result = []

    for number in numbers:
        factors.append(_combine(*factor(number)))

    for numbers in factors:
        for _number, power in numbers:
            if _number not in degree:
                degree[_number] = power

            else:
                if power > degree[_number]:
                    degree[_number] = power

    for number, power in degree.items():
        result.append(number**power)

    return product(*result)


def fractionPlus(*fractions):
    """Returns sum of fractions"""
    newFract = []
    start = 0
    end = 2
    length = len(fractions)
    odd = isodd(length)

    while True:
        if end > length:
            if odd:
                newFract.append(fractions[end - 2])
                break

            else:
                break

        _fract = fractions[start:end]
        (firstNumer, secondNumer), denom = equalDenom(*_fract)
        # Plus
        newFract.append((firstNumer + secondNumer, denom))

        start = end
        end += 2

    if len(newFract) == 1:
        return Fraction(*newFract[0])

    return fractionPlus(*newFract)


def fractionMinus(*fractions):
    """Returns substract of fractions"""
    if len(fractions) == 2:
        (firstNumer, secondNumer), denom = equalDenom(*fractions)
        return Fraction(firstNumer - secondNumer, denom)

    numer, denom = _fractionCal(*fractions)
    newNumer = minus(*numer)
    return Fraction(newNumer, denom)


def fractionProduct(*fractions):
    """Returns product of fractions"""
    numerator = []
    denominator = []

    for _fraction in fractions:
        numer = _fraction[0]
        if len(_fraction) == 2:
            denom = _fraction[1]
            if denom < 0:
                numer *= -1
                denom *= -1

            numerator.append(numer)
            denominator.append(denom)

        elif len(_fraction) == 1:
            numerator.append(numer)
            denominator.append(1)

        else:
            pass

    return Fraction(product(*numerator), product(*denominator))


def fractionDivide(*fractions):
    """Returns divide of fractions"""
    numerator = [fractions[0][0]]
    denominator = [fractions[0][1]]

    for numer, denom in fractions[1:]:
        numerator.append(denom)
        denominator.append(numer)

    return Fraction(product(*numerator), product(*denominator))


def absDenom(numer, denom):
    """Returns absolute of fraction"""
    if denom < 0:
        denom *= -1
        numer *= -1

    return Fraction(numer, denom)


def equalDenom(fractFirst, fractSecond):
    """Return (fnumer, snumer), common LCM"""
    firstNumer, firstDenom = fractFirst
    secondNumer, secondDenom = fractSecond

    if firstDenom < 0:
        firstDenom *= -1
        firstNumer *= -1

    if secondDenom < 0:
        secondDenom *= -1
        secondNumer *= -1

    denom = lcm(firstDenom, secondDenom)
    firstNumer = denom / firstDenom * firstNumer
    secondNumer = denom / secondDenom * secondNumer

    return (firstNumer, secondNumer), denom


class Divider:
    """Divider class object gives you remainder, quotient"""

    def __init__(self, number, divisor):
        self.divisor = divisor
        self.remainder = number % divisor
        number -= self.remainder
        self.quotient = number // divisor


class Fraction:
    """Class Fraction make easy to play with fractions"""

    def __init__(self, numerator, denominator=1):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator should be 'int'")

        self.numerator = numerator
        self.denominator = denominator

        if denominator == 0:
            raise ZeroDivisionError("%s(%s, 0)" % (self.__type(self), numerator))

        elif denominator < 0:
            self.denominator *= -1
            self.numerator *= -1

        commonFactor = hcf(self.numerator, self.denominator)

        self.numerator = round(self.numerator / commonFactor)
        self.denominator = round(self.denominator / commonFactor)

        self.format = self.numerator, self.denominator
        self.solve = self.numerator / self.denominator

    def __repr__(self):
        return f"{self.__class__.__name__}{self.format}"

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)

        return "%d/%d" % (self.numerator, self.denominator)

    def __error(self, value, of, msg):
        if not isinstance(value, of):
            raise TypeError(msg)

    def __type(self, _object):
        return _object.__class__.__name__

    def __add__(self, other):
        self.__error(
            other,
            Fraction,
            f"Required '{self.__type(self)}' not '{self.__type(other)}'",
        )
        fract = equalDenom(self.format, other.format)
        finalNumer = plus(*fract[0])

        return Fraction(finalNumer, fract[1])

    def __sub__(self, other):
        self.__error(
            other,
            Fraction,
            f"Required '{self.__type(self)}' not '{self.__type(other)}'",
        )
        fract = equalDenom(self.format, other.format)
        finalNumer = minus(*fract[0])

        return Fraction(finalNumer, fract[1])

    def __mul__(self, other):
        self.__error(
            other,
            Fraction,
            f"Required '{self.__type(self)}' not '{self.__type(other)}'",
        )
        selfNumer, selfDenom = self.format
        otherNumer, otherDenom = other.format

        return Fraction(selfNumer * otherNumer, selfDenom * otherDenom)

    def __truediv__(self, other):
        self.__error(
            other,
            Fraction,
            f"Required '{self.__type(self)}' not '{self.__type(other)}'",
        )
        selfNumer, selfDenom = self.format

        # Recipocal
        otherDenom, otherNumer = other.format

        return Fraction(selfNumer * otherNumer, selfDenom * otherDenom)

    def __pow__(self, number):
        if isinstance(number, float):
            number = int(number)

        else:
            self.__error(
                number, int, f"Power should be 'int' not '{number.__class__.__name__}'"
            )

        if number == 0:
            return Fraction(1)

        elif number < 0:
            numer = self.denominator
            denom = self.numerator

            absNumber = abs(number)
            denom = denom**absNumber
            numer = numer**absNumber

            return Fraction(numer, denom)

        fract = self
        for _ in range(number - 1):
            fract *= self

        return fract

    def __eq__(self, other):
        isInt = False

        if isinstance(other, int) or isinstance(other, float):
            isInt = True

        else:
            self.__error(
                other,
                Fraction,
                f"Required '{self.__type(self)}' not '{self.__type(other)}'",
            )

        if isInt:
            return self.solve == other

        (firstNumer, secondNumer), commonDenom = equalDenom(self.format, other.format)

        return firstNumer == secondNumer

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        isInt = False

        if isinstance(other, int) or isinstance(other, float):
            isInt = True
        else:
            self.__error(
                other,
                Fraction,
                f"Required '{self.__type(self)}' not '{self.__type(other)}'",
            )

        if isInt:
            return self.solve < other

        (firstNumer, secondNumer), commonDenom = equalDenom(self.format, other.format)

        return firstNumer < secondNumer

    def __gt__(self, other):
        return not self.__lt__(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)


class Shape2d:
    pass


class Shape3d:
    pass


class Square(Shape2d):
    def area(self, length):
        return length * length

    def perimeter(self, length):
        return length * 4


class Rectangle(Shape2d):
    def area(self, length, height):
        return length * height

    def perimeter(self, length, height):
        return 2 * (length + height)


class Circle(Shape2d):
    def __init__(self):
        self.pi = 3.14159

    def area(self, radius):
        return self.pi * radius**2

    def circumference(self, radius):
        return 2 * self.pi * radius
