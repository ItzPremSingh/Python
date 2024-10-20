from timeit import timeit


class Solution:
    def countPrimes(self, n) -> int:
        def isPrime(n: int) -> bool:
            if n == 2:
                return True

            if n % 2 == 0:
                return False

            for i in range(3, n, 2):
                if n % i == 0:
                    return False
            return True

        return list(filter(isPrime, range(2, n + 1))).__len__()

    def countPrime(self, n) -> int:
        def isPrime(n: int) -> bool:
            if n % 2 == 0:
                return False

            for i in range(3, n, 2):
                if n % i == 0:
                    return False

            return True

        count = 1
        for i in range(3, n + 1):
            if isPrime(i):
                count += 1

        return count


print(timeit(stmt="Solution().countPrimes(103952)", globals=globals(), number=1))
print(timeit(stmt="Solution().countPrime(103952)", globals=globals(), number=1))
