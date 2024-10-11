import unittest

class TestFunctions(unittest.TestCase):

    def test_findNumLength(self):
        self.assertEqual(findNumLength(0), 1)
        self.assertEqual(findNumLength(12345), 5)
        self.assertEqual(findNumLength(-9876), 4)

    def test_sumOfDigits(self):
        self.assertEqual(sumOfDigits(123), 6)
        self.assertEqual(sumOfDigits(0), 0)
        self.assertEqual(sumOfDigits(-456), 15)

    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(101, 10), 1)
        self.assertEqual(gcd(56, 98), 14)

    def test_isArmstrong(self):
        self.assertTrue(isArmstrong(153))
        self.assertTrue(isArmstrong(370))
        self.assertFalse(isArmstrong(123))

    def test_countVowelsAndConsonants(self):
        self.assertEqual(countVowelsAndConsonants(1234), {'vowels': 2, 'consonants': 2})
        self.assertEqual(countVowelsAndConsonants(56789), {'vowels': 3, 'consonants': 2})

    def test_reverseInteger(self):
        self.assertEqual(reverseInteger(123), 321)
        self.assertEqual(reverseInteger(-456), -654)
        self.assertEqual(reverseInteger(1000), 1)


def sumOfDigits(number: int) -> int:
    number = abs(number)
    _sum = 0

    while number > 0:
        _sum += 1
        number //= 10

    return _sum

if __name__ == '__main__':
    print(sumOfDigits(123))
