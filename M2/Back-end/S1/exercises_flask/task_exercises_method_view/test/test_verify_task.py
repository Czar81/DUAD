import pytest
from scripts.verify_task import verify

def test_good_functionality_return_true_and_message_none():
    # Arrage
    request = {
    "id": 1,
    "title":"Test",
    "description":"This is a test",
    "state":"in progress"
}
    expected_verified, expected_message = True, None
    # Act
    response_verified, response_message = verify(request)
    # Assert
    assert response_verified == expected_verified and response_message == expected_message


def test_all_input_blank_return_false_and_message_with_element():
    # Arrage
    request = {
    "id": None,
    "title":"",
    "description":"",
    "state":""
}
    expected_verified, expected_message = False, "invalid request blank space in id"
    # Act
    response_verified, response_message = verify(request)

    # Assert
    assert response_verified == expected_verified and response_message == expected_message


def test_int_on_state_return_false_and_message():
    # Arrage
    request = {
    "id": 1,
    "title":"Test",
    "description":"This is a test",
    "state": 2
}
    expected_verified, expected_message = False, "invalid state of the task"
    # Act
    response_verified, response_message = verify(request)

    # Assert
    assert response_verified == expected_verified and response_message == expected_message

def test_string_on_id_return_false_and_message():
    # Arrage
    request = {
    "id": "a",
    "title":"Test",
    "description":"This is a test",
    "state": "ready"
}
    expected_verified, expected_message = False, "invalid id"
    
    # Act
    response_verified, response_message = verify(request)

    # Assert
    assert response_verified == expected_verified and response_message == expected_message