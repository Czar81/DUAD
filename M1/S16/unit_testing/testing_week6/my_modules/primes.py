import math
def verify_prime_numbers(list_numbers):
    __verify_if_is_list(list_numbers)
    prime_numbers = []
    for number in list_numbers:
        if __is_prime(number):
            prime_numbers.append(number)
    return(prime_numbers)


def __is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if number%i == 0:
            return False
    return True


def __verify_if_is_list(list_numbers):
    if not isinstance(list_numbers, list):
            raise TypeError