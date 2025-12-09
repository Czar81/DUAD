import pytest


def test_create_cart(db_cart_manager, base_user):
    id_user = base_user
    result_expected = 1

    cart_created = db_cart_manager.insert_data(id_user)

    assert result_expected == cart_created


def test_get_all_cart(db_cart_manager, base_cart, ):
    id_cart = base_cart
    result_expected = [{"id": id_cart, "id_user": 1, "state": "active"}]

    carts = db_cart_manager.get_data(id_user=1)

    assert result_expected == carts

def test_get_active_cart(db_cart_manager, base_cart, ):
   id_cart = base_cart
   result_expected = [{"id": id_cart, "id_user": 1, "state": "active"}]
   carts = db_cart_manager.get_data(id_user=1)
   assert result_expected == carts

def test_updates_cart_state(db_cart_manager, base_cart):
    id_cart = base_cart
    new_state = "active"
    cart_created = db_cart_manager.insert_data(id_user=1)
    result_expected =    [
        {
            'id': id_cart,
            'id_user': 1,
            'state': 'inactive',
        },
        {
            'id': cart_created,
            'id_user': 1,
            'state': 'active',
        },
    ]

    updated = db_cart_manager.update_data(id_cart=2, state=new_state, id_user=1)
    carts = db_cart_manager.get_data(id_user=1)

    assert updated == True
    assert carts == result_expected


def test_delete_cart(db_cart_manager, base_cart):
    id_cart = base_cart
    result_expected = "Not carts found"
    deleted = db_cart_manager.delete_data(id_cart, 1)
    carts = db_cart_manager.get_data(id_user=1)

    assert deleted == True
    assert carts == result_expected
