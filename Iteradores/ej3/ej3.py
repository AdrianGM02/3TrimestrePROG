def is_prime(number):
    if number < 2:
        return False
    for i_ in range(2, int(number ** 0.5) + 1):
        if number % i_ == 0:
            return False
    return True


def PrimeIterator(number: int):
    prime_number = 2
    for _ in range(number + 1):
        if is_prime(prime_number):
            yield prime_number
        prime_number += 1


if __name__ == '__main__':
    for n in (PrimeIterator(20)):
        print(f"{n}")
