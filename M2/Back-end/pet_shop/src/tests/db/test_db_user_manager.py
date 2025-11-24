import pytest
from src.db import DbUserManager, TablesManager
from sqlalchemy import inspect


def test_create_user(db_user_manager):
    username = "Ian"
    password = "2NFD9JDFI4324NJF20"
    result_expected = 1

    id_user = db_user_manager.insert_data(username, password)

    assert id_user == result_expected


def test_create_admin(db_user_manager):
    username = "Czar"
    password = "2NFD9JDsdaFI4324NJF20"
    role = "admin"

    result_expected = 1

    id_user = db_user_manager.insert_data(username, password, role)

    assert id_user == result_expected


def test_get_users(db_user_manager):
    username = "Czar"
    password = "2NFD9JDsdaFI4324NJF20"
    result_expected = [
        {"id": 1, "username": "Czar", "password": "2NFD9JDsdaFI4324NJF20", "role":"user"}
    ]

    id_user = db_user_manager.insert_data(username, password)
    users = db_user_manager.get_data()

    assert users == result_expected


def test_login(db_user_manager):
    username = "Czar"
    password = "2NFD9JDsdaFI4324NJF20"
    result_expected = 1

    id_user = db_user_manager.insert_data(username, password)
    me = db_user_manager.get_user(username, password)

    assert me == result_expected


def test_get_role(db_user_manager):
    id_user = 1
    username = "Czar"
    password = "2NFD9JDsdaFI4324NJF20"
    result_expected = "user"

    id_user = db_user_manager.insert_data(username, password)
    role = db_user_manager.get_role_by_id(id_user)

    assert role == result_expected


def test_update_all_args_user(db_user_manager):
    id_user = 1
    username = "Czar"
    password = "2NFD9JDsdaFI4324NJF20"
    new_username = "Claro"
    new_password = "e4d909c290d0fb1ca068ffaddf22cbd0"
    role = "vendor"
    result_expected = True

    id_user = db_user_manager.insert_data(username, password)
    result = db_user_manager.update_data(id_user, new_username, new_password, role)
    assert result == result_expected


def test_update_one_args_user(db_user_manager):
    id_user = 1
    username = "Czar"
    password = "2NFD9JDsdaFI4324NJF20"
    new_username = "Nutrisource"
    result_expected = True

    id_user = db_user_manager.insert_data(username, password)
    result = db_user_manager.update_data(id_user, new_username)
    assert result == result_expected


def test_delete_user(db_user_manager):
    id_user = 1
    username = "Ian"
    password = "2NFD9JDFI4324NJF20"
    result_expected = True

    id_user = db_user_manager.insert_data(username, password)
    result = db_user_manager.delete_data(id_user)

    assert result == result_expected
