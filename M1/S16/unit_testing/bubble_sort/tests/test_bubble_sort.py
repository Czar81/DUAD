import pytest
from my_module.bubble_sort import bubble_sort_list
def test_bubble_sort_list_sort_small_list():
    # Arrange 
    disordered_list = [23, 5, 17, 12, 30, 8, 19, 3, 14, 25, 1, 28, 10, 7, 21, 16, 4, 27, 9, 20, 2, 29, 11, 6, 18, 13, 26, 15, 22, 24]
    expected_ordered_list  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    
    # Act
    sorted_list = bubble_sort_list(disordered_list)

    # Assert
    assert sorted_list == expected_ordered_list 

def test_bubble_sort_list_sort_big_list():
    # Arrange
    disordered_list = [
    64, 23, 89, 42, 17, 55, 91, 10, 78, 36,
    5, 72, 29, 83, 14, 60, 97, 3, 45, 68,
    21, 50, 87, 33, 12, 76, 39, 94, 7, 81,
    26, 58, 19, 70, 48, 99, 1, 66, 31, 53,
    8, 74, 25, 90, 16, 62, 37, 85, 20, 57,
    4, 79, 28, 65, 13, 52, 96, 2, 47, 71,
    22, 59, 38, 84, 11, 69, 34, 98, 6, 80,
    27, 56, 18, 63, 40, 92, 9, 73, 30, 54,
    15, 67, 24, 88, 35, 61, 44, 95, 32, 77,
    49, 82, 41, 93, 46, 75, 43, 86, 51, 100
]
    expected_ordered_list  = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
    51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
    61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
    71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
    81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
    91, 92, 93, 94, 95, 96, 97, 98, 99, 100
]
    
    # Act
    sorted_list = bubble_sort_list(disordered_list)

    # Assert
    assert sorted_list == expected_ordered_list 


def test_bubble_sort_list_return_empty_with_empty_list():
    # Arrange
    list = []

    # Act
    sorted_list = bubble_sort_list(list)

    # Assert
    assert sorted_list == []


def test_bubble_sort_list_throws_exception_when_is_not_list():
    # Arrange
    invalid_input = "hello"

    # Act Assert
    
    with pytest.raises(TypeError):
        bubble_sort_list(invalid_input)