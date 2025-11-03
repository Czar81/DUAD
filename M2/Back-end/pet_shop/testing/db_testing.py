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
            data["id_user"] = self.__get_input("Id: ", int)
            #data["name"] = self.__get_input("Name: ")
            #data["password"] = self.__get_input("Password: ")
            #data["role"] = self.__get_input("Role: ")
        elif entity_name == "Product":
            data["id_product"] = self.__get_input("Id: ", int)
            #data["sku"] = self.__get_input("SKU: ")
            #data["name"] = self.__get_input("Name: ")
            #data["price"] = self.__get_input("Price: ", int)
            #data["amount"] = self.__get_input("Amount: ", int)
        elif entity_name == "Address":
            data["id_address"] = self.__get_input("Id: ", int)
            data["id_user"] = self.__get_input("User id: ", int)
            #data["location"] = self.__get_input("Location: ")
        elif entity_name == "Payment":
            data["id_payment"] = self.__get_input("Id: ", int)
            data["id_user"] = self.__get_input("User id: ", int)
            #data["type"] = self.__get_input("Type: ")
            #data["data"] = self.__get_input("Data: ")
        elif entity_name == "Cart":
            data["id_cart"] = self.__get_input("Id: ", int)
            data["id_user"] = self.__get_input("User id: ", int)
            #data["state"] = self.__get_input("State: ")
        elif entity_name == "Cart Item":
            data["id_item"] = self.__get_input("Id: ", int)
            data["id_user"] = self.__get_input("User id: ", int)
            #data["id_cart"] = self.__get_input("Cart id: ", int)
            #data["amount"] = self.__get_input("Amount: ", int)
        elif entity_name == "Receipt":
            data["id_receipt"] = self.__get_input("Id: ", int)
            #data["id_cart"] = self.__get_input("Cart id: ", int)
            data["id_user"]= self.__get_input("Id user: ", int)
            #data["entry_date"] = self.__get_input("Entry date: ")
            #data["state"] = self.__get_input("State: ")
        else:
            print(f"No input defined for {entity_name}")
        return data

    def perform_action(self, action, manager, data):
        actions = {
            1: manager.insert_data,
            2: manager.get_data,
            3: manager.update_data,
            4: manager.delete_data,
        }
        try:
            func = actions.get(action)
            if func:
                if action == 2:
                    result=func(**data)
                    print(result)
                else:
                    func(**data)
                    print("Action completed successfully!")
            else:
                print("Invalid action")
        except Exception as e:
            print(f"Error performing action: {e}")

    def __get_input(self, prompt, cast=str):
        value = input(prompt).strip()
        if value == "":
            return None
        try:
            return cast(value)
        except ValueError:
            print(f"Invalid value for {prompt.strip(': ')}. Using None.")
            return None