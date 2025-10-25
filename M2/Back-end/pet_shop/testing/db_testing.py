from db.sell_module.db_product_manager import DbProductManager
from db.sell_module.db_cart_item_manager import DbCartItemsManager
from db.sell_module.db_cart_manager import DbCartManager
from db.sell_module.db_receipt_manager import DbReceiptManager
from db.user_module.db_user_manager import DbUserManager
from db.user_module.db_address_manager import DbAddressManager
from db.user_module.db_payment_manager import DbPaymentManager


class DbTestingManager:
    def __init__(self):
        # Crear instancias de todos los managers una sola vez
        self.managers = {
            1: ("User", DbUserManager()),
            2: ("Product", DbProductManager()),
            3: ("Address", DbAddressManager()),
            4: ("Payment", DbPaymentManager()),
            5: ("Cart", DbCartManager()),
            6: ("Cart Item", DbCartItemsManager()),
            7: ("Receipt", DbReceiptManager()),
        }

    def menu(self):
        option = 0
        while option != 5:
            print(
                """----------------------------------
------- Select one option --------
----------------------------------
1. Insert data
2. Get data
3. Update data
4. Delete data
5. Exit
----------------------------------
"""
            )
            try:
                option = int(input("Select option: "))
                if option < 1 or option > 5:
                    print("Error, option does not exist")
                    continue
                if option == 5:
                    print("Exiting...")
                    break
                self.submenu(option)
            except ValueError:
                print("Error, input must be a number")

    def submenu(self, action):
        while True:
            print(
                """----------------------------------
------- Select one entity --------
----------------------------------
1. User
2. Product 
3. Address
4. Payment
5. Cart
6. Cart Item
7. Receipt
8. Return
----------------------------------
"""
            )
            try:
                choice = int(input("Select entity: "))
                if choice < 1 or choice > 8:
                    print("Error, option does not exist")
                    continue
                if choice == 8:
                    return  # Regresa al menú principal

                entity_name, manager = self.managers[choice]
                data = self.get_input_for_entity(entity_name)
                self.perform_action(action, manager, data)

            except ValueError:
                print("Error, input must be a number")

    def get_input_for_entity(self, entity_name):
        data = {}
        if entity_name == "User":
            data["name"] = input("Name: ")
            data["password"] = input("Password: ")
            data["role"] = input("Role: ")
        elif entity_name == "Product":
            data["sku"] = input("SKU: ")
            data["name"] = input("Name: ")
            data["price"] = int(input("Price: "))
            data["amount"] = int(input("Amount: "))
        elif entity_name == "Address":
            data["id_user"] = int(input("User id: "))
            data["location"] = input("Location: ")
        elif entity_name == "Payment":
            data["id_user"] = int(input("User id: "))
            data["type"] = input("Type: ")
            data["data"] = input("Data: ")
        elif entity_name == "Cart":
            data["id_user"] = int(input("User id: "))
            data["state"] = input("State: ")
        elif entity_name == "Cart Item":
            data["id_cart"] = int(input("Cart id: "))
            data["id_product"] = int(input("Product id: "))
            data["amount"] = int(input("Amount: "))
        elif entity_name == "Receipt":
            data["id_cart"] = int(input("Cart id: "))
            data["id_address"] = int(input("Address id: "))
            data["id_payment"] = int(input("Payment id: "))
            data["state"] = input("State: ")
        else:
            print(f"No input defined for {entity_name}")
        return data

    def perform_action(self, action, manager, data):
        actions = {
            1: manager.insert,
            2: manager.get,
            3: manager.update,
            4: manager.delete,
        }
        try:
            func = actions.get(action)
            if func:
                func(**data)
                print("Action completed successfully!")
            else:
                print("Invalid action")
        except Exception as e:
            print(f"Error performing action: {e}")
