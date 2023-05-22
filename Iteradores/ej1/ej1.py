from typing import Iterator


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


class PrimeIterator(Iterator):
    def __init__(self, maximum):
        self.maximum = maximum
        self.current = 2

    def __next__(self):
        while self.current <= self.maximum:
            if is_prime(self.current):
                prime = self.current
                self.current += 1
                return prime
            self.current += 1
        raise StopIteration()


if __name__ == '__main__':
    primes = list(PrimeIterator(15))
    print(primes)
