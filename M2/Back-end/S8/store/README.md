This store has 3 entities with the next endpoints:

- Product_api endpoints:

  - register_product

    - Rute: /products
    - Method: POST
    - Required fields: Name, Price, Amount
    - Required role: Admin
    - Ruturn: Dictionary with id product

  - get_products

    - Rute: /products
    - Method: GET
    - Required fields: None
    - Required role: None
    - Ruturn: Dictionary with all products

  - update_product

    - Rute: /products/<product_id>
    - Method: PUT
    - Required fields: Name, Price, Amount
    - Required role: Admin
    - Ruturn: Dictionary with a message

  - delete_product

    - Rute: /products/<product_id>
    - Method: DELETE
    - Required fields: Name, Price, Amount
    - Required role: Admin
    Ruturn: Dictionary with a message

- User_api endpoints:
    - register 
        - Rute: /user/register
        - Method: POST
        - Required fields: username, password
        - Required role: None
        - Ruturn: Dictionary with token

    - login
        - Rute: /user/login
        - Method: POST
        - Required fields: username, password
        - Required role: None
        - Ruturn: Dictionary with token

    - me
        - Rute: /me
        - Method: GET
        - Required fields: Token in Authorization Header 
        - Required role: Admin, User
        - Ruturn: Dictionary with user id and username

    - get_user_receipt
        - Rute: /me/receipts
        - Method: GET
        - Required fields: Token in Authorization Header
        - Required role: Admin, User
        - Ruturn: Dictionary with all receipt of the user

- Receipt_api endpoints:
    - register_receipt
        - Rute: /receipts
        - Method: POST
        - Required fields: Token in Authorization Header, id_product, Amount
        - Required role: Admin, User
        - Ruturn: Dictionary with a message