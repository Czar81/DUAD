import pytest
from my_modules.sum_list_items import sum_list

def test_sum_list_return_sum_with_small_numbers():
    # Arrage
    numbers = [4, 8, 15, 16, 23, 42]

    # Act
    result_sum_list = sum_list(numbers)

    # Assert
    assert result_sum_list == 108

def test_sum_list_return_sum_with_big_list():
    # Arrage
    numbers = [123456, 789012, 345678, 901234, 567890]
    # Act
    result_sum_list = sum_list(numbers)

    # Assert
    assert result_sum_list == 2727270


def test_sum_list_throw_exeption_when_is_not_list():
    # Arrage 
    invalid_argument = "Hello"
    
    # Act Assert
    with pytest.raises(TypeError):
        sum_list(invalid_argument)