import pytest
from my_modules.return_string import reversed_string

def test_reversed_string_short_string():
    # Arrage
    string = "The only way to do great work is to love what you do"
    expected_string = "od uoy tahw evol ot si krow taerg od ot yaw ylno ehT"

    # Act
    result = reversed_string(string)

    # Assert
    assert result == expected_string


def test_reversed_string_large_string():
    # Arrage
    string =   "Today, mom died. Or maybe yesterday, I don’t know. I received a telegram from the nursing home: ‘Mother deceased. Funeral tomorrow. Sincere condolences. That doesn’t mean anything. Maybe it was yesterday."
    expected_string = ".yadretsey saw ti ebyaM .gnihtyna naem t’nseod tahT .secnelodnoc erecniS .worromot larenuF .desaeced rehtoM‘ :emoh gnisrun eht morf margelet a deviecer I .wonk t’nod I ,yadretsey ebyam rO .deid mom ,yadoT"

    # Act
    result = reversed_string(string)

    # Assert
    assert result == expected_string


def test_reversed_string_throw_when_is_not_string():
    # Arrage
    invalid_argument = 500

    # Act Assert
    with pytest.raises(TypeError):
        reversed_string(invalid_argument)