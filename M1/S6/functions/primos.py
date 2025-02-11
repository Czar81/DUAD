import math
def verify_prime(list_numbers):
    prime_numbers = []
    for number in list_numbers:
        if is_prime(number):
            prime_numbers.append(number)
    print(prime_numbers)


def is_prime(number):
    for i in range(2, int(math.sqrt(number))+1):
        if number%i == 0:
            return False
    return True


list_numbers = [93,60, 77, 11, 22]
verify_prime(list_numbers)