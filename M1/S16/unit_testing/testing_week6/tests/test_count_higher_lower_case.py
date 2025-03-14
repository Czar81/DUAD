import pytest
from my_modules.count_higher_lower_case import UpperLower

def test_upper_lower_return_amount_with_all_upper_cases():
    # Arrage
    string = "THIS IS A STRING WITH ALL UPPER LETTERS"
    upper_lower = UpperLower()
    # Act
    upper_lower.amount_upper_lower(string)

    # Assert
    assert upper_lower.get_upper_count() == 32


def test_upper_lower_return_amount_with_all_lower_cases():
    # Arrage
    string = "this is a string with all lower letters"
    upper_lower = UpperLower()

    # Act
    upper_lower.amount_upper_lower(string)

    # Assert
    assert upper_lower.get_lower_count() == 32


def test_upper_lower_return_none_with_empty_string():
    # Arrage
    empty_string = ""
    upper_lower = UpperLower()

    
    # Act
    upper_lower.amount_upper_lower(empty_string)
    
    # Assert
    assert upper_lower.get_lower_count() == 0  
    assert upper_lower.get_upper_count() == 0