import pytest
from my_modules.primes import verify_prime_numbers

def test_verify_prime_numbers_return_prime_numbers_with_100_numbers():
    # Arrage
    numbers = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
    61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
    81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    excepted_prime_numbes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 
    47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    # Act
    prime_numbers = verify_prime_numbers(numbers)

    # Assert
    assert prime_numbers == excepted_prime_numbes

def test_verify_prime_numbers_return_prime_numbers_with_15_numbers():
    # Arrage
    numbers = [4, 7, 15, 23, 29, 34, 37, 42, 53, 60, 67, 71, 78, 83, 97]
    excepted_prime_numbes = [7, 23, 29, 37, 53, 67, 71, 83, 97]
    
    # Act
    prime_numbers = verify_prime_numbers(numbers)
    
    # Assert
    assert prime_numbers == excepted_prime_numbes


def test_verify_prime_numbers_throws_exception_when_is_not_int():
    # Arrage
    invalid_argument = "Hello"
    # Act Assert
    with pytest.raises(TypeError):
        verify_prime_numbers(invalid_argument)
